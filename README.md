# Weather App API

A FastAPI-based application that provides weather information by interacting with the WeatherAPI.com service.

## Features

- Get current weather conditions for any location
- Retrieve multi-day weather forecasts
- Search for locations with autocomplete functionality
- Secure API key management
- Asynchronous API calls for improved performance

## Tech Stack

- **FastAPI**: Modern, fast web framework for building APIs
- **httpx**: Asynchronous HTTP client
- **python-dotenv**: Environment variable management
- **uvicorn**: ASGI server

## Project Structure

```
weather-app/
├── app/
│   ├── __init__.py
│   ├── main.py         # FastAPI application
│   ├── config.py       # Configuration including API key
│   ├── api/
│   │   ├── __init__.py
│   │   └── weather.py  # Weather API routes
│   └── services/
│       ├── __init__.py
│       └── weather_service.py  # Service to make API calls
├── docs/               # Documentation
├── tests/              # Test files
├── .env                # Environment variables (not in version control)
├── .gitignore          # Git ignore file
├── requirements.txt    # Project dependencies
├── requirements.in     # Source dependencies for pip-compile
├── setup.py            # Package setup
└── README.md           # This file
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/weather-app.git
   cd weather-app
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root with your WeatherAPI.com API key:
   ```
   WEATHER_API_KEY=your_api_key_here
   ```
   Get your API key by signing up at [WeatherAPI.com](https://www.weatherapi.com/).

## Usage

1. Start the development server:
   ```bash
   uvicorn app.main:app --reload
   ```

2. Access the API documentation:
   - Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

3. Make API requests:
   - Get current weather: `GET /weather/current?location=London`
   - Get forecast: `GET /weather/forecast?location=New York&days=5`
   - Search locations: `GET /weather/search?query=San Fran`

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/weather/current` | GET | Get current weather for a location |
| `/weather/forecast` | GET | Get weather forecast for a location |
| `/weather/search` | GET | Search for locations |

## Development

For development work:

1. Install development dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

2. Run tests:
   ```bash
   pytest
   ```

## Environment Variables

| Variable | Description |
|----------|-------------|
| `WEATHER_API_KEY` | Your WeatherAPI.com API key |

## License

[MIT](LICENSE)

## Credits

This project uses the [WeatherAPI.com](https://www.weatherapi.com/) service for weather data.