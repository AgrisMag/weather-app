import os
from dotenv import load_dotenv

load_dotenv()  # Load variables from .env file

WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")
WEATHER_API_BASE_URL = "http://api.weatherapi.com/v1"
