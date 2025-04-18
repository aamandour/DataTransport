import json

with open("2025-04-14_2901.json") as f1, open("2025-04-14_2904.json") as f2:
    data1 = json.load(f1)
    data2 = json.load(f2)

combined = data1 + data2

with open("bcsample.json", "w") as fout:
    json.dump(combined, fout, indent=2)

print(f"✅ Merged {len(combined)} total records into bcsample.json")
