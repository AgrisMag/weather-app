from fastapi import APIRouter, Depends, Query

from app.services.weather_service import WeatherService

router = APIRouter(prefix="/weather", tags=["weather"])


@router.get("/current")
async def get_current_weather(
        location: str = Query(..., description="City name, latitude/longitude, IP address, etc."),
        weather_service: WeatherService = Depends(lambda: WeatherService())
):
    """Get current weather for a location"""
    return await weather_service.get_current_weather(location)


@router.get("/forecast")
async def get_forecast(
        location: str = Query(..., description="City name, latitude/longitude, IP address, etc."),
        days: int = Query(3, ge=1, le=10, description="Number of days of forecast (1-10)"),
        weather_service: WeatherService = Depends(lambda: WeatherService())
):
    """Get weather forecast for a location"""
    return await weather_service.get_forecast(location, days)


@router.get("/search")
async def search_locations(
        query: str = Query(..., description="Location search query"),
        weather_service: WeatherService = Depends(lambda: WeatherService())
):
    """Search for locations"""
    return await weather_service.search_locations(query)
