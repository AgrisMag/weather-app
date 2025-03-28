from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import weather
from app.config import WEATHER_API_KEY

app = FastAPI(
    title="Weather API",
    description="A FastAPI application that interacts with WeatherAPI.com",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify actual origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# Check if API key is configured
@app.on_event("startup")
async def startup_event():
    if not WEATHER_API_KEY:
        raise ValueError("WEATHER_API_KEY environment variable is not set")


# Include routers
app.include_router(weather.router)


@app.get("/", tags=["root"])
async def root():
    """Root endpoint"""
    return {"message": "Welcome to the Weather API"}


# Handle 404 errors
@app.exception_handler(404)
async def not_found_exception_handler(request, exc):
    return {"detail": "The requested resource was not found"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
