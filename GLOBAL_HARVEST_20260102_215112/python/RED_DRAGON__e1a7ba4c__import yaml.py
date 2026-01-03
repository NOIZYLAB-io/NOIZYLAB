import yaml

def log_pages_to_yaml(pages, filename='fb_pages_log.yaml'):
    data = [{'name': p.get('name'), 'id': p.get('id'), 'category': p.get('category')} for p in pages]
    with open(filename, 'w') as f:
        yaml.dump(data, f)

if __name__ == "__main__":
    import sys
    pages = [{'name': 'Page1', 'id': '1', 'category': 'Category1'}, {'name': 'Page2', 'id': '2', 'category': 'Category2'}]  # Example data
    log_pages_to_yaml(pages, sys.argv[1] if len(sys.argv) > 1 else 'fb_pages_log.yaml')