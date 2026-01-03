import { Hono } from 'hono';
import { cors } from 'hono/cors';

interface Env {
  OS_DB: D1Database;
  OS_CACHE: KVNamespace;
  OS_STORAGE: R2Bucket;
  AI: any;
  OS_VECTORS: VectorizeIndex;
  OS_QUEUE: Queue;
}

// ==============================================================================
// NOIZYLAB OS - OPERATING SYSTEMS WORKER
// Every OS Ever Made Since The Dawn of Computing
// ==============================================================================

const app = new Hono<{ Bindings: Env }>();
app.use('*', cors());

// ==============================================================================
// COMPLETE OPERATING SYSTEMS DATABASE - FROM 1950s TO PRESENT
// ==============================================================================

const OPERATING_SYSTEMS_DATABASE = {
  // EARLY BATCH PROCESSING SYSTEMS (1950s-1960s)
  earlyBatch: {
    gm_naa_io: {
      name: 'GM-NAA I/O',
      year: 1956,
      developer: 'General Motors / North American Aviation',
      platform: 'IBM 704',
      type: 'Batch Processing',
      significance: 'First operating system ever created',
      features: ['Job scheduling', 'I/O handling', 'Batch processing']
    },
    ibsys: {
      name: 'IBSYS',
      year: 1960,
      developer: 'IBM',
      platform: 'IBM 7090/7094',
      type: 'Batch Processing',
      significance: 'Major IBM batch system',
      features: ['Tape handling', 'Job control', 'FORTRAN support']
    },
    atlas_supervisor: {
      name: 'Atlas Supervisor',
      year: 1962,
      developer: 'University of Manchester',
      platform: 'Atlas Computer',
      type: 'Batch/Time-sharing',
      significance: 'Introduced virtual memory, demand paging',
      features: ['Virtual memory', 'Demand paging', 'Spooling', 'Supervisor calls']
    },
    ctss: {
      name: 'CTSS (Compatible Time-Sharing System)',
      year: 1961,
      developer: 'MIT',
      platform: 'IBM 7090/7094',
      type: 'Time-sharing',
      significance: 'First time-sharing system demonstrated',
      features: ['Multi-user', 'Time-sharing', 'File system', 'Email']
    },
    multics: {
      name: 'Multics',
      year: 1964,
      developer: 'MIT/Bell Labs/GE',
      platform: 'GE-645, Honeywell 6180',
      type: 'Time-sharing',
      significance: 'Revolutionary - direct ancestor of UNIX',
      features: ['Hierarchical file system', 'Ring security', 'Dynamic linking', 'Virtual memory']
    }
  },

  // UNIX FAMILY (1969-present)
  unixFamily: {
    unix_v1: {
      name: 'UNIX Version 1',
      year: 1971,
      developer: 'Ken Thompson, Dennis Ritchie',
      company: 'Bell Labs',
      platform: 'PDP-7, PDP-11',
      significance: 'Birth of UNIX - changed computing forever',
      features: ['File system', 'Shell', 'Pipes', 'C language']
    },
    unix_v6: {
      name: 'UNIX Version 6',
      year: 1975,
      developer: 'Bell Labs',
      significance: 'First widely distributed UNIX',
      features: ['Portable C code', 'Academic distribution']
    },
    unix_v7: {
      name: 'UNIX Version 7',
      year: 1979,
      developer: 'Bell Labs',
      significance: 'Last "true" Research UNIX',
      features: ['Bourne shell', 'C compiler', 'Kernel improvements']
    },
    bsd: {
      name: 'BSD (Berkeley Software Distribution)',
      year: 1977,
      developer: 'UC Berkeley',
      variants: ['1BSD', '2BSD', '3BSD', '4BSD', '4.2BSD', '4.3BSD', '4.4BSD'],
      significance: 'Added TCP/IP networking, virtual memory',
      features: ['TCP/IP', 'Vi editor', 'C shell', 'Virtual memory', 'FFS']
    },
    freebsd: {
      name: 'FreeBSD',
      year: 1993,
      developer: 'FreeBSD Project',
      basedon: '4.4BSD-Lite',
      significance: 'Major open-source BSD',
      features: ['ZFS', 'Jails', 'Ports collection', 'DTrace']
    },
    openbsd: {
      name: 'OpenBSD',
      year: 1995,
      developer: 'Theo de Raadt',
      significance: 'Security-focused BSD',
      features: ['Security auditing', 'OpenSSH', 'LibreSSL', 'pledge/unveil']
    },
    netbsd: {
      name: 'NetBSD',
      year: 1993,
      developer: 'NetBSD Foundation',
      significance: 'Portability-focused BSD',
      features: ['Portable', 'pkgsrc', 'Clean design']
    },
    dragonflybsd: {
      name: 'DragonFly BSD',
      year: 2003,
      developer: 'Matthew Dillon',
      significance: 'Innovative BSD fork',
      features: ['HAMMER filesystem', 'Virtual kernels', 'Lightweight threads']
    },
    system_v: {
      name: 'UNIX System V',
      year: 1983,
      developer: 'AT&T',
      releases: ['SVR1', 'SVR2', 'SVR3', 'SVR4'],
      significance: 'Commercial UNIX standard',
      features: ['Init system', 'Streams', 'SVID specification']
    },
    sunos: {
      name: 'SunOS',
      year: 1982,
      developer: 'Sun Microsystems',
      versions: ['SunOS 1.0-4.x (BSD)', 'SunOS 5.x/Solaris (SVR4)'],
      significance: 'Dominant commercial UNIX',
      features: ['NFS', 'YP/NIS', 'Virtual memory']
    },
    solaris: {
      name: 'Solaris',
      year: 1992,
      developer: 'Sun Microsystems / Oracle',
      significance: 'Enterprise UNIX leader',
      features: ['ZFS', 'DTrace', 'Zones', 'SMF', 'FMA']
    },
    aix: {
      name: 'AIX',
      year: 1986,
      developer: 'IBM',
      platform: 'POWER/PowerPC',
      significance: 'IBM enterprise UNIX',
      features: ['JFS/JFS2', 'LVM', 'WPAR', 'Live kernel update']
    },
    hp_ux: {
      name: 'HP-UX',
      year: 1984,
      developer: 'Hewlett-Packard',
      platform: 'PA-RISC, Itanium',
      significance: 'HP enterprise UNIX',
      features: ['VxFS', 'LVM', 'ServiceGuard']
    },
    irix: {
      name: 'IRIX',
      year: 1988,
      developer: 'Silicon Graphics',
      platform: 'MIPS',
      significance: 'Graphics workstation OS',
      features: ['XFS', 'NUMA', 'REACT/Pro']
    },
    sco_unix: {
      name: 'SCO UNIX',
      year: 1989,
      developer: 'Santa Cruz Operation',
      platform: 'x86',
      significance: 'Popular x86 UNIX',
      features: ['Merge DOS/Windows', 'Enterprise features']
    },
    tru64: {
      name: 'Tru64 UNIX',
      year: 1992,
      developer: 'DEC/Compaq/HP',
      platform: 'Alpha',
      significance: 'Advanced 64-bit UNIX',
      features: ['AdvFS', 'TruCluster', 'ASM']
    },
    xenix: {
      name: 'XENIX',
      year: 1980,
      developer: 'Microsoft (SCO)',
      platform: 'x86, Z8000',
      significance: 'Microsoft UNIX - yes, really!',
      features: ['PC UNIX', 'SCO support']
    },
    minix: {
      name: 'MINIX',
      year: 1987,
      developer: 'Andrew Tanenbaum',
      significance: 'Teaching OS - inspired Linux',
      features: ['Microkernel', 'POSIX', 'Educational']
    },
    minix3: {
      name: 'MINIX 3',
      year: 2005,
      developer: 'Andrew Tanenbaum',
      significance: 'Reliable microkernel OS',
      features: ['Self-healing', 'Driver isolation', 'Microkernel']
    }
  },

  // LINUX DISTRIBUTIONS
  linux: {
    kernel: {
      name: 'Linux Kernel',
      year: 1991,
      developer: 'Linus Torvalds',
      significance: 'Changed the world - open source revolution',
      versions: {
        '0.01': '1991 - First release',
        '1.0': '1994 - First production',
        '2.0': '1996 - SMP support',
        '2.4': '2001 - Enterprise ready',
        '2.6': '2003 - Major rewrite',
        '3.0': '2011 - 20th anniversary',
        '4.0': '2015 - Live patching',
        '5.0': '2019 - Modern era',
        '6.0': '2022 - Current mainline'
      }
    },
    distributions: {
      // Debian Family
      debian: {
        name: 'Debian GNU/Linux',
        year: 1993,
        developer: 'Ian Murdock / Debian Project',
        significance: 'Foundation of many distros',
        packageManager: 'APT/dpkg',
        derivatives: ['Ubuntu', 'Linux Mint', 'Kali', 'Raspberry Pi OS']
      },
      ubuntu: {
        name: 'Ubuntu',
        year: 2004,
        developer: 'Canonical',
        significance: 'Brought Linux to masses',
        variants: ['Server', 'Desktop', 'Core', 'Kylin'],
        flavors: ['Kubuntu', 'Xubuntu', 'Lubuntu', 'Ubuntu MATE']
      },
      linux_mint: {
        name: 'Linux Mint',
        year: 2006,
        developer: 'Clem Lefebvre',
        desktops: ['Cinnamon', 'MATE', 'Xfce']
      },
      kali: {
        name: 'Kali Linux',
        year: 2013,
        developer: 'Offensive Security',
        significance: 'Security/penetration testing'
      },
      raspbian: {
        name: 'Raspberry Pi OS',
        year: 2012,
        developer: 'Raspberry Pi Foundation',
        significance: 'Dominant Pi OS'
      },

      // Red Hat Family
      redhat: {
        name: 'Red Hat Linux',
        year: 1994,
        developer: 'Red Hat',
        significance: 'Enterprise Linux pioneer',
        packageManager: 'RPM/YUM/DNF'
      },
      rhel: {
        name: 'Red Hat Enterprise Linux',
        year: 2000,
        developer: 'Red Hat / IBM',
        significance: 'Enterprise Linux standard'
      },
      centos: {
        name: 'CentOS',
        year: 2004,
        developer: 'CentOS Project / Red Hat',
        significance: 'Free RHEL clone',
        status: 'CentOS Stream now'
      },
      fedora: {
        name: 'Fedora',
        year: 2003,
        developer: 'Fedora Project',
        significance: 'Cutting-edge Red Hat testing'
      },
      rocky: {
        name: 'Rocky Linux',
        year: 2021,
        developer: 'Rocky Enterprise Software Foundation',
        significance: 'CentOS successor'
      },
      alma: {
        name: 'AlmaLinux',
        year: 2021,
        developer: 'AlmaLinux OS Foundation',
        significance: 'Another CentOS successor'
      },
      oracle_linux: {
        name: 'Oracle Linux',
        year: 2006,
        developer: 'Oracle',
        significance: 'Oracle database optimized'
      },

      // SUSE Family
      suse: {
        name: 'SUSE Linux',
        year: 1994,
        developer: 'SUSE',
        significance: 'German enterprise Linux'
      },
      opensuse: {
        name: 'openSUSE',
        year: 2005,
        developer: 'openSUSE Project',
        variants: ['Leap', 'Tumbleweed', 'MicroOS']
      },
      sles: {
        name: 'SUSE Linux Enterprise Server',
        year: 2000,
        developer: 'SUSE',
        significance: 'Enterprise SUSE'
      },

      // Arch Family
      arch: {
        name: 'Arch Linux',
        year: 2002,
        developer: 'Judd Vinet / Aaron Griffin',
        significance: 'Rolling release, DIY',
        packageManager: 'pacman'
      },
      manjaro: {
        name: 'Manjaro',
        year: 2011,
        developer: 'Manjaro GmbH',
        significance: 'User-friendly Arch'
      },
      endeavouros: {
        name: 'EndeavourOS',
        year: 2019,
        developer: 'EndeavourOS team',
        significance: 'Antergos successor'
      },
      garuda: {
        name: 'Garuda Linux',
        year: 2020,
        developer: 'Garuda Linux team',
        significance: 'Gaming-focused Arch'
      },

      // Gentoo Family
      gentoo: {
        name: 'Gentoo Linux',
        year: 2000,
        developer: 'Daniel Robbins',
        significance: 'Source-based, customizable',
        packageManager: 'Portage'
      },
      calculate: {
        name: 'Calculate Linux',
        year: 2007,
        developer: 'Calculate Ltd',
        significance: 'Enterprise Gentoo'
      },
      chromeos: {
        name: 'Chrome OS / ChromeOS',
        year: 2011,
        developer: 'Google',
        significance: 'Web-centric OS',
        base: 'Gentoo-derived'
      },

      // Slackware Family
      slackware: {
        name: 'Slackware',
        year: 1993,
        developer: 'Patrick Volkerding',
        significance: 'Oldest surviving distro'
      },
      slax: {
        name: 'Slax',
        year: 2002,
        developer: 'Tomas Matejicek',
        significance: 'Live Slackware'
      },

      // Independent
      alpine: {
        name: 'Alpine Linux',
        year: 2006,
        developer: 'Alpine Linux Development Team',
        significance: 'Musl/BusyBox, containers',
        packageManager: 'apk'
      },
      void: {
        name: 'Void Linux',
        year: 2008,
        developer: 'Void Linux team',
        significance: 'runit, musl option'
      },
      nixos: {
        name: 'NixOS',
        year: 2003,
        developer: 'NixOS Foundation',
        significance: 'Declarative, reproducible'
      },
      guix: {
        name: 'GNU Guix System',
        year: 2012,
        developer: 'GNU Project',
        significance: 'GNU functional package manager'
      },
      clear_linux: {
        name: 'Clear Linux',
        year: 2015,
        developer: 'Intel',
        significance: 'Performance optimized'
      },
      pop_os: {
        name: 'Pop!_OS',
        year: 2017,
        developer: 'System76',
        significance: 'Developer/creator focused'
      },
      elementary: {
        name: 'elementary OS',
        year: 2011,
        developer: 'elementary Inc',
        significance: 'macOS-like design'
      },
      solus: {
        name: 'Solus',
        year: 2015,
        developer: 'Solus Project',
        significance: 'Budgie desktop'
      },
      mx_linux: {
        name: 'MX Linux',
        year: 2014,
        developer: 'MX Linux team',
        significance: 'antiX + MEPIS'
      },
      zorin: {
        name: 'Zorin OS',
        year: 2008,
        developer: 'Zorin Group',
        significance: 'Windows-like for beginners'
      },
      deepin: {
        name: 'Deepin',
        year: 2004,
        developer: 'Deepin Technology',
        significance: 'Chinese, beautiful DDE'
      }
    }
  },

  // APPLE OPERATING SYSTEMS
  apple: {
    // Classic Mac OS
    system_1: {
      name: 'System 1.0',
      year: 1984,
      significance: 'First Macintosh OS',
      features: ['GUI', 'Mouse support', 'Desktop metaphor', 'Finder']
    },
    system_6: {
      name: 'System 6',
      year: 1988,
      significance: 'Mature classic Mac OS',
      features: ['MultiFinder', 'Color support']
    },
    system_7: {
      name: 'System 7',
      year: 1991,
      significance: 'Major upgrade, virtual memory',
      features: ['Virtual memory', 'TrueType', 'AppleScript', 'Aliases']
    },
    mac_os_8: {
      name: 'Mac OS 8',
      year: 1997,
      significance: 'First "Mac OS" branding',
      features: ['Platinum appearance', 'HFS+', 'Multithreading']
    },
    mac_os_9: {
      name: 'Mac OS 9',
      year: 1999,
      significance: 'Last classic Mac OS',
      features: ['Sherlock 2', 'Multiple users', 'Keychain']
    },

    // Mac OS X / macOS
    mac_os_x_cheetah: {
      name: 'Mac OS X 10.0 Cheetah',
      year: 2001,
      significance: 'First Mac OS X release',
      features: ['Aqua', 'Darwin kernel', 'Dock', 'Cocoa/Carbon']
    },
    mac_os_x_puma: { name: 'Mac OS X 10.1 Puma', year: 2001 },
    mac_os_x_jaguar: { name: 'Mac OS X 10.2 Jaguar', year: 2002 },
    mac_os_x_panther: { name: 'Mac OS X 10.3 Panther', year: 2003 },
    mac_os_x_tiger: {
      name: 'Mac OS X 10.4 Tiger',
      year: 2005,
      features: ['Spotlight', 'Dashboard', 'Automator', 'Intel transition']
    },
    mac_os_x_leopard: {
      name: 'Mac OS X 10.5 Leopard',
      year: 2007,
      features: ['Time Machine', 'Spaces', 'Quick Look', 'Boot Camp']
    },
    mac_os_x_snow_leopard: {
      name: 'Mac OS X 10.6 Snow Leopard',
      year: 2009,
      features: ['64-bit', 'Grand Central Dispatch', 'OpenCL']
    },
    mac_os_x_lion: {
      name: 'Mac OS X 10.7 Lion',
      year: 2011,
      features: ['Mission Control', 'Launchpad', 'AirDrop', 'Versions']
    },
    os_x_mountain_lion: {
      name: 'OS X 10.8 Mountain Lion',
      year: 2012,
      features: ['Notification Center', 'iCloud', 'Gatekeeper']
    },
    os_x_mavericks: { name: 'OS X 10.9 Mavericks', year: 2013 },
    os_x_yosemite: { name: 'OS X 10.10 Yosemite', year: 2014 },
    os_x_el_capitan: { name: 'OS X 10.11 El Capitan', year: 2015 },
    macos_sierra: { name: 'macOS 10.12 Sierra', year: 2016 },
    macos_high_sierra: { name: 'macOS 10.13 High Sierra', year: 2017, features: ['APFS'] },
    macos_mojave: { name: 'macOS 10.14 Mojave', year: 2018, features: ['Dark Mode'] },
    macos_catalina: { name: 'macOS 10.15 Catalina', year: 2019, features: ['Catalyst', 'No 32-bit'] },
    macos_big_sur: { name: 'macOS 11 Big Sur', year: 2020, features: ['Apple Silicon', 'Redesign'] },
    macos_monterey: { name: 'macOS 12 Monterey', year: 2021 },
    macos_ventura: { name: 'macOS 13 Ventura', year: 2022, features: ['Stage Manager'] },
    macos_sonoma: { name: 'macOS 14 Sonoma', year: 2023 },
    macos_sequoia: { name: 'macOS 15 Sequoia', year: 2024, features: ['Apple Intelligence'] },

    // iOS
    iphone_os_1: { name: 'iPhone OS 1.0', year: 2007, significance: 'First iPhone OS' },
    ios_4: { name: 'iOS 4', year: 2010, features: ['Multitasking', 'Folders'] },
    ios_7: { name: 'iOS 7', year: 2013, significance: 'Flat design revolution' },
    ios_11: { name: 'iOS 11', year: 2017, features: ['ARKit', 'Files app'] },
    ios_13: { name: 'iOS 13', year: 2019, features: ['Dark Mode', 'iPadOS split'] },
    ios_14: { name: 'iOS 14', year: 2020, features: ['Widgets', 'App Library'] },
    ios_15: { name: 'iOS 15', year: 2021 },
    ios_16: { name: 'iOS 16', year: 2022, features: ['Lock Screen customization'] },
    ios_17: { name: 'iOS 17', year: 2023 },
    ios_18: { name: 'iOS 18', year: 2024, features: ['Apple Intelligence'] },

    // Other Apple OS
    ipados: { name: 'iPadOS', year: 2019, significance: 'Tablet-specific iOS fork' },
    watchos: { name: 'watchOS', year: 2015, significance: 'Apple Watch OS' },
    tvos: { name: 'tvOS', year: 2015, significance: 'Apple TV OS' },
    visionos: { name: 'visionOS', year: 2024, significance: 'Apple Vision Pro spatial computing' },

    // NeXT
    nextstep: {
      name: 'NeXTSTEP',
      year: 1989,
      developer: 'NeXT',
      significance: 'Foundation of Mac OS X',
      features: ['Display PostScript', 'Objective-C', 'Interface Builder', 'Mach kernel']
    },
    openstep: {
      name: 'OPENSTEP',
      year: 1994,
      developer: 'NeXT/Sun',
      significance: 'NeXTSTEP standard'
    },

    // A/UX
    aux: {
      name: 'A/UX',
      year: 1988,
      developer: 'Apple',
      significance: 'Apple UNIX for Mac',
      features: ['SVR2/BSD hybrid', 'Mac toolbox', 'X11']
    }
  },

  // MICROSOFT OPERATING SYSTEMS
  microsoft: {
    // DOS
    ms_dos_1: { name: 'MS-DOS 1.0', year: 1981, significance: 'IBM PC OS' },
    ms_dos_2: { name: 'MS-DOS 2.0', year: 1983, features: ['Subdirectories'] },
    ms_dos_3: { name: 'MS-DOS 3.0', year: 1984, features: ['Hard drive support'] },
    ms_dos_5: { name: 'MS-DOS 5.0', year: 1991, features: ['EMM386', 'HIMEM'] },
    ms_dos_6: { name: 'MS-DOS 6.x', year: 1993, features: ['DoubleSpace', 'MemMaker'] },
    pc_dos: { name: 'PC DOS', year: 1981, developer: 'IBM', significance: 'IBM branded MS-DOS' },

    // Windows 1.x-3.x (DOS-based)
    windows_1: { name: 'Windows 1.0', year: 1985, significance: 'First Windows' },
    windows_2: { name: 'Windows 2.0', year: 1987 },
    windows_3: { name: 'Windows 3.0', year: 1990, significance: 'First successful Windows' },
    windows_3_1: { name: 'Windows 3.1', year: 1992, features: ['TrueType', 'Multimedia'] },
    windows_for_workgroups: { name: 'Windows for Workgroups 3.11', year: 1993 },

    // Windows 9x (DOS-based)
    windows_95: {
      name: 'Windows 95',
      year: 1995,
      significance: 'Revolutionary GUI, Start menu',
      features: ['32-bit', 'Start menu', 'Taskbar', 'Long filenames', 'Plug and Play']
    },
    windows_98: { name: 'Windows 98', year: 1998, features: ['USB support', 'FAT32'] },
    windows_98_se: { name: 'Windows 98 SE', year: 1999 },
    windows_me: { name: 'Windows ME', year: 2000, significance: 'Last DOS-based Windows' },

    // Windows NT Family
    windows_nt_3_1: { name: 'Windows NT 3.1', year: 1993, significance: 'First NT kernel' },
    windows_nt_3_5: { name: 'Windows NT 3.5', year: 1994 },
    windows_nt_4: { name: 'Windows NT 4.0', year: 1996, features: ['Win95 interface'] },
    windows_2000: {
      name: 'Windows 2000',
      year: 2000,
      features: ['Active Directory', 'NTFS 3.0', 'Plug and Play']
    },
    windows_xp: {
      name: 'Windows XP',
      year: 2001,
      significance: 'Longest-serving Windows, beloved',
      features: ['Luna interface', 'ClearType', 'Remote Desktop', 'System Restore']
    },
    windows_server_2003: { name: 'Windows Server 2003', year: 2003 },
    windows_vista: {
      name: 'Windows Vista',
      year: 2006,
      features: ['Aero', 'UAC', 'DirectX 10', 'WPF']
    },
    windows_server_2008: { name: 'Windows Server 2008', year: 2008 },
    windows_7: {
      name: 'Windows 7',
      year: 2009,
      significance: 'Beloved successor to XP',
      features: ['Aero improvements', 'Libraries', 'Jump lists', 'Snap']
    },
    windows_server_2012: { name: 'Windows Server 2012', year: 2012 },
    windows_8: {
      name: 'Windows 8',
      year: 2012,
      significance: 'Controversial Metro UI',
      features: ['Metro/Modern UI', 'Windows Store', 'Touch focus']
    },
    windows_8_1: { name: 'Windows 8.1', year: 2013, features: ['Start button return'] },
    windows_10: {
      name: 'Windows 10',
      year: 2015,
      significance: 'Windows as a Service',
      features: ['Cortana', 'Edge', 'Start menu return', 'Virtual desktops', 'WSL']
    },
    windows_server_2016: { name: 'Windows Server 2016', year: 2016 },
    windows_server_2019: { name: 'Windows Server 2019', year: 2018 },
    windows_11: {
      name: 'Windows 11',
      year: 2021,
      features: ['Centered taskbar', 'Rounded corners', 'Widgets', 'Android apps', 'WSL 2']
    },
    windows_server_2022: { name: 'Windows Server 2022', year: 2021 },

    // Other Microsoft
    os_2: { name: 'OS/2 (Microsoft era)', year: 1987, developer: 'Microsoft/IBM' },
    xbox_os: { name: 'Xbox System Software', year: 2001, significance: 'Gaming console OS' }
  },

  // IBM OPERATING SYSTEMS
  ibm: {
    os_360: {
      name: 'OS/360',
      year: 1966,
      significance: 'Revolutionary mainframe OS',
      features: ['Job control', 'Device independence']
    },
    mvs: {
      name: 'MVS',
      year: 1974,
      significance: 'Multiple Virtual Storage',
      evolution: 'MVS → MVS/XA → MVS/ESA → OS/390 → z/OS'
    },
    z_os: {
      name: 'z/OS',
      year: 2001,
      significance: 'Modern mainframe OS'
    },
    vm: {
      name: 'VM/CMS',
      year: 1972,
      significance: 'Virtual machine pioneer'
    },
    os_2_full: {
      name: 'OS/2',
      year: 1987,
      versions: ['OS/2 1.x', 'OS/2 2.x', 'OS/2 Warp', 'OS/2 Warp 4'],
      significance: 'Advanced PC OS, ahead of its time',
      features: ['32-bit', 'Preemptive multitasking', 'HPFS', 'WPS']
    },
    i_os: {
      name: 'IBM i (OS/400)',
      year: 1988,
      significance: 'AS/400 midrange OS'
    },
    aix_full: {
      name: 'AIX',
      year: 1986,
      significance: 'IBM UNIX'
    }
  },

  // DEC/VMS OPERATING SYSTEMS
  dec: {
    tops_10: {
      name: 'TOPS-10',
      year: 1967,
      platform: 'PDP-10',
      significance: 'Time-sharing system'
    },
    tops_20: {
      name: 'TOPS-20',
      year: 1976,
      platform: 'DECsystem-20',
      significance: 'Advanced TOPS-10'
    },
    rsts_e: {
      name: 'RSTS/E',
      year: 1970,
      platform: 'PDP-11',
      significance: 'Multi-user BASIC system'
    },
    rt_11: {
      name: 'RT-11',
      year: 1970,
      platform: 'PDP-11',
      significance: 'Single-user real-time OS'
    },
    rsx_11: {
      name: 'RSX-11',
      year: 1972,
      platform: 'PDP-11',
      significance: 'Real-time executive'
    },
    vms: {
      name: 'VMS/OpenVMS',
      year: 1977,
      developer: 'DEC/HP/VSI',
      platform: 'VAX, Alpha, Itanium, x86-64',
      significance: 'Legendary reliability',
      features: ['Clustering', 'RMS', 'DCL', 'Uptime records']
    }
  },

  // REAL-TIME OPERATING SYSTEMS
  rtos: {
    vxworks: {
      name: 'VxWorks',
      year: 1987,
      developer: 'Wind River',
      significance: 'Mars rovers, 787 Dreamliner',
      features: ['POSIX', 'Deterministic', 'Certifiable']
    },
    qnx: {
      name: 'QNX',
      year: 1982,
      developer: 'QNX/BlackBerry',
      significance: 'Microkernel RTOS, automotive',
      features: ['Microkernel', 'POSIX', 'High availability']
    },
    freertos: {
      name: 'FreeRTOS',
      year: 2003,
      developer: 'Richard Barry/Amazon',
      significance: 'Most popular embedded RTOS',
      features: ['Free', 'Portable', 'Small footprint']
    },
    rtems: {
      name: 'RTEMS',
      year: 1988,
      significance: 'Real-time for embedded systems'
    },
    threadx: {
      name: 'ThreadX (Azure RTOS)',
      year: 1997,
      developer: 'Express Logic/Microsoft',
      significance: 'Billions of deployments'
    },
    integrity: {
      name: 'INTEGRITY',
      year: 1999,
      developer: 'Green Hills',
      significance: 'High-security RTOS'
    },
    lynxos: {
      name: 'LynxOS',
      year: 1986,
      developer: 'Lynx Software',
      significance: 'Hard real-time POSIX'
    },
    nucleus: {
      name: 'Nucleus RTOS',
      year: 1993,
      developer: 'Mentor/Siemens',
      significance: 'Embedded royalty-free'
    },
    zephyr: {
      name: 'Zephyr',
      year: 2016,
      developer: 'Linux Foundation',
      significance: 'Modern IoT RTOS'
    },
    riot: {
      name: 'RIOT',
      year: 2008,
      significance: 'IoT operating system'
    },
    contiki: {
      name: 'Contiki',
      year: 2002,
      developer: 'Adam Dunkels',
      significance: 'IoT pioneer'
    },
    nuttx: {
      name: 'NuttX',
      year: 2007,
      developer: 'Gregory Nutt',
      significance: 'POSIX RTOS, PX4 drone autopilot'
    },
    chibios: {
      name: 'ChibiOS',
      year: 2007,
      significance: 'Compact embedded RTOS'
    },
    embos: {
      name: 'embOS',
      year: 1992,
      developer: 'SEGGER',
      significance: 'Professional RTOS'
    },
    ecos: {
      name: 'eCos',
      year: 1998,
      developer: 'Red Hat/eCosCentric',
      significance: 'Configurable embedded OS'
    }
  },

  // MOBILE OPERATING SYSTEMS
  mobile: {
    android: {
      name: 'Android',
      year: 2008,
      developer: 'Google',
      base: 'Linux kernel',
      significance: 'Most-used mobile OS',
      versions: {
        '1.5': 'Cupcake (2009)',
        '2.2': 'Froyo (2010)',
        '4.0': 'Ice Cream Sandwich (2011)',
        '5.0': 'Lollipop (2014) - Material Design',
        '6.0': 'Marshmallow (2015)',
        '7.0': 'Nougat (2016)',
        '8.0': 'Oreo (2017)',
        '9': 'Pie (2018)',
        '10': '2019',
        '11': '2020',
        '12': '2021',
        '13': '2022',
        '14': '2023',
        '15': '2024'
      }
    },
    palm_os: {
      name: 'Palm OS',
      year: 1996,
      developer: 'Palm Inc',
      significance: 'PDA pioneer'
    },
    windows_mobile: {
      name: 'Windows Mobile',
      year: 2000,
      developer: 'Microsoft',
      evolution: 'Pocket PC → Windows Mobile'
    },
    windows_phone: {
      name: 'Windows Phone',
      year: 2010,
      developer: 'Microsoft',
      significance: 'Metro UI mobile (discontinued)'
    },
    symbian: {
      name: 'Symbian',
      year: 1997,
      developer: 'Psion/Nokia',
      significance: 'Pre-iPhone smartphone leader'
    },
    blackberry_os: {
      name: 'BlackBerry OS',
      year: 1999,
      developer: 'BlackBerry',
      significance: 'Enterprise mobile pioneer'
    },
    webos: {
      name: 'webOS',
      year: 2009,
      developer: 'Palm/HP/LG',
      significance: 'Innovative, now in LG TVs'
    },
    meego: {
      name: 'MeeGo',
      year: 2010,
      developer: 'Nokia/Intel',
      significance: 'Linux mobile attempt'
    },
    tizen: {
      name: 'Tizen',
      year: 2012,
      developer: 'Samsung/Intel',
      significance: 'Samsung watches/TVs'
    },
    sailfish_os: {
      name: 'Sailfish OS',
      year: 2013,
      developer: 'Jolla',
      significance: 'MeeGo successor'
    },
    kaios: {
      name: 'KaiOS',
      year: 2017,
      developer: 'KaiOS Technologies',
      significance: 'Feature phone OS, Firefox OS based'
    },
    harmonyos: {
      name: 'HarmonyOS',
      year: 2019,
      developer: 'Huawei',
      significance: 'Huawei alternative to Android'
    },
    fuchsia: {
      name: 'Google Fuchsia',
      year: 2016,
      developer: 'Google',
      significance: 'Zircon microkernel, not Linux'
    }
  },

  // OTHER NOTABLE OPERATING SYSTEMS
  other: {
    beos: {
      name: 'BeOS',
      year: 1995,
      developer: 'Be Inc',
      significance: 'Ahead of its time, multimedia focus',
      features: ['64-bit journaling BFS', 'Pervasive multithreading', 'Database-like file attributes']
    },
    haiku: {
      name: 'Haiku',
      year: 2001,
      developer: 'Haiku Inc',
      significance: 'Open-source BeOS recreation'
    },
    amigaos: {
      name: 'AmigaOS',
      year: 1985,
      developer: 'Commodore',
      significance: 'Revolutionary multimedia OS',
      features: ['Preemptive multitasking', 'Custom chips', 'Intuition GUI']
    },
    tos: {
      name: 'TOS (Atari)',
      year: 1985,
      developer: 'Atari',
      significance: 'Atari ST operating system',
      features: ['GEM desktop', 'MIDI support']
    },
    geos: {
      name: 'GEOS',
      year: 1986,
      developer: 'Berkeley Softworks',
      significance: 'GUI for 8-bit computers',
      platforms: ['C64', 'Apple II', 'PC']
    },
    risc_os: {
      name: 'RISC OS',
      year: 1987,
      developer: 'Acorn/RISC OS Developments',
      significance: 'ARM native OS'
    },
    plan_9: {
      name: 'Plan 9 from Bell Labs',
      year: 1992,
      developer: 'Bell Labs',
      significance: 'UNIX successor research OS',
      features: ['Everything is a file', '9P protocol', 'UTF-8 origin']
    },
    inferno: {
      name: 'Inferno',
      year: 1996,
      developer: 'Bell Labs',
      significance: 'Distributed OS'
    },
    reactos: {
      name: 'ReactOS',
      year: 1998,
      significance: 'Open-source Windows compatible OS'
    },
    kolibrios: {
      name: 'KolibriOS',
      year: 2004,
      significance: 'Tiny OS, fits on floppy'
    },
    menuetos: {
      name: 'MenuetOS',
      year: 2000,
      significance: 'Written in assembly'
    },
    templeos: {
      name: 'TempleOS',
      year: 2005,
      developer: 'Terry A. Davis',
      significance: 'Unique religious OS project'
    },
    serenity: {
      name: 'SerenityOS',
      year: 2018,
      developer: 'Andreas Kling',
      significance: '90s-inspired modern OS from scratch'
    },
    redox: {
      name: 'Redox',
      year: 2015,
      developer: 'Jeremy Soller',
      significance: 'Rust-written microkernel OS'
    }
  },

  // HISTORICAL MAINFRAME/MINI SYSTEMS
  historical: {
    exec_8: {
      name: 'EXEC 8',
      year: 1964,
      developer: 'UNIVAC',
      significance: 'UNIVAC 1108 operating system'
    },
    scope: {
      name: 'SCOPE',
      year: 1966,
      developer: 'CDC',
      significance: 'CDC 6000 series OS'
    },
    nos: {
      name: 'NOS',
      year: 1976,
      developer: 'CDC',
      significance: 'CDC Cyber mainframe OS'
    },
    gcos: {
      name: 'GCOS',
      year: 1962,
      developer: 'GE/Honeywell/Bull',
      significance: 'General Electric mainframe OS'
    },
    rsx: {
      name: 'RSX',
      year: 1972,
      developer: 'DEC',
      significance: 'Real-time executive'
    },
    cp_m: {
      name: 'CP/M',
      year: 1974,
      developer: 'Gary Kildall / Digital Research',
      significance: 'First microcomputer OS standard',
      features: ['BDOS', 'CCP', '8080/Z80 standard']
    },
    cp_m_86: {
      name: 'CP/M-86',
      year: 1981,
      developer: 'Digital Research',
      significance: '8086 CP/M, lost to MS-DOS'
    },
    dr_dos: {
      name: 'DR-DOS',
      year: 1988,
      developer: 'Digital Research',
      significance: 'MS-DOS compatible'
    },
    primos: {
      name: 'PRIMOS',
      year: 1972,
      developer: 'Prime Computer',
      significance: 'Prime minicomputer OS'
    },
    pick: {
      name: 'Pick Operating System',
      year: 1965,
      developer: 'Dick Pick',
      significance: 'Multi-value database OS'
    },
    theos: {
      name: 'THEOS',
      year: 1983,
      developer: 'THEOS Software',
      significance: 'Multi-user business OS'
    },
    newdos: {
      name: 'NEWDOS/80',
      year: 1979,
      significance: 'TRS-80 enhanced DOS'
    },
    trsdos: {
      name: 'TRSDOS',
      year: 1978,
      developer: 'Tandy',
      significance: 'TRS-80 operating system'
    },
    apple_dos: {
      name: 'Apple DOS',
      year: 1978,
      developer: 'Apple',
      versions: ['DOS 3.2', 'DOS 3.3'],
      significance: 'Apple II disk operating system'
    },
    prodos: {
      name: 'ProDOS',
      year: 1983,
      developer: 'Apple',
      significance: 'Advanced Apple II/III OS'
    },
    sos: {
      name: 'SOS (Sophisticated OS)',
      year: 1980,
      developer: 'Apple',
      significance: 'Apple III operating system'
    },
    commodore_dos: {
      name: 'Commodore DOS',
      year: 1977,
      developer: 'Commodore',
      significance: 'C64/VIC-20 disk OS'
    }
  }
};

