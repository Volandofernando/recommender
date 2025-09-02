import streamlit as st

st.set_page_config(page_title="AI Fabric Recommender", layout="wide")

st.markdown("""
<style>
    .main { background-color: #FAFAFA; }
    h1, h2, h3 { color: #1F4E79; font-family: 'Helvetica Neue', sans-serif; }
    .intro-box {
        padding: 2rem;
        border-radius: 15px;
        background: white;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
        text-align: center;
    }
    .start-btn {
        background: #1F4E79;
        color: white;
        font-size: 1.2rem;
        padding: 0.6rem 1.2rem;
        border-radius: 8px;
        text-decoration: none;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="intro-box">
    <h1>👕 AI Fabric Recommender</h1>
    <h3>Industry-Ready Comfort & Performance Predictor</h3>
    <p>
        This system leverages <b>Machine Learning</b> trained on academic literature and 
        real-world survey data to recommend fabrics based on temperature, humidity, sweat 
        sensitivity, and activity intensity.
    </p>
    <p>
        Built for <b>textile industry innovation</b> and <b>fashion R&D</b>.
    </p>
    <a href="Guidance" target="_self" class="start-btn">🚀 Start Guidance</a>
</div>
""", unsafe_allow_html=True)
