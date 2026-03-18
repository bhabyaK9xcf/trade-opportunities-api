import httpx
from bs4 import BeautifulSoup

async def fetch_sector_news(sector: str):
    url = f"https://news.google.com/search?q={sector}+India"

    async with httpx.AsyncClient() as client:
        res = await client.get(url)

    soup = BeautifulSoup(res.text, "html.parser")

    headlines = [h.text for h in soup.select("a.DY5T1d")[:5]]

    return headlines
