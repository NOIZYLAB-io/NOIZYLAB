"""
GABRIEL Python SDK

Official Python SDK for the GABRIEL board inspection API.

Usage:
    from gabriel import GabrielClient
    
    client = GabrielClient(api_key='gab_live_xxx')
    scan = client.scan.create(open('board.jpg', 'rb'))
    result = client.scan.wait_for_completion(scan['scanId'])
"""

import time
import hmac
import hashlib
import base64
from typing import Optional, Dict, Any, List, BinaryIO, Union
from dataclasses import dataclass
from enum import Enum
import json

try:
    import httpx
except ImportError:
    httpx = None
    import urllib.request
    import urllib.error


class Severity(Enum):
    CRITICAL = 'critical'
    WARNING = 'warning'
    INFO = 'info'


class IssueType(Enum):
    DAMAGED = 'damaged'
    MISSING = 'missing'
    MISALIGNED = 'misaligned'
    COLD_SOLDER = 'cold_solder'
    BRIDGED = 'bridged'


@dataclass
class Issue:
    id: str
    component: str
    type: IssueType
    severity: Severity
    description: str
    confidence: float
    location: Dict[str, float]
    repair_guide: Optional[str] = None


@dataclass
class ScanResult:
    scan_id: str
    status: str
    board_type: Optional[str] = None
    confidence: Optional[float] = None
    issues: Optional[List[Issue]] = None
    metadata: Optional[Dict[str, Any]] = None
    created_at: Optional[str] = None
    completed_at: Optional[str] = None

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'ScanResult':
        issues = None
        if data.get('issues'):
            issues = [
                Issue(
                    id=i['id'],
                    component=i['component'],
                    type=IssueType(i['type']),
                    severity=Severity(i['severity']),
                    description=i['description'],
                    confidence=i['confidence'],
                    location=i['location'],
                    repair_guide=i.get('repairGuide')
                )
                for i in data['issues']
            ]
        
        return cls(
            scan_id=data['scanId'],
            status=data['status'],
            board_type=data.get('boardType'),
            confidence=data.get('confidence'),
            issues=issues,
            metadata=data.get('metadata'),
            created_at=data.get('createdAt'),
            completed_at=data.get('completedAt')
        )


# ============================================================================
# EXCEPTIONS
# ============================================================================

class GabrielError(Exception):
    """Base exception for GABRIEL API errors"""
    def __init__(self, message: str, status_code: int = 0, code: str = 'unknown'):
        super().__init__(message)
        self.message = message
        self.status_code = status_code
        self.code = code


class AuthenticationError(GabrielError):
    """Raised when API key is invalid or missing"""
    def __init__(self, message: str = 'Invalid or missing API key'):
        super().__init__(message, 401, 'authentication_error')


class RateLimitError(GabrielError):
    """Raised when rate limit is exceeded"""
    def __init__(self, retry_after: int, message: str = 'Rate limit exceeded'):
        super().__init__(message, 429, 'rate_limit_error')
        self.retry_after = retry_after


class ScanTimeoutError(GabrielError):
    """Raised when scan does not complete within timeout"""
    def __init__(self, scan_id: str, max_wait: int):
        super().__init__(f'Scan {scan_id} timed out after {max_wait}s', 408, 'timeout')
        self.scan_id = scan_id
        self.max_wait = max_wait


# ============================================================================
# HTTP CLIENT
# ============================================================================

