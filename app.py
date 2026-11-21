import streamlit as st
import random

# Import your agents
from agents.inventory_agent import InventoryAgent
from agents.maintenance_agent import MaintenanceAgent
from agents.predictive_agent import PredictiveAgent

# Initialize agents
inventory_agent = InventoryAgent("Inventory Agent")
maintenance_agent = MaintenanceAgent("Maintenance Agent")
predictive_agent = PredictiveAgent("Predictive Agent")

# Page config
st.set_page_config(page_title="Smart Factory AI", layout="wide")

# Title
st.title("Agentic AI and Automation for Industry Workflows")
st.markdown("AI-powered Industrial Monitoring & Decision System")

# Sidebar inputs
st.sidebar.header("Sensor Inputs")

temperature = st.sidebar.slider("Temperature (°C)", 20, 120, 60)
vibration = st.sidebar.slider("Vibration Level", 0, 10, 3)
usage_hours = st.sidebar.slider("Usage Hours", 0, 24, 8)

# Run button
if st.sidebar.button("Run System"):

    st.subheader("System Output")
    

    # Initialize agents
    inventory_agent = InventoryAgent("Inventory Agent")
    maintenance_agent = MaintenanceAgent("Maintenance Agent")
    predictive_agent = PredictiveAgent("Predictive Agent")

    # Inventory check
    inventory_data = inventory_agent.check_inventory(stock=100,threshold=50)

if st.button("RUN System"):

    predictive_agent.train_model()
    prediction = predictive_agent.predict_next(temperature, vibration, usage_hours)
    machine_status = maintenance_agent.analyze(temperature, vibration, usage_hours)
    maintenance_decision = maintenance_agent.decide_maintenance(machine_status)
    stock = 100 - (usage_hours * 3)
    threshold = 50
    inventory_status = inventory_agent.check_inventory(stock, threshold)
   
    st.subheader("System Results")

    st.success(f"Machine Status:{machine_status}")
    st.info(f"Maintenance Decision:{maintenance_decision}")
    st.info(f"Inventory Status:{inventory_status}")
    st.info(f"Future Prediction:{maintenance_decision}")
    st.write("DEBUG:", machine_status)

    st.subheader("AI Explanation")

    if machine_status == "RISKY":
        st.error("⚠️ Machine is operating under risky conditions!")
        st.warning("Maintenance is required to avoid failure.")
    else:
        st.success("✅ Machine operating under normal conditions.")
    if inventory_status == "LOW STOCK":
        st.warning("Inventory is low. Reordering recommended.")
    else:        
        st.success("Inventory levels are sufficient.")


    # Predictive Model
    predictive_agent.train_model()
    future_decision = predictive_agent.predict_next(temperature, vibration, usage_hours)

    # Display results
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Machine Status", machine_status)

    with col2:
        st.metric("Inventory Status", inventory_status)

    with col3:
        st.metric("Future Prediction", maintenance_decision)

    st.divider()

    # Detailed Analysis
    st.subheader("AI Explanation")

    if machine_status == "RISKY":
        st.error("High temperature or vibration detected. Maintenance required soon.")
    else:
        st.success("Machine operating under normal conditions.")

    if inventory_status == "LOW STOCK":
        st.warning("Inventory is low. Reordering recommended.")
    else:
        st.success("Inventory levels are sufficient.")

    # Raw Data
    st.subheader("Inventory Data")

    inventory_data = {"Current Stock": stock, "Threshold": threshold, "Status": inventory_status}
    st.json(inventory_data)
    final_status = machine_status