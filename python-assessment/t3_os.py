import os

# 🔹 Step 1: environment variable read karo
# agar LOG_DIR nahi mila to default ./data use karo
log_dir = os.getenv("LOG_DIR", "./data") #"/home/user/logs"


# 🔹 Step 2: directory create karo agar exist nahi karti
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
    print("Directory created:", log_dir)
else:
    print("Directory already exists:", log_dir)


# 🔹 Step 3: logs.jsonl ka safe path banao
log_file_path = os.path.join(log_dir, "logs.jsonl")
print("Log file path:", log_file_path)


# 🔹 Step 4: .jsonl aur .log files list karo
print("\nLog files found:")

for file in os.listdir(log_dir):
    if file.endswith(".jsonl") or file.endswith(".log"):
        print(file)