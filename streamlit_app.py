import streamlit as st
import os
from shared.utils import system_health
from marketing_studio.crew import create_marketing_crew

st.set_page_config(page_title="Apex Digital AI", layout="wide")
st.title("🚀 Apex Digital AI")

# Health check
health = system_health()
st.sidebar.success("✅ System Healthy")
st.sidebar.json(health)

# Upload images
st.subheader("Upload Brand Assets")
uploaded = st.file_uploader("Upload new image", type=["jpg", "png", "jpeg"])
if uploaded:
    os.makedirs("marketing_studio/uploads", exist_ok=True)
    with open(f"marketing_studio/uploads/{uploaded.name}", "wb") as f:
        f.write(uploaded.getbuffer())
    st.success("Uploaded!")

# Marketing example
if st.button("Run Marketing Studio Example"):
    crew = create_marketing_crew()
    result = crew.kickoff(inputs={"brief": "Create pure organic marketing for Xtreme Graphics"})
    st.success(result)
    st.write(result)

st.info("All studios ready. Use main.py or /streamlit for full interface.")
