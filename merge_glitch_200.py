import os
import json

data_path = "glitch_200"
merged = []

for filename in os.listdir(data_path):
    if filename.endswith(".json"):
        filepath = os.path.join(data_path, filename)
        with open(filepath, 'r') as f:
            try:
                data = json.load(f)
                merged.extend(data)
            except json.JSONDecodeError:
                print(f"⚠️ Skipping invalid file: {filename}")

with open("bcsample_glitch_200.json", "w") as fout:
    json.dump(merged, fout, indent=2)

print(f"✅ Merged {len(merged)} total breadcrumb records into bcsample_glitch_200.json")
