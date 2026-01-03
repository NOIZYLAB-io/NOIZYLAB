import { Hono } from 'hono';
import { cors } from 'hono/cors';

interface Env {
  NETWORK_DB: D1Database;
  NETWORK_CACHE: KVNamespace;
  AI: any;
}

// ==============================================================================
// NOIZYLAB OS - NETWORK PROTOCOLS WORKER
// Complete History of Networking from ARPANET to Modern Internet
// ==============================================================================

const app = new Hono<{ Bindings: Env }>();
app.use('*', cors());

const NETWORK_PROTOCOLS = {
  // ===========================================================================
  // FOUNDATIONAL PROTOCOLS
  // ===========================================================================
  foundational: {
    // TCP/IP Suite
    tcp: {
      name: 'TCP (Transmission Control Protocol)',
      rfc: 'RFC 793',
      year: 1981,
      layer: 'Transport (Layer 4)',
      designers: ['Vint Cerf', 'Bob Kahn'],
      significance: 'Foundation of reliable internet communication',
      features: ['Connection-oriented', 'Reliable delivery', 'Flow control', 'Congestion control']
    },
    udp: {
      name: 'UDP (User Datagram Protocol)',
      rfc: 'RFC 768',
      year: 1980,
      layer: 'Transport (Layer 4)',
      significance: 'Fast, connectionless transport',
      useCases: ['Streaming', 'Gaming', 'DNS', 'VoIP']
    },
    ip: {
      name: 'IP (Internet Protocol)',
      versions: {
        ipv4: { rfc: 'RFC 791', year: 1981, addressSpace: '32-bit (~4.3 billion addresses)' },
        ipv6: { rfc: 'RFC 8200', year: 1998, addressSpace: '128-bit (340 undecillion addresses)' }
      },
      layer: 'Network (Layer 3)',
      significance: 'Universal addressing and routing'
    },
    icmp: {
      name: 'ICMP (Internet Control Message Protocol)',
      rfc: 'RFC 792',
      year: 1981,
      layer: 'Network (Layer 3)',
      significance: 'Error reporting and diagnostics (ping, traceroute)'
    },
    arp: {
      name: 'ARP (Address Resolution Protocol)',
      rfc: 'RFC 826',
      year: 1982,
      layer: 'Data Link (Layer 2)',
      significance: 'Maps IP addresses to MAC addresses'
    }
  },

  // ===========================================================================
  // APPLICATION LAYER PROTOCOLS
  // ===========================================================================
  application: {
    http: {
      name: 'HTTP (Hypertext Transfer Protocol)',
      versions: {
        http_0_9: { year: 1991, features: ['GET only', 'No headers'] },
        http_1_0: { rfc: 'RFC 1945', year: 1996, features: ['Headers', 'Status codes'] },
        http_1_1: { rfc: 'RFC 2616', year: 1997, features: ['Keep-alive', 'Chunked transfer', 'Host header'] },
        http_2: { rfc: 'RFC 7540', year: 2015, features: ['Multiplexing', 'Server push', 'Header compression', 'Binary framing'] },
        http_3: { rfc: 'RFC 9114', year: 2022, features: ['QUIC-based', 'UDP transport', 'Reduced latency'] }
      },
      layer: 'Application (Layer 7)',
      significance: 'Foundation of the World Wide Web'
    },
    https: {
      name: 'HTTPS (HTTP Secure)',
      year: 1994,
      layer: 'Application (Layer 7)',
      encryption: ['SSL (deprecated)', 'TLS 1.2', 'TLS 1.3'],
      significance: 'Encrypted web communication'
    },
    dns: {
      name: 'DNS (Domain Name System)',
      rfc: 'RFC 1035',
      year: 1987,
      designer: 'Paul Mockapetris',
      layer: 'Application (Layer 7)',
      significance: 'Translates domain names to IP addresses',
      recordTypes: ['A', 'AAAA', 'CNAME', 'MX', 'TXT', 'NS', 'SOA', 'PTR', 'SRV', 'CAA']
    },
    ftp: {
      name: 'FTP (File Transfer Protocol)',
      rfc: 'RFC 959',
      year: 1985,
      layer: 'Application (Layer 7)',
      significance: 'Early file transfer standard'
    },
    sftp: {
      name: 'SFTP (SSH File Transfer Protocol)',
      year: 2001,
      significance: 'Secure file transfer over SSH'
    },
    smtp: {
      name: 'SMTP (Simple Mail Transfer Protocol)',
      rfc: 'RFC 5321',
      year: 1982,
      layer: 'Application (Layer 7)',
      significance: 'Email sending standard'
    },
    imap: {
      name: 'IMAP (Internet Message Access Protocol)',
      rfc: 'RFC 3501',
      year: 1986,
      significance: 'Email retrieval with server-side storage'
    },
    pop3: {
      name: 'POP3 (Post Office Protocol v3)',
      rfc: 'RFC 1939',
      year: 1988,
      significance: 'Email retrieval with local storage'
    },
    ssh: {
      name: 'SSH (Secure Shell)',
      rfc: 'RFC 4253',
      year: 1995,
      designer: 'Tatu Ylönen',
      versions: ['SSH-1 (deprecated)', 'SSH-2'],
      significance: 'Secure remote access standard'
    },
    telnet: {
      name: 'Telnet',
      rfc: 'RFC 854',
      year: 1983,
      significance: 'Early remote terminal (insecure)'
    },
    ntp: {
      name: 'NTP (Network Time Protocol)',
      rfc: 'RFC 5905',
      year: 1985,
      designer: 'David Mills',
      significance: 'Time synchronization across networks'
    },
    snmp: {
      name: 'SNMP (Simple Network Management Protocol)',
      versions: ['SNMPv1', 'SNMPv2c', 'SNMPv3'],
      rfc: 'RFC 1157',
      year: 1988,
      significance: 'Network device monitoring and management'
    },
    ldap: {
      name: 'LDAP (Lightweight Directory Access Protocol)',
      rfc: 'RFC 4511',
      year: 1993,
      significance: 'Directory services protocol (Active Directory)'
    },
    dhcp: {
      name: 'DHCP (Dynamic Host Configuration Protocol)',
      rfc: 'RFC 2131',
      year: 1993,
      significance: 'Automatic IP address assignment'
    }
  },

  // ===========================================================================
  // WEB PROTOCOLS & APIs
  // ===========================================================================
  web: {
    websocket: {
      name: 'WebSocket',
      rfc: 'RFC 6455',
      year: 2011,
      significance: 'Full-duplex communication over HTTP'
    },
    grpc: {
      name: 'gRPC',
      year: 2015,
      developer: 'Google',
      significance: 'High-performance RPC framework'
    },
    graphql: {
      name: 'GraphQL',
      year: 2015,
      developer: 'Facebook',
      significance: 'Query language for APIs'
    },
    rest: {
      name: 'REST (Representational State Transfer)',
      year: 2000,
      designer: 'Roy Fielding',
      significance: 'Architectural style for web services'
    },
    soap: {
      name: 'SOAP (Simple Object Access Protocol)',
      year: 1998,
      significance: 'XML-based messaging protocol'
    },
    oauth: {
      name: 'OAuth',
      versions: ['OAuth 1.0a', 'OAuth 2.0', 'OAuth 2.1'],
      year: 2007,
      significance: 'Authorization framework'
    },
    oidc: {
      name: 'OpenID Connect',
      year: 2014,
      significance: 'Authentication layer on OAuth 2.0'
    },
    jwt: {
      name: 'JWT (JSON Web Tokens)',
      rfc: 'RFC 7519',
      year: 2015,
      significance: 'Compact claims representation'
    },
    quic: {
      name: 'QUIC',
      rfc: 'RFC 9000',
      year: 2021,
      developer: 'Google',
      significance: 'UDP-based transport, powers HTTP/3'
    },
    webrtc: {
      name: 'WebRTC',
      year: 2011,
      significance: 'Real-time communication in browsers'
    }
  },

  // ===========================================================================
  // ROUTING PROTOCOLS
  // ===========================================================================
  routing: {
    bgp: {
      name: 'BGP (Border Gateway Protocol)',
      rfc: 'RFC 4271',
      year: 1989,
      version: 'BGP-4',
      significance: 'Internet backbone routing (the protocol that runs the internet)'
    },
    ospf: {
      name: 'OSPF (Open Shortest Path First)',
      rfc: 'RFC 2328',
      year: 1989,
      type: 'Link-state',
      significance: 'Enterprise interior routing'
    },
    rip: {
      name: 'RIP (Routing Information Protocol)',
      rfc: 'RFC 2453',
      year: 1988,
      versions: ['RIPv1', 'RIPv2', 'RIPng'],
      type: 'Distance-vector',
      significance: 'Simple, legacy routing'
    },
    eigrp: {
      name: 'EIGRP (Enhanced Interior Gateway Routing Protocol)',
      year: 1992,
      developer: 'Cisco',
      type: 'Hybrid',
      significance: 'Cisco proprietary (now open)'
    },
    isis: {
      name: 'IS-IS (Intermediate System to Intermediate System)',
      year: 1992,
      type: 'Link-state',
      significance: 'Large ISP routing'
    },
    mpls: {
      name: 'MPLS (Multiprotocol Label Switching)',
      rfc: 'RFC 3031',
      year: 2001,
      significance: 'High-performance packet forwarding'
    }
  },

  // ===========================================================================
  // SECURITY PROTOCOLS
  // ===========================================================================
  security: {
    tls: {
      name: 'TLS (Transport Layer Security)',
      versions: {
        ssl_2: { year: 1995, status: 'Deprecated' },
        ssl_3: { year: 1996, status: 'Deprecated' },
        tls_1_0: { rfc: 'RFC 2246', year: 1999, status: 'Deprecated' },
        tls_1_1: { rfc: 'RFC 4346', year: 2006, status: 'Deprecated' },
        tls_1_2: { rfc: 'RFC 5246', year: 2008, status: 'Active' },
        tls_1_3: { rfc: 'RFC 8446', year: 2018, status: 'Current' }
      },
      significance: 'Encryption standard for internet'
    },
    ipsec: {
      name: 'IPsec',
      rfc: 'RFC 4301',
      year: 1995,
      significance: 'Network layer security (VPNs)'
    },
    wireguard: {
      name: 'WireGuard',
      year: 2016,
      designer: 'Jason Donenfeld',
      significance: 'Modern VPN protocol'
    },
    openvpn: {
      name: 'OpenVPN',
      year: 2001,
      significance: 'Popular open-source VPN'
    },
    kerberos: {
      name: 'Kerberos',
      version: 'V5',
      rfc: 'RFC 4120',
      year: 1988,
      developer: 'MIT',
      significance: 'Network authentication protocol'
    },
    radius: {
      name: 'RADIUS',
      rfc: 'RFC 2865',
      year: 1997,
      significance: 'AAA protocol for network access'
    },
    dnssec: {
      name: 'DNSSEC',
      rfc: 'RFC 4033',
      year: 2005,
      significance: 'DNS security extensions'
    },
    doh: {
      name: 'DNS over HTTPS (DoH)',
      rfc: 'RFC 8484',
      year: 2018,
      significance: 'Encrypted DNS queries'
    },
    dot: {
      name: 'DNS over TLS (DoT)',
      rfc: 'RFC 7858',
      year: 2016,
      significance: 'Encrypted DNS transport'
    }
  },

  // ===========================================================================
  // DATA LINK & PHYSICAL
  // ===========================================================================
  dataLink: {
    ethernet: {
      name: 'Ethernet',
      year: 1973,
      designers: ['Robert Metcalfe', 'David Boggs'],
      company: 'Xerox PARC',
      standards: ['10BASE-T', '100BASE-TX', '1000BASE-T', '10GBASE-T', '25GBASE-T', '40GBASE-T', '100GBASE'],
      significance: 'Dominant LAN technology'
    },
    wifi: {
      name: 'Wi-Fi (IEEE 802.11)',
      versions: {
        '802.11b': { year: 1999, speed: '11 Mbps', band: '2.4 GHz' },
        '802.11a': { year: 1999, speed: '54 Mbps', band: '5 GHz' },
        '802.11g': { year: 2003, speed: '54 Mbps', band: '2.4 GHz' },
        '802.11n': { year: 2009, speed: '600 Mbps', marketing: 'Wi-Fi 4' },
        '802.11ac': { year: 2013, speed: '6.9 Gbps', marketing: 'Wi-Fi 5' },
        '802.11ax': { year: 2019, speed: '9.6 Gbps', marketing: 'Wi-Fi 6/6E' },
        '802.11be': { year: 2024, speed: '46 Gbps', marketing: 'Wi-Fi 7' }
      },
      significance: 'Wireless LAN standard'
    },
    bluetooth: {
      name: 'Bluetooth',
      year: 1999,
      versions: ['1.0', '2.0+EDR', '3.0+HS', '4.0 LE', '4.1', '4.2', '5.0', '5.1', '5.2', '5.3', '5.4'],
      significance: 'Short-range wireless'
    },
    ppp: {
      name: 'PPP (Point-to-Point Protocol)',
      rfc: 'RFC 1661',
      year: 1994,
      significance: 'Serial link layer protocol'
    },
    hdlc: {
      name: 'HDLC (High-Level Data Link Control)',
      year: 1979,
      significance: 'ISO standard data link protocol'
    }
  },

  // ===========================================================================
  // MESSAGING & STREAMING
  // ===========================================================================
  messaging: {
    mqtt: {
      name: 'MQTT (Message Queuing Telemetry Transport)',
      year: 1999,
      significance: 'IoT messaging standard'
    },
    amqp: {
      name: 'AMQP (Advanced Message Queuing Protocol)',
      year: 2003,
      significance: 'Enterprise message queuing'
    },
    xmpp: {
      name: 'XMPP (Extensible Messaging and Presence Protocol)',
      rfc: 'RFC 6120',
      year: 1999,
      significance: 'Instant messaging and presence'
    },
    sip: {
      name: 'SIP (Session Initiation Protocol)',
      rfc: 'RFC 3261',
      year: 1996,
      significance: 'VoIP signaling'
    },
    rtp: {
      name: 'RTP (Real-time Transport Protocol)',
      rfc: 'RFC 3550',
      year: 1996,
      significance: 'Audio/video streaming'
    },
    rtsp: {
      name: 'RTSP (Real Time Streaming Protocol)',
      rfc: 'RFC 2326',
      year: 1998,
      significance: 'Streaming media control'
    },
    hls: {
      name: 'HLS (HTTP Live Streaming)',
      year: 2009,
      developer: 'Apple',
      significance: 'Adaptive streaming over HTTP'
    },
    dash: {
      name: 'DASH (Dynamic Adaptive Streaming over HTTP)',
      year: 2012,
      significance: 'International streaming standard'
    }
  },

  // ===========================================================================
  // HISTORICAL PROTOCOLS
  // ===========================================================================
  historical: {
    ncp: {
      name: 'NCP (Network Control Protocol)',
      year: 1970,
      significance: 'Original ARPANET protocol (pre-TCP/IP)'
    },
    x25: {
      name: 'X.25',
      year: 1976,
      significance: 'ITU packet-switched standard'
    },
    frame_relay: {
      name: 'Frame Relay',
      year: 1988,
      significance: 'WAN packet-switching (mostly deprecated)'
    },
    atm: {
      name: 'ATM (Asynchronous Transfer Mode)',
      year: 1991,
      significance: 'Cell-based switching (largely deprecated)'
    },
    token_ring: {
      name: 'Token Ring (IEEE 802.5)',
      year: 1984,
      significance: 'IBM LAN technology (deprecated)'
    },
    appletalk: {
      name: 'AppleTalk',
      year: 1985,
      developer: 'Apple',
      significance: 'Apple networking (deprecated)'
    },
    ipx_spx: {
      name: 'IPX/SPX',
      year: 1983,
      developer: 'Novell',
      significance: 'NetWare networking (deprecated)'
    },
    netbeui: {
      name: 'NetBEUI',
      year: 1985,
      developer: 'IBM/Microsoft',
      significance: 'Early Windows networking (deprecated)'
    },
    decnet: {
      name: 'DECnet',
      year: 1975,
      developer: 'DEC',
      significance: 'DEC networking architecture'
    },
    sna: {
      name: 'SNA (Systems Network Architecture)',
      year: 1974,
      developer: 'IBM',
      significance: 'IBM mainframe networking'
    }
  }
};