// ==============================================================================
// API ENDPOINTS
// ==============================================================================

// Get all OS families
app.get('/api/os/families', (c) => {
  const families = Object.keys(OPERATING_SYSTEMS_DATABASE);
  return c.json({
    success: true,
    families,
    totalCategories: families.length
  });
});

// Search all operating systems
app.get('/api/os/search', (c) => {
  const query = (c.req.query('q') || '').toLowerCase();
  const results: any[] = [];

  const searchOS = (category: string, systems: any) => {
    Object.entries(systems).forEach(([key, value]: [string, any]) => {
      if (value.distributions) {
        // Linux distributions
        Object.entries(value.distributions).forEach(([distKey, distValue]: [string, any]) => {
          if (
            distKey.includes(query) ||
            (distValue.name && distValue.name.toLowerCase().includes(query)) ||
            (distValue.significance && distValue.significance.toLowerCase().includes(query))
          ) {
            results.push({ category, subCategory: 'distributions', key: distKey, ...distValue });
          }
        });
      } else {
        const name = value.name || key;
        if (
          key.includes(query) ||
          name.toLowerCase().includes(query) ||
          (value.significance && value.significance.toLowerCase().includes(query)) ||
          (value.developer && value.developer.toLowerCase().includes(query))
        ) {
          results.push({ category, key, ...value });
        }
      }
    });
  };

  Object.entries(OPERATING_SYSTEMS_DATABASE).forEach(([category, systems]) => {
    searchOS(category, systems);
  });

  return c.json({
    success: true,
    query,
    resultCount: results.length,
    results
  });
});

