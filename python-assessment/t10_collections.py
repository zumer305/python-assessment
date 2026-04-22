import json
from collections import Counter, defaultdict, namedtuple

# STEP 1: namedtuple define
Log = namedtuple("Log", ["user", "event"])

events_list = []
user_groups = defaultdict(list)

# STEP 2: read JSONL file
with open("data/logs.jsonl", "r") as f:
    for line in f:
        line = line.strip()

        if not line:
            continue

        try:
            data = json.loads(line)

            user = data.get("user", "unknown")
            event = data.get("level", "OTHER")

            # namedtuple create
            log_entry = Log(user, event)

            events_list.append(event)
            user_groups[user].append(event)

        except json.JSONDecodeError:
            continue

# STEP 3: Counter (most common events)
counter = Counter(events_list)

print("\nTop 2 Events:")
for event, count in counter.most_common(2):
    print(event, ":", count)

# STEP 4: grouped by user
print("\nEvents by User:")
for user, events in user_groups.items():
    print(user, "->", events)