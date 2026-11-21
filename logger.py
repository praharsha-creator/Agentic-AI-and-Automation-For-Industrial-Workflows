import csv
import os
from datetime import datetime

LOG_FILE = "daily_agent_log.csv"

def log_decision(day,
    temperature,
    vibration,
    usage_hours,
    machine_status,
    maintenance_decision,
    inventory_status,predictive_decision):

    print("LOGGER FUNCTION CALLED")

    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # Write header only once
        if not file_exists:
            writer.writerow(["Day",
                "timestamp",
                "temperature",
                "vibration",
                "usage_hours",
                "machine_status",
                "maintenance_decision",
                "inventory_status","PredictiveDecision"
            ])

        # Write data row
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            temperature,
            vibration,
            usage_hours,
            machine_status,
            maintenance_decision,
            inventory_status,predictive_decision
        ])
