from fastapi import APIRouter, HTTPException, Header
from app.services.scraper import fetch_sector_news
from app.services.ai_analyzer import analyze_market
from app.core.auth import verify_token
from app.core.session import track_session
from app.core.rate_limiter import limiter

router = APIRouter()

@router.get("/analyze/{sector}")
@limiter.limit("5/minute")
async def analyze_sector(sector: str, authorization: str = Header(None)):

    if not authorization:
        raise HTTPException(status_code=401, detail="Token required")

    try:
        user = verify_token(authorization.replace("Bearer ", ""))["sub"]
    except:
        raise HTTPException(status_code=403, detail="Invalid token")

    track_session(user)

    news = await fetch_sector_news(sector)

    if not news:
        raise HTTPException(status_code=500, detail="Failed to fetch news")

    report = await analyze_market(sector, news)

    return {
        "sector": sector,
        "report_markdown": report
    }
