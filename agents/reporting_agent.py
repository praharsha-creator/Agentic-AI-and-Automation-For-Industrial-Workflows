class ReportingAgent:
    def __init__(self, agent_name):
        self.agent_name = agent_name

    def generate_report(self, machine_status, maintenance_decision, inventory_status):
        print(f"\n[{self.agent_name}] Generating report...")

        report = {
            "Machine Status": machine_status,
            "Maintenance Decision": maintenance_decision,
            "Inventory Status": inventory_status
        }

        for key, value in report.items():
            print(f"{key}: {value}")

        return report
