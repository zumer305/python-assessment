import json
from datetime import datetime, timedelta

def process_logs(file_path):
    logs = []

    # STEP 1: read + parse timestamps
    with open(file_path, "r") as f:
        for line in f:
            line = line.strip()

            if not line:
                continue

            try:
                data = json.loads(line)

                # assume key = "timestamp"
                ts = data.get("timestamp")

                if ts:
                    dt = datetime.fromisoformat(ts)  # ISO → datetime
                    logs.append((dt, data))

            except Exception:
                continue

    # STEP 2: last 24 hours filter
    now = datetime.now()
    last_24 = now - timedelta(hours=24)

    recent_logs = [log for log in logs if log[0] >= last_24]

    # STEP 3: sort by time
    recent_logs.sort(key=lambda x: x[0])

    # STEP 4: print logs
    print("\nLogs in last 24 hours:\n")
    for dt, log in recent_logs:
        print(dt, "->", log)

    # STEP 5: difference in minutes
    if len(recent_logs) >= 2:
        first = recent_logs[0][0]
        last = recent_logs[-1][0] # -1 last element

        diff = (last - first).total_seconds() / 60
        print(f"\nTime difference: {diff:.2f} minutes")
    else:
        print("\nNot enough logs for time difference")


# RUN
if __name__ == "__main__":
    process_logs("data/logs.jsonl")

#Tum pehle:
#last 24 hours ke logs filter karte ho
#phir unhein sort karte ho (time ke hisaab se)