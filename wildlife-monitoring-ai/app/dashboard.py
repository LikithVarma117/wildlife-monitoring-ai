import streamlit as st
import pandas as pd

def show_dashboard(log_path="data/detections.csv"):
    st.header("📊 Live Detection Metrics")
    df = pd.read_csv(log_path)
    st.write("Total Detections:", len(df))
    st.bar_chart(df['species'].value_counts())
    st.line_chart(df['timestamp'])