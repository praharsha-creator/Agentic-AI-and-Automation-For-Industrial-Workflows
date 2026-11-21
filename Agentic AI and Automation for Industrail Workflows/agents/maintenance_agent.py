class MaintenanceAgent:
    def __init__(self, agent_name):
        self.agent_name = agent_name

    def analyze(self, temperature,vibration,usage_hours):
        if temperature > 80 or vibration > 5 or usage_hours > 15:
            return "RISKY"
        else:
            return "SAFE"    

    def decide_maintenance(self, machine_status):
        print(f"\n[{self.agent_name}] Analyzing machine status...")

        if machine_status == "RISKY":
            decision = "Maintenance Required"
        else:
            decision = "No Maintenance Needed"

        print(f"Decision: {decision}")
        return decision
