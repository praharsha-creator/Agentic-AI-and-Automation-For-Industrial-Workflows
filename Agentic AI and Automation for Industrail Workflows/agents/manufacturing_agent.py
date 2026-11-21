class ManufacturingAgent:
    def __init__(self, agent_name):
        self.agent_name = agent_name

    def observe_machine(self, temperature, vibration, usage_hours):
        print(f"\n[{self.agent_name}] Observing machine data...")

        if temperature > 90 or vibration > 1.5:
            status = "RISKY"
        else:
            status = "NORMAL"

        print(f"Machine Status: {status}")

        return status
