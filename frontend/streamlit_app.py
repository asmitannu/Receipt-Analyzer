
import streamlit as st
import requests
import pandas as pd
import mimetypes

st.set_page_config(page_title="Receipt Analyzer", layout="wide")
st.title("Smart Receipt Uploader")

BACKEND_URL = "http://localhost:8000/upload/"

uploaded_file = st.file_uploader("Upload receipt (.jpg, .png, .pdf, .txt)", type=["jpg", "png", "pdf", "txt"])

if uploaded_file:
    mime_type, _ = mimetypes.guess_type(uploaded_file.name)
    files = {
        "file": (
            uploaded_file.name,
            uploaded_file.getvalue(),
            mime_type or "application/octet-stream"
        )
    }

    with st.spinner("Processing receipt..."):
        response = requests.post(BACKEND_URL, files=files)

    if response.status_code == 200:
        try:
            receipt = response.json()
            st.success("Receipt processed successfully!")

            if isinstance(receipt, dict):
                st.json(receipt)
                df = pd.DataFrame([receipt])
                st.dataframe(df)

                st.subheader("Summary")
                st.write(f"**Vendor:** {receipt.get('vendor', 'Unknown')}")
                st.write(f"**Date:** {receipt.get('date', 'N/A')}")
                st.write(f"**Amount:** {receipt.get('amount', 0)} {receipt.get('currency', '')}")
            else:
                st.warning("Unexpected response format.")

        except Exception as e:
            st.error(f"Failed to parse response JSON: {e}")
    else:
        st.error(f"Error: {response.status_code} - {response.text}")