class HTTPClient:
    """HTTP client with support for httpx or urllib fallback"""
    
    def __init__(self, base_url: str, api_key: str, timeout: int = 30):
        self.base_url = base_url
        self.api_key = api_key
        self.timeout = timeout
        self._httpx_client = None
        
        if httpx:
            self._httpx_client = httpx.Client(timeout=timeout)
    
    def request(
        self,
        method: str,
        path: str,
        json_data: Optional[Dict] = None,
        files: Optional[Dict] = None
    ) -> Dict[str, Any]:
        url = f'{self.base_url}{path}'
        headers = {'Authorization': f'Bearer {self.api_key}'}
        
        if self._httpx_client:
            return self._request_httpx(method, url, headers, json_data, files)
        else:
            return self._request_urllib(method, url, headers, json_data, files)
    
    def _request_httpx(
        self,
        method: str,
        url: str,
        headers: Dict,
        json_data: Optional[Dict],
        files: Optional[Dict]
    ) -> Dict[str, Any]:
        kwargs = {'headers': headers}
        
        if json_data:
            kwargs['json'] = json_data
        if files:
            kwargs['files'] = files
        
        response = self._httpx_client.request(method, url, **kwargs)
        
        if response.status_code >= 400:
            self._handle_error(response.status_code, response.text, response.headers)
        
        return response.json()
    
    def _request_urllib(
        self,
        method: str,
        url: str,
        headers: Dict,
        json_data: Optional[Dict],
        files: Optional[Dict]
    ) -> Dict[str, Any]:
        data = None
        
        if json_data:
            headers['Content-Type'] = 'application/json'
            data = json.dumps(json_data).encode()
        elif files:
            # Simple multipart handling for urllib
            boundary = '----GabrielSDKBoundary'
            headers['Content-Type'] = f'multipart/form-data; boundary={boundary}'
            
            body_parts = []
            for name, (filename, content, content_type) in files.items():
                body_parts.append(f'--{boundary}\r\n'.encode())
                body_parts.append(
                    f'Content-Disposition: form-data; name="{name}"; filename="{filename}"\r\n'.encode()
                )
                body_parts.append(f'Content-Type: {content_type}\r\n\r\n'.encode())
                body_parts.append(content if isinstance(content, bytes) else content.read())
                body_parts.append(b'\r\n')
            body_parts.append(f'--{boundary}--\r\n'.encode())
            data = b''.join(body_parts)
        
        req = urllib.request.Request(url, data=data, headers=headers, method=method)
        
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as response:
                return json.loads(response.read().decode())
        except urllib.error.HTTPError as e:
            self._handle_error(e.code, e.read().decode(), {})
    
    def _handle_error(self, status_code: int, body: str, headers: Dict):
        try:
            data = json.loads(body)
            message = data.get('message', 'Unknown error')
        except:
            message = body or 'Unknown error'
        
        if status_code == 401:
            raise AuthenticationError(message)
        elif status_code == 429:
            retry_after = int(headers.get('Retry-After', 60))
            raise RateLimitError(retry_after, message)
        else:
            raise GabrielError(message, status_code)
    
    def close(self):
        if self._httpx_client:
            self._httpx_client.close()


# ============================================================================
# API CLASSES
# ============================================================================

class ScanAPI:
    """API for scan operations"""
    
    def __init__(self, client: HTTPClient):
        self._client = client
    
    def create(
        self,
        image: Union[bytes, BinaryIO],
        board_type: Optional[str] = None,
        user_id: Optional[str] = None,
        webhook_url: Optional[str] = None,
        priority: str = 'normal'
    ) -> Dict[str, str]:
        """Create a new scan from an image"""
        
        if hasattr(image, 'read'):
            image_data = image.read()
        else:
            image_data = image
        
        files = {'image': ('image.jpg', image_data, 'image/jpeg')}
        
        # Add additional form fields
        return self._client.request('POST', '/api/scan', files=files)
    
    def get(self, scan_id: str) -> ScanResult:
        """Get scan result by ID"""
        data = self._client.request('GET', f'/api/scan/{scan_id}')
        return ScanResult.from_dict(data)
    
    def wait_for_completion(
        self,
        scan_id: str,
        max_wait: int = 60,
        poll_interval: int = 2
    ) -> ScanResult:
        """Wait for scan to complete (polls until done)"""
        start_time = time.time()
        
        while time.time() - start_time < max_wait:
            result = self.get(scan_id)
            
            if result.status in ('complete', 'failed'):
                return result
            
            time.sleep(poll_interval)
        
        raise ScanTimeoutError(scan_id, max_wait)
    
    def list(
        self,
        page: int = 1,
        per_page: int = 20,
        status: Optional[str] = None
    ) -> Dict[str, Any]:
        """List recent scans"""
        params = f'?page={page}&perPage={per_page}'
        if status:
            params += f'&status={status}'
        
        return self._client.request('GET', f'/api/scans{params}')
    
    def delete(self, scan_id: str) -> Dict[str, bool]:
        """Delete a scan"""
        return self._client.request('DELETE', f'/api/scan/{scan_id}')


class ReferenceAPI:
    """API for golden reference operations"""
    
    def __init__(self, client: HTTPClient):
        self._client = client
    
    def upload(
        self,
        image: Union[bytes, BinaryIO],
        board_type: str,
        name: str
    ) -> Dict[str, Any]:
        """Upload a golden reference image"""
        if hasattr(image, 'read'):
            image_data = image.read()
        else:
            image_data = image
        
        files = {'image': ('reference.jpg', image_data, 'image/jpeg')}
        return self._client.request('POST', '/api/reference', files=files)
    
    def list(self) -> List[Dict[str, Any]]:
        """List all golden references"""
        response = self._client.request('GET', '/api/references')
        return response.get('references', [])
    
    def get(self, reference_id: str) -> Dict[str, Any]:
        """Get a specific reference"""
        return self._client.request('GET', f'/api/reference/{reference_id}')
    
    def delete(self, reference_id: str) -> Dict[str, bool]:
        """Delete a reference"""
        return self._client.request('DELETE', f'/api/reference/{reference_id}')


