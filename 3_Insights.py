import streamlit as st
import pandas as pd

st.title("📊 Dataset Insights")
df = pd.read_csv("models/processed_dataset.csv")

st.markdown("### Cleaned Dataset Preview")
st.dataframe(df.head(10))

st.write("More insights and visualizations can be added here.")