// API Endpoints
app.get('/api/protocols/categories', (c) => {
  return c.json({ success: true, categories: Object.keys(NETWORK_PROTOCOLS) });
});

app.get('/api/protocols/search', (c) => {
  const query = (c.req.query('q') || '').toLowerCase();
  const results: any[] = [];
  
  Object.entries(NETWORK_PROTOCOLS).forEach(([category, protocols]) => {
    Object.entries(protocols).forEach(([key, proto]: [string, any]) => {
      if (
        (proto.name || key).toLowerCase().includes(query) ||
        (proto.significance && proto.significance.toLowerCase().includes(query))
      ) {
        results.push({ category, key, ...proto });
      }
    });
  });
  
  return c.json({ success: true, resultCount: results.length, results });
});

app.get('/api/protocols/category/:category', (c) => {
  const category = c.req.param('category') as keyof typeof NETWORK_PROTOCOLS;
  const data = NETWORK_PROTOCOLS[category];
  if (!data) return c.json({ error: 'Not found' }, 404);
  return c.json({ success: true, category, protocols: data });
});

app.get('/api/protocols/osi-model', (c) => {
  return c.json({
    success: true,
    layers: {
      7: { name: 'Application', protocols: ['HTTP', 'HTTPS', 'DNS', 'FTP', 'SSH', 'SMTP'] },
      6: { name: 'Presentation', protocols: ['SSL/TLS', 'MIME', 'ASCII'] },
      5: { name: 'Session', protocols: ['NetBIOS', 'PPTP', 'RPC'] },
      4: { name: 'Transport', protocols: ['TCP', 'UDP', 'QUIC', 'SCTP'] },
      3: { name: 'Network', protocols: ['IP', 'ICMP', 'OSPF', 'BGP'] },
      2: { name: 'Data Link', protocols: ['Ethernet', 'Wi-Fi', 'PPP', 'ARP'] },
      1: { name: 'Physical', protocols: ['Ethernet cables', 'Fiber optics', 'Radio waves'] }
    }
  });
});

app.get('/health', (c) => c.json({ status: 'healthy', worker: 'network-protocols-worker' }));

export default app;
