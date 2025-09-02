import streamlit as st

st.title("📖 Guidance")
st.write("""
Follow these steps to use the recommender system:

1. Adjust **Temperature (°C)** → affects breathability.  
2. Adjust **Humidity (%)** → impacts sweat absorption.  
3. Choose your **Sweat Sensitivity** → Low, Medium, or High.  
4. Select **Activity Intensity** → Low, Moderate, or High.  

👉 Once ready, go to the **Recommender Page** to get your fabric suggestions.
""")

if st.button("➡️ Go to Recommender"):
    st.switch_page("pages/2_Recommender.py")
