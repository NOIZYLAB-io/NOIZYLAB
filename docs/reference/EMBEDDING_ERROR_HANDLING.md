# Embedding Service Error Handling

This document explains the robust error handling system implemented for embedding service failures across the application.

## Overview

The embedding service can fail due to various reasons:
- Network connectivity issues
- Service unavailability
- Authentication failures
- Rate limiting
- Server errors

Previously, these failures would crash the entire application. Now, we have a graceful error handling system that:

1. **For Upload Operations**: Notifies the frontend and stops the process gracefully
2. **For Search Operations**: Returns empty results instead of crashing
3. **For Watchdog Operations**: Logs the error and continues without embeddings

## Components

### 1. Custom Exception Class

```python
class EmbeddingServiceError(Exception):
    """Custom exception for embedding service failures."""
    def __init__(self, message: str, service_type: str = "cloud", retry_count: int = 0):
        self.message = message
        self.service_type = service_type
        self.retry_count = retry_count
        super().__init__(self.message)
```

### 2. Error Handling Utility

```python
def handle_embedding_error(error: EmbeddingServiceError, context: str = "unknown") -> dict:
    """Handle embedding service errors consistently across the application."""
    return {
        "status": "error",
        "message": f"Embedding service unavailable: {error.message}",
        "error_type": "embedding_service_error",
        "service_type": error.service_type,
        "context": context
    }
```

## Usage Patterns

### 1. Upload Context (Critical - Must Stop Process)

**File**: `BASE/events/kb/upload_kb.py`

When embedding service fails during knowledge base upload:
- ✅ Sends error message to frontend via `error_fn`
- ✅ Stops the upload process gracefully
- ✅ Logs detailed error information
- ✅ Returns `None` to indicate failure

```python
async def fill_embeddings_functional(chunks, progress_fn, error_fn):
    try:
        embeddings = await generate_embeddings_cloud(batch=True, texts=contents)
        # Process embeddings...
    except EmbeddingServiceError as e:
        logger.error(f"Embedding service error: {e.message}")
        await error_fn(f"Embedding service failed: {e.message}")
        return None  # Stop the process
```

### 2. Search Context (Non-Critical - Return Empty Results)

**Files**: `BASE/actions/context_search.py`, `BASE/actions/swagger_search.py`, `BASE/actions/folder_search.py`

When embedding service fails during search operations:
- ✅ Returns empty results instead of crashing
- ✅ Logs the error for debugging
- ✅ Allows the application to continue functioning
- ✅ User gets "no results" instead of an error

```python
async def _perform_qdrant_search(query, kbid, limit=30):
    try:
        embeddings = await generate_embeddings_cloud(False, query)
        # Perform search...
    except EmbeddingServiceError as e:
        logger.error(f"Embedding service error: {e.message}")
        return []  # Return empty results
```

### 3. Watchdog Context (Non-Critical - Continue Without Embeddings)

**File**: `BASE/http/watchdog.py`

When embedding service fails during file monitoring:
- ✅ Logs the error but continues processing
- ✅ Skips embedding generation for affected chunks
- ✅ Allows file monitoring to continue
- ✅ Maintains system stability

```python
async def generate_embeddings_for_chunks(chunks):
    try:
        embeddings = await generate_embeddings_cloud(batch=True, texts=contents)
        # Assign embeddings...
    except EmbeddingServiceError as e:
        logger.error(f"Embedding service error: {e.message}")
        logger.warning("Continuing without embeddings due to service unavailability")
        return  # Continue without embeddings
```

## Error Flow

### Upload Process Error Flow
```
1. User starts upload
2. Chunking completes successfully
3. Embedding generation starts
4. Embedding service fails
5. Error caught by EmbeddingServiceError
6. Error message sent to frontend
7. Upload process stops gracefully
8. User sees clear error message
```

### Search Process Error Flow
```
1. User performs search
2. Search query processed
3. Embedding generation starts
4. Embedding service fails
5. Error caught by EmbeddingServiceError
6. Empty results returned
7. User sees "no results found"
8. Application continues normally
```

## Benefits

### 1. **Improved User Experience**
- Clear error messages instead of crashes
- Graceful degradation of functionality
- No data loss during uploads

### 2. **System Stability**
- Prevents cascading failures
- Maintains application availability
- Allows partial functionality when embedding service is down

### 3. **Better Debugging**
- Consistent error logging
- Context-aware error messages
- Detailed error information for troubleshooting

### 4. **Operational Resilience**
- System continues working even with embedding service issues
- Automatic recovery when service comes back online
- No manual intervention required for most failures

## Testing

Use the test script to verify error handling:

```bash
python test_embedding_error_handling.py
```

This demonstrates how different contexts handle embedding service failures.

## Monitoring

Monitor embedding service health by checking logs for:
- `EmbeddingServiceError` exceptions
- Error messages with context information
- Service availability patterns

## Future Enhancements

1. **Fallback to Local Embeddings**: Automatically switch to local embeddings when cloud service fails
2. **Retry with Exponential Backoff**: Implement smarter retry logic
3. **Health Check Endpoint**: Add embedding service health monitoring
4. **Circuit Breaker Pattern**: Prevent cascading failures during service outages

## Migration Notes

- All existing code continues to work without changes
- New error handling is backward compatible
- Legacy `Embeddings` class still functions as before
- Error handling can be gradually adopted in other parts of the codebase

