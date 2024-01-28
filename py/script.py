import json
from packaging import version

def get_dependencies_stats(requirements_file='requirements.txt'):
    with open(requirements_file, 'r') as file:
        dependencies = [line.strip() for line in file.readlines()]

    dependencies_stats = []

    for dependency in dependencies:
        name, version_str = dependency.split('==')
        dependencies_stats.append({
            'name': name,
            'version': version.parse(version_str)
        })

    return dependencies_stats

def save_to_json(data, filename='dependencies_stats.json'):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)

if __name__ == "__main__":
    stats = get_dependencies_stats()
    save_to_json(stats)
