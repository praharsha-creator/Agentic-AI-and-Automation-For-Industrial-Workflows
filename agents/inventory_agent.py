class InventoryAgent:
    def __init__(self, agent_name):
        self.agent_name = agent_name

    def check_inventory(self, stock, threshold):
        print(f"\n[{self.agent_name}] Checking inventory levels...")

        if stock < threshold:
            status = "LOW STOCK"
        else:
            status = "STOCK OK"

        print(f"Inventory Status: {status}")
        return status
