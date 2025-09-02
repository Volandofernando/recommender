import streamlit as st
import numpy as np
import altair as alt
import joblib
import pandas as pd

st.title("🤖 Fabric Recommender")

model = joblib.load("models/fabric_model.pkl")
scaler = joblib.load("models/scaler.pkl")
df = pd.read_csv("models/processed_dataset.csv")

st.sidebar.header("Input Your Conditions")
temperature = st.sidebar.slider("🌡️ Temperature (°C)", 10, 45, 28)
humidity = st.sidebar.slider("💧 Humidity (%)", 10, 100, 60)
sweat_sensitivity = st.sidebar.radio("🧍 Sweat Sensitivity", ["Low", "Medium", "High"])
activity_intensity = st.sidebar.radio("🏃 Activity Intensity", ["Low", "Moderate", "High"])

sweat_map = {"Low": 1, "Medium": 2, "High": 3}
activity_map = {"Low": 1, "Moderate": 2, "High": 3}
sweat_num, activity_num = sweat_map[sweat_sensitivity], activity_map[activity_intensity]

user_input = np.array([[
    sweat_num * 5,
    800 + humidity * 5,
    60 + activity_num * 10,
    0.04 + (temperature - 25) * 0.001
]])
user_input_scaled = scaler.transform(user_input)

predicted_score = model.predict(user_input_scaled)[0]
df["predicted_diff"] = abs(df["comfort_score"] - predicted_score)
top_matches = df.sort_values("predicted_diff").head(3)

st.markdown("## 🔹 Recommended Fabrics")
cols = st.columns(3)
for i, (_, row) in enumerate(top_matches.iterrows()):
    with cols[i]:
        st.markdown(f"### 🧵 {row['fabric_type']}")
        st.metric("Comfort Score", round(row["comfort_score"], 2))

chart = alt.Chart(top_matches).mark_bar(color="#1F4E79").encode(
    x="fabric_type", y="comfort_score"
)
st.altair_chart(chart, use_container_width=True)
