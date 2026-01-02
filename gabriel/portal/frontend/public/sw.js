/// <reference lib="webworker" />

const CACHE_NAME = 'gabriel-v1';
const OFFLINE_URL = '/offline.html';

// Assets to cache immediately on install
const PRECACHE_ASSETS = [
  '/',
  '/index.html',
  '/offline.html',
  '/manifest.json',
  '/icons/icon-192x192.png',
  '/icons/icon-512x512.png',
];

// API routes that should use network-first strategy
const API_ROUTES = [
  '/api/scan',
  '/api/health',
  '/api/user',
];

// Cache strategies
const CACHE_STRATEGIES = {
  cacheFirst: ['image', 'font', 'style'],
  networkFirst: ['document', 'script'],
  staleWhileRevalidate: ['manifest'],
};

// ============================================================================
// INSTALL EVENT
// ============================================================================

self.addEventListener('install', (event) => {
  event.waitUntil(
    (async () => {
      const cache = await caches.open(CACHE_NAME);
      
      // Pre-cache essential assets
      await cache.addAll(PRECACHE_ASSETS);
      
      // Skip waiting to activate immediately
      await self.skipWaiting();
      
      console.log('[SW] Installed and precached assets');
    })()
  );
});

// ============================================================================
// ACTIVATE EVENT
// ============================================================================

self.addEventListener('activate', (event) => {
  event.waitUntil(
    (async () => {
      // Clean up old caches
      const cacheNames = await caches.keys();
      await Promise.all(
        cacheNames
          .filter(name => name !== CACHE_NAME)
          .map(name => caches.delete(name))
      );
      
      // Take control of all pages immediately
      await self.clients.claim();
      
      console.log('[SW] Activated and claimed clients');
    })()
  );
});

// ============================================================================
// FETCH EVENT
// ============================================================================

self.addEventListener('fetch', (event) => {
  const { request } = event;
  const url = new URL(request.url);
  
  // Skip cross-origin requests
  if (url.origin !== self.location.origin) {
    return;
  }
  
  // Handle API requests with network-first
  if (API_ROUTES.some(route => url.pathname.startsWith(route))) {
    event.respondWith(networkFirst(request));
    return;
  }
  
  // Handle navigation requests
  if (request.mode === 'navigate') {
    event.respondWith(handleNavigation(request));
    return;
  }
  
  // Use appropriate strategy based on destination
  const destination = request.destination;
  
  if (CACHE_STRATEGIES.cacheFirst.includes(destination)) {
    event.respondWith(cacheFirst(request));
  } else if (CACHE_STRATEGIES.staleWhileRevalidate.includes(destination)) {
    event.respondWith(staleWhileRevalidate(request));
  } else {
    event.respondWith(networkFirst(request));
  }
});

// ============================================================================
// CACHE STRATEGIES
// ============================================================================

async function cacheFirst(request) {
  const cached = await caches.match(request);
  
  if (cached) {
    return cached;
  }
  
  try {
    const response = await fetch(request);
    
    if (response.ok) {
      const cache = await caches.open(CACHE_NAME);
      cache.put(request, response.clone());
    }
    
    return response;
  } catch (error) {
    console.error('[SW] Cache first failed:', error);
    return new Response('Offline', { status: 503 });
  }
}

async function networkFirst(request) {
  try {
    const response = await fetch(request);
    
    if (response.ok) {
      const cache = await caches.open(CACHE_NAME);
      cache.put(request, response.clone());
    }
    
    return response;
  } catch (error) {
    const cached = await caches.match(request);
    
    if (cached) {
      return cached;
    }
    
    console.error('[SW] Network first failed:', error);
    return new Response(JSON.stringify({ error: 'Offline' }), {
      status: 503,
      headers: { 'Content-Type': 'application/json' }
    });
  }
}

async function staleWhileRevalidate(request) {
  const cache = await caches.open(CACHE_NAME);
  const cached = await caches.match(request);
  
  // Fetch in background
  const fetchPromise = fetch(request).then(response => {
    if (response.ok) {
      cache.put(request, response.clone());
    }
    return response;
  });
  
  // Return cached if available, otherwise wait for network
  return cached || fetchPromise;
}

async function handleNavigation(request) {
  try {
    // Try to get fresh version
    const preloadResponse = await event.preloadResponse;
    if (preloadResponse) {
      return preloadResponse;
    }
    
    const response = await fetch(request);
    return response;
  } catch (error) {
    // Return offline page for navigation failures
    const cached = await caches.match(OFFLINE_URL);
    return cached || new Response('Offline', { status: 503 });
  }
}

// ============================================================================
// BACKGROUND SYNC
// ============================================================================

self.addEventListener('sync', (event) => {
  if (event.tag === 'sync-scans') {
    event.waitUntil(syncPendingScans());
  }
});

