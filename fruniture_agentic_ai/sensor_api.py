from fastapi import FastAPI
import random
from datetime import datetime

# Create FastAPI app (THIS LINE IS CRITICAL)
app = FastAPI()

@app.get("/api/machine-status")
def get_machine_status():
    return {
        "timestamp": datetime.now().isoformat(),
        "temperature": random.randint(60, 110),
        "vibration": round(random.uniform(0.3, 2.5), 2),
        "usage_hours": random.randint(1000, 3000),
        "machine_status": random.choice(["NORMAL", "RISKY", "CRITICAL"])
    }

@app.get("/api/inventory")
def get_inventory():
    return {
        "wood_units": random.randint(20, 200),
        "metal_units": random.randint(10, 100),
        "status": random.choice(["OK", "LOW", "OUT_OF_STOCK"])
    }

@app.get("/api/orders")
def get_orders():
    return {
        "pending_orders": random.randint(1, 50),
        "priority": random.choice(["LOW", "MEDIUM", "HIGH"])
    }