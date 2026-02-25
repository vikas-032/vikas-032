from datetime import datetime

# Write current timestamp to a file
with open("daily_commit.txt", "w") as f:
    f.write(f"Last commit: {datetime.now()}\n")
