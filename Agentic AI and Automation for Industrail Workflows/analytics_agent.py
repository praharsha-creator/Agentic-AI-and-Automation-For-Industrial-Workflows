import csv
import os

LOG_FILE = "daily_agent_log.csv"

def generate_visual_report():
    if not os.path.isfile(LOG_FILE):
        print("[Analytics Agent] No log file found.")
        return

    total_records = 0
    maintenance_count = 0
    risky_count = 0

    with open(LOG_FILE, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            total_records += 1
            if "MAINTENANCE" in row[-1]:
                maintenance_count+= 1
            if "RISKY" in row:
                risky_count += 1

    print("\n[Analytics Agent] Summary Report")
    print("Total Records:", total_records)
    print("Risky Machine Count:", risky_count)
    print("Maintenance Decisions:", maintenance_count) 