async function syncPendingScans() {
  try {
    // Get pending scans from IndexedDB
    const db = await openDB();
    const pending = await getPendingScans(db);
    
    for (const scan of pending) {
      try {
        const response = await fetch('/api/scan', {
          method: 'POST',
          body: scan.formData
        });
        
        if (response.ok) {
          await removePendingScan(db, scan.id);
          
          // Notify user
          await self.registration.showNotification('Scan Uploaded', {
            body: 'Your offline scan has been processed',
            icon: '/icons/icon-192x192.png',
            badge: '/icons/badge-72x72.png',
            tag: 'scan-synced',
            data: { scanId: scan.id }
          });
        }
      } catch (err) {
        console.error('[SW] Failed to sync scan:', scan.id);
      }
    }
  } catch (error) {
    console.error('[SW] Sync failed:', error);
  }
}

// ============================================================================
// PUSH NOTIFICATIONS
// ============================================================================

self.addEventListener('push', (event) => {
  if (!event.data) return;
  
  const data = event.data.json();
  
  const options = {
    body: data.body || 'New notification from GABRIEL',
    icon: '/icons/icon-192x192.png',
    badge: '/icons/badge-72x72.png',
    vibrate: [200, 100, 200],
    tag: data.tag || 'gabriel-notification',
    renotify: true,
    data: data.data || {},
    actions: data.actions || []
  };
  
  // Add scan-specific actions
  if (data.type === 'scan_complete') {
    options.actions = [
      { action: 'view', title: 'View Results' },
      { action: 'dismiss', title: 'Dismiss' }
    ];
  }
  
  event.waitUntil(
    self.registration.showNotification(data.title || 'GABRIEL', options)
  );
});

self.addEventListener('notificationclick', (event) => {
  event.notification.close();
  
  const { action } = event;
  const { data } = event.notification;
  
  if (action === 'dismiss') {
    return;
  }
  
  let url = '/';
  
  if (action === 'view' && data.scanId) {
    url = `/scan/${data.scanId}`;
  } else if (data.url) {
    url = data.url;
  }
  
  event.waitUntil(
    clients.matchAll({ type: 'window' }).then(windowClients => {
      // Focus existing window if open
      for (const client of windowClients) {
        if (client.url.includes(url) && 'focus' in client) {
          return client.focus();
        }
      }
      
      // Open new window
      if (clients.openWindow) {
        return clients.openWindow(url);
      }
    })
  );
});

// ============================================================================
// MESSAGE HANDLING
// ============================================================================

self.addEventListener('message', (event) => {
  const { type, payload } = event.data || {};
  
  switch (type) {
    case 'SKIP_WAITING':
      self.skipWaiting();
      break;
      
    case 'CACHE_URLS':
      event.waitUntil(cacheUrls(payload.urls));
      break;
      
    case 'CLEAR_CACHE':
      event.waitUntil(clearCache());
      break;
      
    case 'GET_CACHE_SIZE':
      event.waitUntil(getCacheSize().then(size => {
        event.source.postMessage({ type: 'CACHE_SIZE', size });
      }));
      break;
  }
});

async function cacheUrls(urls) {
  const cache = await caches.open(CACHE_NAME);
  await cache.addAll(urls);
}

async function clearCache() {
  await caches.delete(CACHE_NAME);
  const cache = await caches.open(CACHE_NAME);
  await cache.addAll(PRECACHE_ASSETS);
}

async function getCacheSize() {
  const cache = await caches.open(CACHE_NAME);
  const keys = await cache.keys();
  
  let size = 0;
  for (const request of keys) {
    const response = await cache.match(request);
    const blob = await response.blob();
    size += blob.size;
  }
  
  return size;
}

// ============================================================================
// INDEXEDDB HELPERS
// ============================================================================

function openDB() {
  return new Promise((resolve, reject) => {
    const request = indexedDB.open('gabriel-offline', 1);
    
    request.onerror = () => reject(request.error);
    request.onsuccess = () => resolve(request.result);
    
    request.onupgradeneeded = (event) => {
      const db = event.target.result;
      
      if (!db.objectStoreNames.contains('pending-scans')) {
        db.createObjectStore('pending-scans', { keyPath: 'id' });
      }
    };
  });
}

function getPendingScans(db) {
  return new Promise((resolve, reject) => {
    const tx = db.transaction('pending-scans', 'readonly');
    const store = tx.objectStore('pending-scans');
    const request = store.getAll();
    
    request.onerror = () => reject(request.error);
    request.onsuccess = () => resolve(request.result);
  });
}

function removePendingScan(db, id) {
  return new Promise((resolve, reject) => {
    const tx = db.transaction('pending-scans', 'readwrite');
    const store = tx.objectStore('pending-scans');
    const request = store.delete(id);
    
    request.onerror = () => reject(request.error);
    request.onsuccess = () => resolve();
  });
}

console.log('[SW] Service Worker loaded');
