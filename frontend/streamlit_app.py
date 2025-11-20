import streamlit as st
import requests
import json

API_URL = "http://localhost:8000"

st.title("Autonomous QA Agent")

# --------------------------
# 1. Upload Documents + HTML
# --------------------------
st.header("1. Upload Documents")
uploaded_files = st.file_uploader(
    "Upload support docs (.md, .txt, .json) + checkout.html", 
    accept_multiple_files=True
)

if uploaded_files:
    docs_text = []
    html_text = ""
    
    for f in uploaded_files:
        content = f.read().decode("utf-8")
        if f.name.endswith(".html"):
            html_text = content
        else:
            docs_text.append(content)

    if st.button("Build Knowledge Base"):
        r = requests.post(
            f"{API_URL}/upload_docs",
            json={"docs": docs_text, "html": html_text}
        )
        st.success(r.json())

# --------------------------
# 2. Generate Test Cases
# --------------------------
st.header("2. Generate Test Cases")
query = st.text_input("Enter test case request (e.g., discount code cases)")

if st.button("Generate Test Cases"):
    if query.strip() == "":
        st.warning("Please enter a query!")
    else:
        res = requests.post(
            f"{API_URL}/generate_test_cases", 
            json={"query": query}
        ).json()
        st.json(res)

# --------------------------
# 3. Generate Selenium Script
# --------------------------
st.header("3. Generate Selenium Script")
selected_tc = st.text_area("Paste selected test case JSON here")

if st.button("Generate Selenium Script"):
    if selected_tc.strip() == "":
        st.warning("Please paste a valid test case JSON!")
    else:
        try:
            tc_dict = json.loads(selected_tc)
        except json.JSONDecodeError:
            st.error("Invalid JSON format for test case!")
        else:
            res = requests.post(
                f"{API_URL}/generate_selenium",
                json={"test_case": tc_dict}
            ).json()
            st.code(res["script"], language="python")