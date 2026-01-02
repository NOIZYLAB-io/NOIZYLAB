import yaml

def log_pages_to_yaml(pages, filename='fb_pages_log.yaml'):
    data = [{'name': p.get('name'), 'id': p.get('id'), 'category': p.get('category')} for p in pages]
    with open(filename, 'w') as f:
        yaml.dump(data, f)
