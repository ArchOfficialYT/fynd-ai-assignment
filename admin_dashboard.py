import streamlit as st
from utils import load_data, safe_generate

st.title("Admin Dashboard")

data = load_data()

if len(data) == 0:
    st.info("No feedback submitted yet.")
else:
    for i, item in enumerate(reversed(data), 1):
        st.markdown(f"## Feedback {i}")
        st.write("⭐ Rating:", item["rating"])
        st.write("📝 Review:", item["review"])
        st.write("💬 AI Response:", item["ai_response"])

        summary_prompt = f"""
Summarize the following customer review in one sentence:

"{item['review']}"
"""
        action_prompt = f"""
Based on the review below, suggest one recommended action for the business:

"{item['review']}"
"""

        summary = safe_generate(summary_prompt)
        action = safe_generate(action_prompt)

        st.write("📌 AI Summary:", summary)
        st.write("✅ Recommended Action:", action)
        st.divider()