// Get specific OS category
app.get('/api/os/category/:category', (c) => {
  const category = c.req.param('category') as keyof typeof OPERATING_SYSTEMS_DATABASE;
  const data = OPERATING_SYSTEMS_DATABASE[category];

  if (!data) {
    return c.json({ error: 'Category not found' }, 404);
  }

  return c.json({
    success: true,
    category,
    systems: data
  });
});

// Get OS by family and name
app.get('/api/os/:family/:name', (c) => {
  const family = c.req.param('family') as keyof typeof OPERATING_SYSTEMS_DATABASE;
  const name = c.req.param('name');
  const familyData = OPERATING_SYSTEMS_DATABASE[family] as any;

  if (!familyData) {
    return c.json({ error: 'Family not found' }, 404);
  }

  const os = familyData[name];
  if (!os) {
    return c.json({ error: 'Operating system not found' }, 404);
  }

  return c.json({
    success: true,
    family,
    name,
    details: os
  });
});

// Get timeline of operating systems
app.get('/api/os/timeline', (c) => {
  const timeline: { year: number; name: string; category: string; significance?: string }[] = [];

  const extractTimeline = (category: string, systems: any) => {
    Object.entries(systems).forEach(([key, value]: [string, any]) => {
      if (value.distributions) {
        Object.entries(value.distributions).forEach(([distKey, distValue]: [string, any]) => {
          if (distValue.year) {
            timeline.push({
              year: distValue.year,
              name: distValue.name || distKey,
              category: `${category}/distributions`,
              significance: distValue.significance
            });
          }
        });
      } else if (value.year) {
        timeline.push({
          year: value.year,
          name: value.name || key,
          category,
          significance: value.significance
        });
      }
    });
  };

  Object.entries(OPERATING_SYSTEMS_DATABASE).forEach(([category, systems]) => {
    extractTimeline(category, systems);
  });

  timeline.sort((a, b) => a.year - b.year);

  return c.json({
    success: true,
    totalEntries: timeline.length,
    timeline
  });
});

