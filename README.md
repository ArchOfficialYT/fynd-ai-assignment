# fynd-ai-task2

## Task 2: AI-Powered Customer Feedback System

### Overview

This task implements a lightweight AI-powered feedback management system consisting of two web dashboards: a user-facing feedback submission interface and an internal admin dashboard. The system demonstrates practical LLM integration for customer interaction and operational analytics.

---

## System Architecture

The application is built using Streamlit, allowing both frontend and backend logic to be implemented in Python. A shared JSON file is used for persistent storage to keep the system simple and easily deployable.

**Frontend & Backend:** Streamlit  
**LLM:** Google Gemini API  
**Storage:** JSON file (`data.json`)  
**Deployment Target:** HuggingFace Spaces  

---

## User Dashboard

The user dashboard allows customers to:

- Select a star rating (1–5)
- Submit a textual review
- Receive an AI-generated response from the business

Upon submission, the system stores the rating, review, and AI response in shared storage. This demonstrates real-time AI usage for customer engagement.

---

## Admin Dashboard

The admin dashboard provides internal visibility into submitted feedback. For each review, it displays:

- Customer rating
- Review text
- AI-generated response
- AI-generated summary of the feedback
- AI-recommended action for the business

This dashboard highlights how LLMs can be used not only for customer interaction but also for operational insights.

---

## AI Integration & Reliability

The system integrates the Gemini LLM using a safe retry mechanism to handle API rate limits. In case of quota exhaustion, the application degrades gracefully by returning a fallback response, ensuring the user experience remains smooth and the application does not hang.

This approach reflects real-world production practices where AI systems must handle external service limitations reliably.

---

## Key Design Decisions

- **Two-Dashboard Separation:** Clearly separates customer interaction from internal analytics.
- **Graceful Failure Handling:** Prevents UI blocking when LLM quotas are exceeded.
- **Simple Storage Layer:** JSON storage keeps the system transparent and easy to reason about.
- **Extensible Architecture:** Can be easily upgraded to use a database or authentication layer.

---

## Outcome

The final system demonstrates a complete AI-powered feedback loop:

**User input → AI response → Admin analysis → Business action**

This fulfills the task requirements and showcases practical AI engineering skills, including LLM integration, system design, and reliability considerations.
