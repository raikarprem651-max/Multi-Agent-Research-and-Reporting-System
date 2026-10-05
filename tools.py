from langchain_core.tools import tool
import os
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
import os 
from rich import print 
from dotenv import load_dotenv
load_dotenv()

tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def web_search(query:str) -> str:
    """Search the web for the given query and return the results."""
    results = tavily_client.search(query=query,max_results=5)
    out =[]
    for r in results['results']:
        out.append(
            f"Title: {r['title']}\nURL: {r['url']}\nDescription: {r['content']}\n")
        
    return " \n---\n".join(out)
print(web_search.invoke("What is the recent news of war" ))

@tool
def scrape_web(url:str) -> str:
    """Scrape the content of the given URL and return the text."""
    try:
        resp = requests.get(url, timeout=9, headers={"User-Agent": "Mozilla/5.0"})
        soup= BeautifulSoup(resp.text, 'html.parser')
        for tag in soup(['script', 'style','nav','footer']):
            tag.decompose()
        return soup.get_text(separator=' ', strip=True)
    except Exception as e:
        return f"Could not scrape url : {str(e)}"
print(scrape_web.invoke("https://www.hindustantimes.com/india-news/west-asia-crisis-straits-of-hormuz-blockade-to-figure-in-heads-of-mission-conference-next-week-101777005394908.html"))
