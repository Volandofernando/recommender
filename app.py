import streamlit as st
from utils import load_config

config = load_config()
st.set_page_config(page_title=config["app"]["title"], layout="wide")

st.markdown(f'''
<style>
    .main {{ background-color: #FAFAFA; }}
    h1, h2, h3 {{ color: {config['app']['theme_color']}; }}
    .center {{ text-align: center; margin-top: 50px; }}
</style>
''', unsafe_allow_html=True)

st.title(f"👕 {config['app']['title']}")
st.subheader(config["app"]["subtitle"])

st.markdown("### Welcome to the AI-Powered Fabric Recommender 👕")
st.write("This app helps you choose the most comfortable fabrics based on temperature, humidity, sweat sensitivity, and activity intensity.")

if st.button("🚀 Get Started"):
    st.switch_page("pages/1_Guidance.py")