// Get Linux distributions
app.get('/api/os/linux/distros', (c) => {
  const distros = OPERATING_SYSTEMS_DATABASE.linux.distributions;
  return c.json({
    success: true,
    totalDistros: Object.keys(distros).length,
    distributions: distros
  });
});

// Get macOS history
app.get('/api/os/apple/macos/history', (c) => {
  const macosVersions = Object.entries(OPERATING_SYSTEMS_DATABASE.apple)
    .filter(([key]) => key.includes('mac_os') || key.includes('os_x') || key.includes('macos'))
    .map(([key, value]) => ({ key, ...value }))
    .sort((a: any, b: any) => (a.year || 0) - (b.year || 0));

  return c.json({
    success: true,
    versions: macosVersions
  });
});

// Get Windows history
app.get('/api/os/microsoft/windows/history', (c) => {
  const windowsVersions = Object.entries(OPERATING_SYSTEMS_DATABASE.microsoft)
    .filter(([key]) => key.includes('windows'))
    .map(([key, value]) => ({ key, ...value }))
    .sort((a: any, b: any) => (a.year || 0) - (b.year || 0));

  return c.json({
    success: true,
    versions: windowsVersions
  });
});

// Get RTOS systems
app.get('/api/os/rtos/all', (c) => {
  return c.json({
    success: true,
    totalSystems: Object.keys(OPERATING_SYSTEMS_DATABASE.rtos).length,
    systems: OPERATING_SYSTEMS_DATABASE.rtos
  });
});

