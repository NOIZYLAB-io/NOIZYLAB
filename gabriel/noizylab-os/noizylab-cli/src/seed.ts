export type SeedPlaybook = {
  code: string;
  name: string;
  persona?: string;
  tags?: string[];
  steps: { os: "win" | "mac" | "both"; order: number; title: string; detail?: string }[];
};

export const PLAYBOOKS_SEED: SeedPlaybook[] = [
  {
    code: "PB1",
    name: "Browser Diet",
    persona: "P1 Tab Tornado",
    tags: ["PERF-TABS", "PERF-LOWRAM", "SEC-BROWSERHIJACK"],
    steps: [
      { os: "both", order: 1, title: "Count the damage", detail: "How many tabs + which browser + extensions list." },
      { os: "win",  order: 2, title: "Kill heavy startup", detail: "Task Manager → Startup → disable non-essential." },
      { os: "mac",  order: 2, title: "Trim login items", detail: "System Settings → Login Items → remove junk." },
      { os: "both", order: 3, title: "Disable/Remove extensions", detail: "Keep only must-haves; remove unknowns." },
      { os: "both", order: 4, title: "Reset profile if corrupted", detail: "New profile; migrate bookmarks only." },
      { os: "both", order: 5, title: "Enable tab sleeping", detail: "Chrome/Edge: Memory Saver; Safari: close heavy sites." }
    ]
  },
  {
    code: "PB2",
    name: "Space Guard",
    persona: "P2 Storage Closet",
    tags: ["STOR-LOWDISK", "SYNC-DUPES", "USR-DOWNLOADSCHAOS"],
    steps: [
      { os: "both", order: 1, title: "Find top offenders", detail: "Largest folders/files first; don't guess." },
      { os: "win",  order: 2, title: "Storage Sense", detail: "Settings → System → Storage → run cleanup." },
      { os: "mac",  order: 2, title: "Storage Manager", detail: "System Settings → General → Storage." },
      { os: "both", order: 3, title: "Downloads quarantine", detail: "Move messy downloads to one folder; sort later." },
      { os: "both", order: 4, title: "Stop sync loops", detail: "Fix duplicate roots; choose source-of-truth folder." },
      { os: "both", order: 5, title: "Set alerts", detail: "Warn at 20/15/10% free." }
    ]
  },
  {
    code: "PB3",
    name: "No Snake Oil",
    persona: "P3 Click-Yes Optimizer",
    tags: ["SEC-PUP", "SEC-BROWSERHIJACK", "USR-CLICKYES"],
    steps: [
      { os: "win",  order: 1, title: "Uninstall PUPs", detail: "Apps → uninstall unknown cleaners/toolbars." },
      { os: "win",  order: 2, title: "Browser policy reset", detail: "Reset browser settings; remove managed policies if hijacked." },
      { os: "both", order: 3, title: "Extension purge", detail: "Remove unknown extensions; keep whitelist only." },
      { os: "both", order: 4, title: "Prevention switch", detail: "Approved installers only; block fake update sites." }
    ]
  },
  {
    code: "PB4",
    name: "Update Safe-Window",
    persona: "P4 Update Avoider",
    tags: ["UPD-OS", "UPD-APP", "USR-UPDATEAVOID"],
    steps: [
      { os: "both", order: 1, title: "Stabilize current state", detail: "Confirm what changed (update/install) + when." },
      { os: "both", order: 2, title: "Rollback/patch if needed", detail: "Target the offending update/driver." },
      { os: "both", order: 3, title: "Schedule update window", detail: "Pick a weekly safe slot; no random updates." },
      { os: "both", order: 4, title: "Pre-update safety", detail: "Snapshot/backup before major OS upgrades." }
    ]
  },
  {
    code: "PB5",
    name: "Password Cleanroom",
    persona: "P5 Password Spiral",
    tags: ["AUTH-MFA", "AUTH-PASSWORDRESET", "USR-PASSWORDCHAOS"],
    steps: [
      { os: "both", order: 1, title: "Account map", detail: "List Apple/Microsoft/Google + which email owns what." },
      { os: "both", order: 2, title: "MFA reset cleanly", detail: "Update trusted devices; store backup codes." },
      { os: "both", order: 3, title: "Recovery verified", detail: "Recovery email/phone verified; write it down." },
      { os: "both", order: 4, title: "Password manager", detail: "Set up; stop reuse; stop guesswork." }
    ]
  },
  {
    code: "PB6",
    name: "Wi-Fi Stabilizer",
    persona: "P6 Wi-Fi Whiplash",
    tags: ["NET-WIFIDROP", "NET-DNS", "NET-ROUTER"],
    steps: [
      { os: "both", order: 1, title: "Isolate fault", detail: "ISP vs router vs device: test wired if possible." },
      { os: "both", order: 2, title: "Firmware + reboot plan", detail: "Update router firmware; avoid daily power cycles." },
      { os: "both", order: 3, title: "Kill double-NAT", detail: "One router brain; mesh/extenders cleaned up." },
      { os: "both", order: 4, title: "DNS sanity", detail: "Set stable DNS; confirm no VPN conflict." }
    ]
  },
  {
    code: "PB7",
    name: "Peripheral Detox",
    persona: "P7 Peripheral Collector",
    tags: ["DRV-PRINTER", "DRV-USB", "DRV-AUDIO"],
    steps: [
      { os: "both", order: 1, title: "Remove ghosts", detail: "Delete old printers/devices; unplug/replug cleanly." },
      { os: "win",  order: 2, title: "Driver clean reinstall", detail: "Use known-good package; avoid random driver sites." },
      { os: "mac",  order: 2, title: "Reset device config", detail: "Remove + re-add; check permissions (mic/camera) if needed." },
      { os: "both", order: 3, title: "Cable/adapter sanity", detail: "Adapters stacked = bugs; simplify." }
    ]
  },
  {
    code: "PB8",
    name: "Cloud Sync Sanity",
    persona: "P8 Cloud Sync Tangle",
    tags: ["SYNC-DUPES", "FILE-PERMISSIONS", "SYNC-GDRIVE"],
    steps: [
      { os: "both", order: 1, title: "Pick source of truth", detail: "One root folder; everything else points to it." },
      { os: "both", order: 2, title: "Stop duplicate roots", detail: "No Desktop/Documents double-sync wars." },
      { os: "both", order: 3, title: "Re-link cleanly", detail: "Unlink/relink account; verify permissions." },
      { os: "both", order: 4, title: "Verify conflicts stopped", detail: "Watch for 24h; confirm no dupes." }
    ]
  },
  {
    code: "PB9",
    name: "Thermal Rescue",
    persona: "P9 Thermal Throttler",
    tags: ["PERF-THERMAL", "HW-DUSTFAN", "PERF-BACKGROUND"],
    steps: [
      { os: "both", order: 1, title: "Background load check", detail: "Find top CPU/Memory culprits." },
      { os: "both", order: 2, title: "Airflow + cleaning", detail: "Clear vents; clean dust; don't suffocate the machine." },
      { os: "both", order: 3, title: "Thermal prevention", detail: "Maintenance cadence 6–12 months." }
    ]
  },
  {
    code: "PB10",
    name: "Creative Workstation Tune",
    persona: "P10 Creative Chaos",
    tags: ["STOR-EXTERNALDRIVE", "PERF-BACKGROUND", "USR-NOBACKUP"],
    steps: [
      { os: "both", order: 1, title: "Scratch/cache placement", detail: "Move caches to fast drive; keep OS drive breathing." },
      { os: "both", order: 2, title: "Library/project layout", detail: "Standard project folder; no scattered media." },
      { os: "both", order: 3, title: "External drive health", detail: "Check errors; replace failing drives early." },
      { os: "both", order: 4, title: "Nightly incremental backup", detail: "Deadline-proof." }
    ]
  },
  {
    code: "PB11",
    name: "Hardware Truth Test",
    persona: "P12 Hardware Failing Quietly",
    tags: ["HW-SSD", "HW-RAM", "STOR-DISKERRORS"],
    steps: [
      { os: "both", order: 1, title: "Backup immediately", detail: "Before testing. Always." },
      { os: "both", order: 2, title: "Disk health check", detail: "SMART/errors; confirm capacity + wear." },
      { os: "both", order: 3, title: "Memory check", detail: "RAM test if crashes/freezes are random." },
      { os: "both", order: 4, title: "Migration plan", detail: "If failing: replace + restore + verify." }
    ]
  },
  {
    code: "PB12",
    name: "Backup Bulletproof",
    persona: "All",
    tags: ["USR-NOBACKUP"],
    steps: [
      { os: "both", order: 1, title: "Pick backup target", detail: "External SSD or NAS + cloud copy (simple version)." },
      { os: "both", order: 2, title: "Automate schedule", detail: "Daily incrementals; weekly full where possible." },
      { os: "both", order: 3, title: "Monthly restore test", detail: "If it can't restore, it's not a backup." }
    ]
  }
];
