import sys
import os


# STEP 1: command line args read karo


args = sys.argv

# expected:
# python t4_sys.py --file ./data/logs.jsonl --top 3

if "--file" in args:
    file_path = args[args.index("--file") + 1]
else:
    file_path = None

if "--top" in args:
    top_n = int(args[args.index("--top") + 1])
else:
    top_n = 3



# STEP 2: file check


if not file_path or not os.path.exists(file_path):
    print("ERROR: File not found", file_path, file=sys.stderr)
    sys.exit(2)   # exit code 2 = file missing



# STEP 3: read file + count log levels


log_counts = {}

with open(file_path, "r") as f:
    for line in f:
        line = line.strip() # strips whitespace/newline from ends

        # assume format: [LEVEL] message OR LEVEL,message etc.
        if not line:
            continue

        # simple extraction (example format handling)
        if "ERROR" in line:
            level = "ERROR"
        elif "INFO" in line:
            level = "INFO"
        elif "WARNING" in line:
            level = "WARNING"
        else:
            level = "OTHER"

        log_counts[level] = log_counts.get(level, 0) + 1



# STEP 4: sort levels by count


sorted_levels = sorted(log_counts.items(), key=lambda x: x[1], reverse=True)



# STEP 5: print top N levels


print("\nTop log levels:")

for level, count in sorted_levels[:top_n]:
    print(level, ":", count)



# STEP 6: errors stderr par


if "ERROR" in log_counts:
    print("ERROR logs found:", log_counts["ERROR"], file=sys.stderr)



# STEP 7: success exit code


sys.exit(0) #program successfully completed