from fastapi import FastAPI, Query
from tavily import TavilyClient
from summarize import summarize
import os
from dotenv import load_dotenv

load_dotenv()
tavily_api_key = os.getenv("TAVILY_API_KEY")
tavily_client = TavilyClient(api_key=tavily_api_key)

app = FastAPI(title="News Scout API")

@app.get("/news")
def get_ai_news(
    query: str = Query(
        default="Latest news in artificial intelligence",  # default search if none provided
        min_length=3,
        max_length=100,
        description="Search query for news"
    )
):
    response = tavily_client.search(
        query=query,
        include_answer=True,
        include_raw_content=False,
        max_results=3
    )

    articles = []
    for result in response["results"]:
        summary_text = summarize(result["content"])
        articles.append({
            "title": result["title"],
            "url": result["url"],
            "summary": summary_text
        })

    return {
        "query_used": query,
        "summary": response.get("answer", "No summary available."),
        "articles": articles
    }
