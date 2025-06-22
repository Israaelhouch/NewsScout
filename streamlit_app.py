import streamlit as st
from tavily import TavilyClient
from summarize import summarize
import os
from dotenv import load_dotenv

load_dotenv()
tavily_api_key = os.getenv("TAVILY_API_KEY")
tavily_client = TavilyClient(api_key=tavily_api_key)

st.title("📰 News Scout")

query = st.text_input("Enter your search query", "Latest AI news")

if st.button("Search"):
    with st.spinner("Searching..."):
        response = tavily_client.search(
            query=query,
            include_answer=True,
            max_results=3
        )
        st.subheader("🔍 Summary")
        st.write(response.get("answer", "No summary found."))

        for res in response["results"]:
            st.markdown(f"### {res['title']}")
            st.markdown(f"[Read more]({res['url']})")
            st.write("🧠 GPT Summary:")
            summary = summarize(res["content"])
            st.info(summary)
