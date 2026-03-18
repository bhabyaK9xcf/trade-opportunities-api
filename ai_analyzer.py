import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

async def analyze_market(sector, news):

    prompt = f"""
    Analyze the Indian {sector} sector using the news below.

    News Headlines:
    {news}

    Generate a structured markdown report with:

    ## Market Overview
    ## Key Trends
    ## Trade Opportunities
    ## Risks
    """

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)

    return response.text
