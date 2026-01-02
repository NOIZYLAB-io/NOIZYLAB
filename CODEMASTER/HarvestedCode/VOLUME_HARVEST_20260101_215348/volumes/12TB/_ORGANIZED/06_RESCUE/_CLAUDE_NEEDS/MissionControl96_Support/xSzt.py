SITES = {
  "Studio": {"ids": ["DL-001","DL-002"]},
  "Home": {"ids": []},
  "Remote": {"ids": []},
}

def devices_for(site_name, all_devices):
    ids = set(SITES.get(site_name, {}).get("ids", []))
    return [d for d in all_devices if d.id in ids]
