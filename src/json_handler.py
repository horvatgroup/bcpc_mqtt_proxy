import json

def read_json(filename):
    with open(filename) as f:
        d = json.load(f)
        return d

def write_json(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    pass
