from fastapi import FastAPI
from slowapi.middleware import SlowAPIMiddleware
from app.routes.analyze import router as analyze_router
from app.core.rate_limiter import limiter

app = FastAPI(title="Trade Opportunities API")

app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

app.include_router(analyze_router)