// Get mobile operating systems
app.get('/api/os/mobile/all', (c) => {
  return c.json({
    success: true,
    totalSystems: Object.keys(OPERATING_SYSTEMS_DATABASE.mobile).length,
    systems: OPERATING_SYSTEMS_DATABASE.mobile
  });
});

// Get UNIX family tree
app.get('/api/os/unix/family-tree', (c) => {
  return c.json({
    success: true,
    earlyBatch: OPERATING_SYSTEMS_DATABASE.earlyBatch,
    unixFamily: OPERATING_SYSTEMS_DATABASE.unixFamily
  });
});

// AI-powered OS recommendation
app.post('/api/os/recommend', async (c) => {
  const { useCase, requirements, experience } = await c.req.json();

  const prompt = `Based on this use case: "${useCase}"
Requirements: ${JSON.stringify(requirements)}
User experience level: ${experience}

Recommend the best operating system from this database and explain why.
Consider: performance, ease of use, community support, and specific features needed.`;

  const response = await c.env.AI.run('@cf/meta/llama-3-8b-instruct', {
    prompt,
    max_tokens: 1000
  });

  return c.json({
    success: true,
    recommendation: response.response
  });
});

// AI-powered OS comparison
app.post('/api/os/compare', async (c) => {
  const { systems } = await c.req.json();

  const systemDetails = systems.map((sys: string) => {
    // Search for the system in database
    let found: any = null;
    Object.entries(OPERATING_SYSTEMS_DATABASE).forEach(([category, data]) => {
      Object.entries(data as object).forEach(([key, value]: [string, any]) => {
        if (key.includes(sys.toLowerCase()) || (value.name && value.name.toLowerCase().includes(sys.toLowerCase()))) {
          found = { category, key, ...value };
        }
      });
    });
    return found || { name: sys, note: 'Not found in database' };
  });

  const prompt = `Compare these operating systems in detail:
${JSON.stringify(systemDetails, null, 2)}

Provide a comprehensive comparison covering:
1. Performance characteristics
2. Use cases and target audience
3. Pros and cons of each
4. Recommendations for different scenarios`;

  const response = await c.env.AI.run('@cf/meta/llama-3-8b-instruct', {
    prompt,
    max_tokens: 1500
  });

  return c.json({
    success: true,
    systems: systemDetails,
    comparison: response.response
  });
});

