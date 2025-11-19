from collections import Counter
import os

LOG_FILE = "logs/keystrokes.txt"

def analyze():
    if not os.path.exists(LOG_FILE):
        print("No log file found! Run the keylogger first.")
        return
    
    with open(LOG_FILE, "r") as log:
        data = log.read()

    count = Counter(data)
    sorted_keys = count.most_common(10)

    print("\n🔍 Top 10 most used keys:")
    for key, freq in sorted_keys:
        key_display = key.replace("\n", "[ENTER]").replace(" ", "[SPACE]")
        print(f"  {key_display} → {freq} times")

if __name__ == "__main__":
    analyze()
