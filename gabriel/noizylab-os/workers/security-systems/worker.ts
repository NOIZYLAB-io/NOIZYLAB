import { Hono } from 'hono';
import { cors } from 'hono/cors';

interface Env { SECURITY_DB: D1Database; SECURITY_CACHE: KVNamespace; AI: any; }

const app = new Hono<{ Bindings: Env }>();
app.use('*', cors());

// ==============================================================================
// NOIZYLAB OS - SECURITY SYSTEMS WORKER
// Complete Cybersecurity History & Knowledge Base
// ==============================================================================

const SECURITY_SYSTEMS = {
    // Cryptography
    cryptography: {
        caesar_cipher: { name: 'Caesar Cipher', year: -50, significance: 'First substitution cipher' },
        enigma: { name: 'Enigma Machine', year: 1918, significance: 'WWII German encryption' },
        des: { name: 'DES (Data Encryption Standard)', year: 1977, significance: 'First federal encryption standard' },
        aes: { name: 'AES (Advanced Encryption Standard)', year: 2001, significance: 'Current symmetric encryption standard' },
        rsa: { name: 'RSA', year: 1977, pioneers: ['Rivest', 'Shamir', 'Adleman'], significance: 'First public-key cryptosystem' },
        diffie_hellman: { name: 'Diffie-Hellman Key Exchange', year: 1976, significance: 'First secure key exchange' },
        elliptic_curve: { name: 'Elliptic Curve Cryptography', year: 1985, significance: 'Efficient public-key crypto' },
        sha: { name: 'SHA Family', versions: ['SHA-1 (1995)', 'SHA-2 (2001)', 'SHA-3 (2015)'], significance: 'Hash functions' },
        bcrypt: { name: 'bcrypt', year: 1999, significance: 'Password hashing standard' },
        argon2: { name: 'Argon2', year: 2015, significance: 'Modern password hashing winner' }
    },

    // Attack Types
    attacks: {
        buffer_overflow: { name: 'Buffer Overflow', first: 1988, significance: 'Morris Worm used this' },
        sql_injection: { name: 'SQL Injection', first: 1998, significance: 'Most common web attack' },
        xss: { name: 'Cross-Site Scripting (XSS)', first: 2000, significance: 'Client-side injection' },
        csrf: { name: 'Cross-Site Request Forgery', significance: 'Session riding attack' },
        mitm: { name: 'Man-in-the-Middle', significance: 'Intercept communications' },
        ddos: { name: 'DDoS (Distributed Denial of Service)', significance: 'Overwhelm with traffic' },
        phishing: { name: 'Phishing', first: 1995, significance: 'Social engineering attack' },
        ransomware: { name: 'Ransomware', first: 1989, examples: ['WannaCry', 'NotPetya', 'LockBit'] },
        zero_day: { name: 'Zero-Day Exploit', significance: 'Unknown vulnerability exploitation' },
        apt: { name: 'APT (Advanced Persistent Threat)', significance: 'Nation-state level attacks' }
    },

    // Security Tools
    tools: {
        nmap: { name: 'Nmap', year: 1997, developer: 'Gordon Lyon', significance: 'Network scanner' },
        wireshark: { name: 'Wireshark', year: 1998, significance: 'Packet analyzer' },
        metasploit: { name: 'Metasploit', year: 2003, significance: 'Penetration testing framework' },
        burp_suite: { name: 'Burp Suite', year: 2003, significance: 'Web vulnerability scanner' },
        nessus: { name: 'Nessus', year: 1998, significance: 'Vulnerability scanner' },
        snort: { name: 'Snort', year: 1998, significance: 'IDS/IPS' },
        ossec: { name: 'OSSEC', year: 2004, significance: 'Host-based IDS' },
        splunk: { name: 'Splunk', year: 2003, significance: 'SIEM platform' },
        hashcat: { name: 'Hashcat', year: 2009, significance: 'Password cracker' },
        john_the_ripper: { name: 'John the Ripper', year: 1996, significance: 'Password cracker' }
    },

    // Notable Incidents
    incidents: {
        morris_worm: { name: 'Morris Worm', year: 1988, significance: 'First internet worm' },
        kevin_mitnick: { name: 'Kevin Mitnick Arrests', years: '1988-1995', significance: 'Most famous hacker' },
        stuxnet: { name: 'Stuxnet', year: 2010, significance: 'First cyberweapon (US/Israel vs Iran)' },
        sony_hack: { name: 'Sony Pictures Hack', year: 2014, attacker: 'North Korea' },
        equifax: { name: 'Equifax Breach', year: 2017, affected: '147 million people' },
        solarwinds: { name: 'SolarWinds Attack', year: 2020, significance: 'Supply chain attack' },
        log4j: { name: 'Log4Shell (CVE-2021-44228)', year: 2021, significance: 'Critical Java vulnerability' },
        colonial_pipeline: { name: 'Colonial Pipeline Ransomware', year: 2021, significance: 'Critical infrastructure attack' }
    },

    // Standards & Frameworks
    frameworks: {
        nist: { name: 'NIST Cybersecurity Framework', year: 2014, significance: 'US government standard' },
        iso_27001: { name: 'ISO 27001', year: 2005, significance: 'International security standard' },
        pci_dss: { name: 'PCI DSS', year: 2004, significance: 'Payment card security' },
        hipaa: { name: 'HIPAA', year: 1996, significance: 'Healthcare data protection' },
        gdpr: { name: 'GDPR', year: 2018, significance: 'EU data protection' },
        soc2: { name: 'SOC 2', significance: 'Service organization controls' },
        owasp_top_10: { name: 'OWASP Top 10', significance: 'Web application security risks' },
        mitre_attack: { name: 'MITRE ATT&CK', year: 2013, significance: 'Adversary tactics knowledge base' },
        zero_trust: { name: 'Zero Trust Architecture', significance: 'Never trust, always verify' }
    },

    // Security Technologies
    technologies: {
        firewall: { name: 'Firewall', first: 1988, significance: 'Network perimeter security' },
        vpn: { name: 'VPN', first: 1996, significance: 'Encrypted tunneling' },
        ids_ips: { name: 'IDS/IPS', significance: 'Intrusion detection/prevention' },
        waf: { name: 'WAF (Web Application Firewall)', significance: 'Web attack prevention' },
        siem: { name: 'SIEM', significance: 'Security event management' },
        edr: { name: 'EDR (Endpoint Detection & Response)', significance: 'Endpoint security' },
        xdr: { name: 'XDR (Extended Detection & Response)', significance: 'Unified security' },
        casb: { name: 'CASB', significance: 'Cloud access security broker' },
        mfa: { name: 'Multi-Factor Authentication', significance: 'Identity verification' },
        pam: { name: 'PAM (Privileged Access Management)', significance: 'Admin access control' }
    }
};

app.get('/api/security/categories', (c) => c.json({ success: true, categories: Object.keys(SECURITY_SYSTEMS) }));
app.get('/api/security/category/:cat', (c) => {
    const cat = c.req.param('cat') as keyof typeof SECURITY_SYSTEMS;
    if (!SECURITY_SYSTEMS[cat]) return c.json({ error: 'Not found' }, 404);
    return c.json({ success: true, data: SECURITY_SYSTEMS[cat] });
});
app.get('/api/security/search', (c) => {
    const q = (c.req.query('q') || '').toLowerCase();
    const results: any[] = [];
    Object.entries(SECURITY_SYSTEMS).forEach(([cat, items]) => {
        Object.entries(items).forEach(([k, v]: [string, any]) => {
            if ((v.name || k).toLowerCase().includes(q)) results.push({ category: cat, ...v });
        });
    });
    return c.json({ success: true, results });
});
app.get('/health', (c) => c.json({ status: 'healthy', worker: 'security-systems-worker' }));

export default app;
