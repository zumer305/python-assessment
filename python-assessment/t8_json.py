import json

input_file = "data/logs.jsonl"
output_file = "pretty_logs.json"

data_list = []

# STEP 1: read JSONL file
with open(input_file, "r") as f:
    for line in f:
        line = line.strip()

        if not line:
            continue

        try:
            obj = json.loads(line)   # JSON → Python dict
            data_list.append(obj)

        except json.JSONDecodeError:
            print("Invalid JSON skipped:", line)

# STEP 2: write to new file (pretty format)
with open(output_file, "w") as f:
    json.dump(data_list, f, indent=4)

print("Done! Pretty JSON saved in", output_file)