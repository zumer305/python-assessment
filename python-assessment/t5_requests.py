import requests
import json


# POST REQUEST FUNCTION

def post_summary(url, payload):
    headers = {
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(
            url,
            json=payload,
            headers=headers,
            timeout=5
        )

        try:
            return response.status_code, response.json()
        except ValueError:
            return response.status_code, None

    except requests.exceptions.Timeout:
        print("Request timed out")
        return None, None

    except requests.exceptions.ConnectionError:
        print("Connection error")
        return None, None



# LOG FILE SUMMARY FUNCTION

def summarize_levels(file_path):
    log_counts = {
        "ERROR": 0,
        "INFO": 0,
        "WARNING": 0,
        "OTHER": 0
    }

    try:
        with open(file_path, "r") as f:
            for line in f:
                line = line.strip()

                if not line:
                    continue

                try:
                    data = json.loads(line)
                    level = data.get("level", "OTHER")
                except json.JSONDecodeError:
                    level = "OTHER"

                log_counts[level] = log_counts.get(level, 0) + 1

        return log_counts

    except FileNotFoundError:
        print("File not found")
        return None
    





if __name__ == "__main__":
    
    # file ka summary nikaalo
    result = summarize_levels("data/logs.jsonl")
    print("Log Summary:", result)

    # API call test (example URL)
    url = "https://jsonplaceholder.typicode.com/posts"
    status, response = post_summary(url, result)

    print("Status Code:", status)
    print("Response:", response)