import functions_framework
import requests
from google.cloud import bigquery
from datetime import datetime
import os

@functions_framework.http
def hello_http(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    request_json = request.get_json(silent=True)
    request_args = request.args
    weather_etl()
    if request_json and 'name' in request_json:
        name = request_json['name']
    elif request_args and 'name' in request_args:
        name = request_args['name']
    else:
        name = 'World'
    return 'Hello {}!'.format(name)


def weather_etl():
    api_key = '0e2b8de826535a55535ccea382236be7'  # set this as an env var
    city = 'London'
    
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()

    row = {
        'city': city,
        'temperature': data['main']['temp'],
        'humidity': data['main']['humidity'],
        'description': data['weather'][0]['description'],
        'timestamp': datetime.utcnow().isoformat()
    }

    client = bigquery.Client()
    table_id = 'valued-mediator-454414-h7.weather2312.Daily_weather'
    errors = client.insert_rows_json(table_id, [row])

    if errors:
        print(f"Encountered errors: {errors}")
    else:
        print("Data inserted successfully")
