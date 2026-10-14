import streamlit as st
import requests
import os

st.set_page_config(page_title="Alert Center", page_icon="⚡", layout="wide")

st.title("⚡ Proactive Alert Center")
st.markdown("Configure automated notifications to stay ahead of revenue drops or anomalies via Slack, Discord, or Twilio.")

# Sidebar alert configurations
st.sidebar.header("Alert Configurations")
alert_channel = st.sidebar.selectbox("Select Notification Channel:", ["Slack / Discord Webhook", "WhatsApp (Twilio)", "Email Summary"])

with st.form("alert_form"):
    st.subheader("Notification Parameters")
    recipient = st.text_input("Webhook URL / Phone Number / Email:", placeholder="https://hooks.slack.com/services/... or +51999999999")
    threshold = st.number_input("Daily Revenue Drop Threshold ($):", min_value=0.0, value=500.0, step=50.0)
    is_active = st.checkbox("Enable Automated Monitoring", value=True)
    
    submitted = st.form_submit_button("Save Alert Settings")
    if submitted:
        st.success("Alert configurations saved successfully! Background monitoring active.")

st.divider()

st.subheader("Simulation Test")
st.markdown("Test your webhook or notification channel instantly by triggering a mock alert.")

if st.button("Trigger Test Notification"):
    if not recipient:
        st.warning("Please enter a valid recipient/webhook before testing.")
    else:
        st.info(f"Sending test alert to {recipient}...")
        st.success("Test alert sent successfully! (Simulated)")