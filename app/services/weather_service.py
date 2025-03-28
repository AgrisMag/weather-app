import httpx
from fastapi import HTTPException

from app.config import WEATHER_API_KEY, WEATHER_API_BASE_URL


class WeatherService:
    """Service for interacting with the WeatherAPI.com API"""

    async def get_current_weather(self, location: str):
        """
        Get current weather for a location

        Args:
            location: City name, latitude/longitude, IP address, etc.

        Returns:
            dict: Weather data for the specified location
        """
        try:
            # Using httpx for async HTTP requests
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{WEATHER_API_BASE_URL}/current.json",
                    params={
                        "key": WEATHER_API_KEY,
                        "q": location,
                        "aqi": "no"  # Air Quality Data (yes/no)
                    }
                )

                # Raise exception for non-200 responses
                response.raise_for_status()

                return response.json()

        except httpx.HTTPStatusError as e:
            # Handle API-specific errors
            error_data = e.response.json()
            raise HTTPException(
                status_code=e.response.status_code,
                detail=error_data.get("error", {}).get("message", str(e))
            )
        except Exception as e:
            # Handle other exceptions
            raise HTTPException(status_code=500, detail=f"Error fetching weather data: {str(e)}")

    async def get_forecast(self, location: str, days: int = 3):
        """
        Get weather forecast for a location

        Args:
            location: City name, latitude/longitude, IP address, etc.
            days: Number of days of forecast (1-10)

        Returns:
            dict: Forecast data for the specified location
        """
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{WEATHER_API_BASE_URL}/forecast.json",
                    params={
                        "key": WEATHER_API_KEY,
                        "q": location,
                        "days": days,
                        "aqi": "no",
                        "alerts": "no"  # Weather alerts (yes/no)
                    }
                )

                response.raise_for_status()
                return response.json()

        except httpx.HTTPStatusError as e:
            error_data = e.response.json()
            raise HTTPException(
                status_code=e.response.status_code,
                detail=error_data.get("error", {}).get("message", str(e))
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error fetching forecast data: {str(e)}")

    async def search_locations(self, query: str):
        """
        Search for locations/autocomplete

        Args:
            query: Location search query

        Returns:
            list: Matching locations
        """
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(
                    f"{WEATHER_API_BASE_URL}/search.json",
                    params={
                        "key": WEATHER_API_KEY,
                        "q": query
                    }
                )

                response.raise_for_status()
                return response.json()

        except httpx.HTTPStatusError as e:
            error_data = e.response.json()
            raise HTTPException(
                status_code=e.response.status_code,
                detail=error_data.get("error", {}).get("message", str(e))
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error searching locations: {str(e)}")
