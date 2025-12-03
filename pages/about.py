import streamlit as st

st.title("ℹ️ About Chrome History Explorer")

st.markdown("""
This app lets you explore your **Google Chrome browsing history** locally or via Streamlit Community Cloud.

### What it does
- Reads your local Chrome `History` SQLite database.
- Shows a **raw table** of entries.
- Aggregates by **domain** to show:
  - A bar chart of visits by domain.
  - A pie chart of how many domains you've visited less than a chosen threshold.

### Privacy
- Your uploaded file is processed only in memory for this session.
- It is not stored permanently or sent anywhere else (beyond the Streamlit app server you're using).
""")