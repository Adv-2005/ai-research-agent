import requests
import streamlit as st

st.title("AI Research Agent")

query = st.text_input("Company / Topic / Ticker")

if st.button("Research"):

    try:
        response = requests.post(
            "http://localhost:8000/research",
            json={
                "query": query,
                "type": "company"
            }
        )

        if response.status_code == 200:
            report = response.json()["report"]
            st.markdown(report)
        else:
            st.error(f"Backend error: {response.text}")

    except Exception as e:
        st.exception(e)