class WebhookAPI:
    """API for webhook operations"""
    
    def __init__(self, client: HTTPClient):
        self._client = client
    
    def create(self, url: str, events: List[str]) -> Dict[str, Any]:
        """Create a webhook"""
        return self._client.request('POST', '/api/webhooks', json_data={
            'url': url,
            'events': events
        })
    
    def list(self) -> List[Dict[str, Any]]:
        """List all webhooks"""
        response = self._client.request('GET', '/api/webhooks')
        return response.get('webhooks', [])
    
    def update(
        self,
        webhook_id: str,
        url: Optional[str] = None,
        events: Optional[List[str]] = None,
        active: Optional[bool] = None
    ) -> Dict[str, Any]:
        """Update a webhook"""
        data = {}
        if url is not None:
            data['url'] = url
        if events is not None:
            data['events'] = events
        if active is not None:
            data['active'] = active
        
        return self._client.request('PATCH', f'/api/webhooks/{webhook_id}', json_data=data)
    
    def delete(self, webhook_id: str) -> Dict[str, bool]:
        """Delete a webhook"""
        return self._client.request('DELETE', f'/api/webhooks/{webhook_id}')
    
    def test(self, webhook_id: str) -> Dict[str, bool]:
        """Send test webhook"""
        return self._client.request('POST', f'/api/webhooks/{webhook_id}/test')
    
    @staticmethod
    def verify(payload: str, signature: str, secret: str) -> bool:
        """Verify webhook signature"""
        expected = hmac.new(
            secret.encode(),
            payload.encode(),
            hashlib.sha256
        ).digest()
        
        try:
            received = base64.b64decode(signature)
            return hmac.compare_digest(expected, received)
        except:
            return False


class BoardAPI:
    """API for board database operations"""
    
    def __init__(self, client: HTTPClient):
        self._client = client
    
    def search(self, query: str) -> List[Dict[str, Any]]:
        """Search boards"""
        return self._client.request('GET', f'/api/boards/search?q={query}')
    
    def get(self, board_id: str) -> Dict[str, Any]:
        """Get board details"""
        return self._client.request('GET', f'/api/boards/{board_id}')
    
    def list(self) -> List[Dict[str, Any]]:
        """List all supported boards"""
        response = self._client.request('GET', '/api/boards')
        return response.get('boards', [])
    
    def get_issues(self, board_id: str) -> List[Dict[str, Any]]:
        """Get common issues for a board"""
        return self._client.request('GET', f'/api/boards/{board_id}/issues')


# ============================================================================
# MAIN CLIENT
# ============================================================================

class GabrielClient:
    """
    Official client for the GABRIEL board inspection API.
    
    Args:
        api_key: Your GABRIEL API key
        base_url: Custom API URL (optional)
        timeout: Request timeout in seconds (default: 30)
    
    Example:
        >>> client = GabrielClient(api_key='gab_live_xxx')
        >>> scan = client.scan.create(open('board.jpg', 'rb'))
        >>> result = client.scan.wait_for_completion(scan['scanId'])
        >>> print(f'Found {len(result.issues or [])} issues')
    """
    
    def __init__(
        self,
        api_key: str,
        base_url: str = 'https://api.gabriel.noizylab.com',
        timeout: int = 30
    ):
        self._http = HTTPClient(base_url, api_key, timeout)
        
        self.scan = ScanAPI(self._http)
        self.reference = ReferenceAPI(self._http)
        self.webhook = WebhookAPI(self._http)
        self.board = BoardAPI(self._http)
    
    def __enter__(self):
        return self
    
    def __exit__(self, *args):
        self.close()
    
    def close(self):
        """Close the HTTP client"""
        self._http.close()


# ============================================================================
# CONVENIENCE FUNCTIONS
# ============================================================================

def quick_scan(api_key: str, image_path: str) -> ScanResult:
    """
    Convenience function for quick single scans.
    
    Args:
        api_key: Your GABRIEL API key
        image_path: Path to the image file
    
    Returns:
        ScanResult with issues found
    
    Example:
        >>> result = quick_scan('gab_live_xxx', 'board.jpg')
        >>> for issue in result.issues or []:
        ...     print(f'{issue.component}: {issue.description}')
    """
    with GabrielClient(api_key) as client:
        with open(image_path, 'rb') as f:
            response = client.scan.create(f)
        return client.scan.wait_for_completion(response['scanId'])


__all__ = [
    'GabrielClient',
    'GabrielError',
    'AuthenticationError', 
    'RateLimitError',
    'ScanTimeoutError',
    'ScanResult',
    'Issue',
    'Severity',
    'IssueType',
    'quick_scan',
]
