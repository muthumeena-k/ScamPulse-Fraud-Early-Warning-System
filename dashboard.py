import streamlit as st
import pandas as pd

st.title("ScamPulse Early-Warning Network")
st.caption("Forward suspicious messages to the bot. Community reports help identify active scam campaigns in real time.")
try:
    df = pd.read_csv("scam_log.csv")
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    st.metric("Total Messages Checked", len(df))

    st.subheader("Scam Category Distribution")
    st.bar_chart(df["category"].value_counts())

    df["hour"] = df["timestamp"].dt.strftime("%H:00")
    st.subheader("Recent Fraud Reports (Hourly Activity)")
    st.line_chart(df.groupby("hour").size())

    most_common = df["category"].value_counts().idxmax()
    st.error(f" Active Scam Campaign Detected: {most_common}")
    st.caption("Community reports suggest this scam type is currently circulating.")
except:
    st.write("No data yet. Send messages to the Telegram bot first.")