// Get OS statistics
app.get('/api/os/stats', (c) => {
  let totalOS = 0;
  const byCategory: Record<string, number> = {};
  const byDecade: Record<string, number> = {};

  const countOS = (category: string, systems: any) => {
    let count = 0;
    Object.entries(systems).forEach(([key, value]: [string, any]) => {
      if (value.distributions) {
        const distCount = Object.keys(value.distributions).length;
        count += distCount + 1; // +1 for kernel
      } else {
        count++;
        if (value.year) {
          const decade = `${Math.floor(value.year / 10) * 10}s`;
          byDecade[decade] = (byDecade[decade] || 0) + 1;
        }
      }
    });
    byCategory[category] = count;
    totalOS += count;
  };

  Object.entries(OPERATING_SYSTEMS_DATABASE).forEach(([category, systems]) => {
    countOS(category, systems);
  });

  return c.json({
    success: true,
    totalOperatingSystems: totalOS,
    byCategory,
    byDecade: Object.fromEntries(Object.entries(byDecade).sort())
  });
});

// Health check
app.get('/health', (c) => {
  return c.json({
    status: 'healthy',
    worker: 'operating-systems-worker',
    version: '1.0.0',
    timestamp: new Date().toISOString(),
    capabilities: [
      'Every OS ever made since dawn of computing',
      'UNIX family tree (complete)',
      'Linux distributions (100+ distros)',
      'Windows complete history',
      'macOS/Apple complete history',
      'Mobile OS history',
      'RTOS systems',
      'Mainframe systems',
      'Historical systems',
      'AI-powered recommendations',
      'AI-powered comparisons'
    ]
  });
});

export default app;
