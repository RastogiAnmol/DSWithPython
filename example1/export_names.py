import os
import json

root = "documents"  # current directory

data = []

for dirpath, dirnames, filenames in os.walk(root):
    rel_path = os.path.relpath(dirpath, root)

    entry = {
        "folder": rel_path,
        "subfolders": dirnames,
        "files": filenames
    }

    data.append(entry)

with open("kindle_structure.json", "w") as f:
    json.dump(data, f, indent=2)

print("Saved to kindle_structure.json")
