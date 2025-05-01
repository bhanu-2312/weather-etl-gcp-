## This project is about an automated ETL (Extract, Transform, Load) pipeline that fetches daily weather data from OpenWeatherMap API and loads it into Google BigQuery.


- **Google Cloud Functions**
- **Google BigQuery**
- **Google Cloud Scheduler**
- **Python 3.10**
- **OpenWeatherMap API**


## 📈 ETL Workflow
1. **Extract** weather data for a specific city (e.g., London) via OpenWeatherMap API.
2. **Transform** the JSON response to extract relevant fields like temperature, humidity, description.
3. **Load** the cleaned data into a BigQuery table (`weather2312.daily_weather`).
