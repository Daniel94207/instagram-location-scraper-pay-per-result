thonimport json

def export_to_json(data, filename='output.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)