import requests

BASE_URL = "http://127.0.0.1:8000/api"

def get_machine_status():
    response = requests.get(f"{BASE_URL}/machine-status")
    return response.json()

def get_inventory():
    response = requests.get(f"{BASE_URL}/inventory")
    return response.json()

def get_orders():
    response = requests.get(f"{BASE_URL}/orders")
    return response.json()