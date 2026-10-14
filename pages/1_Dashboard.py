import streamlit as st
import pandas as pd
import plotly.express as px
from utils.connector import fetch_live_ecommerce_data

st.set_page_config(page_title="Sales Dashboard", page_icon="📊", layout="wide")

st.title("📊 Real-Time Sales Dashboard")
st.markdown("Commercial performance overview connected directly to the transaction engine.")

# Fetch live sales data from connector
with st.spinner("Syncing data from E-Commerce API..."):
    df = fetch_live_ecommerce_data()

# Sidebar filters
st.sidebar.header("Dashboard Filters")
available_categories = df['Category'].unique().tolist()
selected_categories = st.sidebar.multiselect(
    "Select Categories:",
    options=available_categories,
    default=available_categories
)

# Filter Dataframe
df_filtered = df[df['Category'].isin(selected_categories)]

# Key Performance Indicators (KPIs)
col1, col2, col3 = st.columns(3)
total_revenue = df_filtered['Revenue'].sum()
total_transactions = df_filtered['Transactions'].sum()
avg_ticket = total_revenue / total_transactions if total_transactions > 0 else 0

with col1:
    st.metric(label="Total Revenue", value=f"${total_revenue:,.2f}")
with col2:
    st.metric(label="Total Transactions", value=f"{total_transactions:,}")
with col3:
    st.metric(label="Average Order Value", value=f"${avg_ticket:,.2f}")

st.divider()

# Plotly Charts
col_g1, col_g2 = st.columns(2)

with col_g1:
    st.subheader("Daily Revenue Trend")
    df_daily = df_filtered.groupby('Date')['Revenue'].sum().reset_index()
    fig_line = px.line(df_daily, x='Date', y='Revenue', title="Daily Revenue Evolution", template="plotly_dark")
    st.plotly_chart(fig_line, use_container_width=True)

with col_g2:
    st.subheader("Revenue by Category")
    df_cat = df_filtered.groupby('Category')['Revenue'].sum().reset_index()
    fig_pie = px.pie(df_cat, names='Category', values='Revenue', title="Sales Distribution by Category", hole=0.4, template="plotly_dark")
    st.plotly_chart(fig_pie, use_container_width=True)

# Detailed data expander
with st.expander("View Raw Transaction Data"):
    st.dataframe(df_filtered, use_container_width=True)