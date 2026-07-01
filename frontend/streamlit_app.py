import streamlit as st
import requests
import json

st.set_page_config(
    page_title="AI Data Validation Agent",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Data Validation Agent")

st.write("Upload a CSV dataset and receive AI-powered validation insights.")

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

if uploaded_file is not None:

    if st.button("🚀 Validate Dataset", use_container_width=True):

        files = {
            "file": (
                uploaded_file.name,
                uploaded_file.getvalue(),
                "text/csv"
            )
        }

        with st.spinner("🤖 AI is analyzing your dataset..."):

            response = requests.post(
                "http://127.0.0.1:8000/validate",
                files=files
            )

        if response.status_code == 200:

            data = response.json()

            report = data["validation_report"]

            summary = report.get("Validation Summary", "Unknown")
            severity = report.get("Severity", "Unknown")
            readiness = report.get("Readiness Decision", "Unknown")

            st.success("✅ Validation Completed Successfully")

            col1, col2, col3 = st.columns(3)

            col1.metric("Validation", summary)
            col2.metric("Severity", severity)
            col3.metric("Readiness", readiness)

            st.divider()

            if readiness.upper() == "READY":
                st.success("🟢 Dataset is READY for downstream consumption.")
            else:
                st.error("🔴 Dataset is NOT READY for downstream consumption.")

            st.divider()

            st.subheader("🤖 AI Validation Summary")

            st.markdown(data["ai_summary"])

            st.divider()

            with st.expander("📄 View Validation Report"):

                st.json(report)

            st.download_button(
                label="📥 Download Validation Report",
                data=json.dumps(
                    report,
                    indent=4
                ),
                file_name="validation_report.json",
                mime="application/json"
            )

        else:

            st.error("❌ Validation Failed")