import streamlit as st
from utils import load_data, save_data, safe_generate

st.title("Customer Feedback")

rating = st.selectbox("Select star rating", [1, 2, 3, 4, 5])
review = st.text_area("Write your review")

if st.button("Submit"):
    if review.strip() == "":
        st.warning("Please write a review.")
    else:
        response_prompt = f"""
You are an automated customer support system.

Your task:
Generate ONE final response that the business would directly send to the customer.

Rules:
- Write only ONE response
- Be polite and professional
- Do NOT give multiple options
- Do NOT explain your reasoning
- Keep it concise (2–4 sentences)

Customer rating: {rating} stars
Customer review:
"{review}"

Business response:
"""


        ai_response = safe_generate(response_prompt)

        data = load_data()
        data.append({
            "rating": rating,
            "review": review,
            "ai_response": ai_response
        })
        save_data(data)

        st.success("Thank you for your feedback!")
        st.markdown("### AI Response")
        st.write(ai_response)
