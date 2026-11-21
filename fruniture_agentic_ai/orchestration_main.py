from api_client import get_machine_status, get_inventory, get_orders

from analytics_agent import generate_visual_report
from logger import log_decision
import random
import time
from agents.predictive_agent import PredictiveAgent


from agents.manufacturing_agent import ManufacturingAgent
from agents.maintenance_agent import MaintenanceAgent
from agents.inventory_agent import InventoryAgent
from agents.reporting_agent import ReportingAgent

# Create agent objects
manufacturing_agent = ManufacturingAgent("Manufacturing Agent")
maintenance_agent = MaintenanceAgent("Maintenance Agent")
inventory_agent = InventoryAgent("Inventory Agent")
reporting_agent = ReportingAgent("Reporting Agent")
predictive_agent = PredictiveAgent("Predictive Agent")


print("\n===== STARTING FACTORY SIMULATION =====")

usage_hours = 500

for day in range(1, 6):

    print(f"\n--------- DAY {day} ---------")

    machine_data = get_machine_status()
    print(machine_data)
    inventory_data = get_inventory()
    print("Inventory Data:",inventory_data)
    orders = get_orders()

    temperature = machine_data["temperature"]
    vibration = machine_data["vibration"]
    usage_hours = machine_data["usage_hours"]

    print(f"Temp:{temperature} Vib:{vibration} Usage:{usage_hours}")

    # Manufacturing
machine_status = manufacturing_agent.observe_machine(
        temperature, vibration, usage_hours
    )

    # Maintenance
maintenance_decision = maintenance_agent.decide_maintenance(machine_status)

    # Inventory
print("Inventory Data:", inventory_data)

wood_units = inventory_data["wood_units"]
metal_units = inventory_data["metal_units"]

inventory_status = inventory_agent.check_inventory(wood_units, metal_units)

    # Reporting
reporting_agent.generate_report(
        machine_status,
        maintenance_decision,
        inventory_status
    )

    # Predictive
predictive_agent.train_model()

future_decision = predictive_agent.predict_next(
        temperature,
        vibration,
        usage_hours,
    )

print("[Predictive Agent] Decision:", future_decision["decision"])
print("[Predictive Agent] Reasons:")
for r in future_decision["reasons"]:
        print("-", r)
log_decision(
    day=day,
    temperature=temperature,
    vibration=vibration,
    usage_hours=usage_hours,
    machine_status=machine_status,

maintenance_decision=maintenance_decision,
    inventory_status=inventory_status,
    predictive_decision=future_decision["decision"]
)   

time.sleep(1)

print("\n===== SIMULATION COMPLETED =====")
generate_visual_report()

