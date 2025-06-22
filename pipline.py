from tavily import TavilyClient
from summarize import summarize
import os
from dotenv import load_dotenv

# Load API keys from .env file
load_dotenv()
tavily_api_key = os.getenv("TAVILY_API_KEY")

# Initialize Tavily client
tavily_client = TavilyClient(api_key=tavily_api_key)

def main():
    print("🔎 Searching latest AI news with Tavily...")

    response = tavily_client.search(
        query="Latest news in artificial intelligence",
        include_answer=True,
        include_raw_content=False,
        max_results=3
    )

    print("\n🔍 Summary:")
    print(response.get("answer", "No summary available."))

    print("\n📰 Articles:")
    for idx, result in enumerate(response["results"], 1):
        print(f"\n{idx}. {result['title']}")
        print(f"URL: {result['url']}")
        print("🧠 GPT Summary:")
        summary = summarize(result["content"])
        print(summary)

if __name__ == "__main__":
    main()
