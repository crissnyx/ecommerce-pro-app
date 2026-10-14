import streamlit as st
import pandas as pd
import plotly.express as px
from prophet import Prophet
from utils.connector import fetch_live_ecommerce_data

st.set_page_config(page_title="AI Sales Forecasting", page_icon="🤖", layout="wide")

st.title("🤖 AI-Powered Sales Forecasting")
st.markdown("Predict future revenue trends using machine learning models (Meta Prophet) trained on live transaction history.")

# Fetch data
with st.spinner("Loading historical data for AI training..."):
    df = fetch_live_ecommerce_data()

# Aggregate daily revenue across all categories for forecasting
df_daily = df.groupby('Date')['Revenue'].sum().reset_index()

# Prepare dataframe for Prophet (requires columns named 'ds' and 'y')
df_prophet = df_daily.rename(columns={'Date': 'ds', 'Revenue': 'y'})

# Sidebar configuration for forecasting
st.sidebar.header("Forecast Settings")
forecast_days = st.sidebar.slider("Projection Horizon (Days):", min_value=7, max_value=60, value=30, step=1)

# Train Prophet Model
with st.spinner("Training predictive model..."):
    model = Prophet(weekly_seasonality=True, daily_seasonality=False)
    model.fit(df_prophet)
    
    # Make future predictions
    future = model.make_future_dataframe(periods=forecast_days)
    forecast = model.predict(future)

# Display metrics of prediction
col1, col2 = st.columns(2)
last_historical_revenue = df_daily['Revenue'].iloc[-1]
predicted_end_revenue = forecast['yhat'].iloc[-1]

with col1:
    st.metric(label="Latest Recorded Daily Revenue", value=f"${last_historical_revenue:,.2f}")
with col2:
    st.metric(label=f"Projected Revenue (in {forecast_days} days)", value=f"${predicted_end_revenue:,.2f}")

st.divider()

# Plotting the forecast with Plotly (usando xaxes y yaxes en plural)
st.subheader("Revenue Forecast & Confidence Intervals")
fig = px.line(forecast, x='ds', y='yhat', title=f"Sales Forecast for the Next {forecast_days} Days", template="plotly_dark")
fig.add_scatter(x=df_prophet['ds'], y=df_prophet['y'], mode='markers', name='Actual Revenue')
fig.update_xaxes(title="Date")
fig.update_yaxes(title="Revenue ($)")
st.plotly_chart(fig, use_container_width=True)

# Detailed forecast table
with st.expander("View Detailed Forecast Data"):
    st.dataframe(forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(forecast_days), use_container_width=True)