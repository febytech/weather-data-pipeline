import json
import boto3
from urllib import request
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('weather_data')

API_KEY = "your_api_key"

def lambda_handler(event, context):

    city = "Kochi"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

    response = request.urlopen(url)

    data = json.loads(response.read())

    item = {
        'city': city,
        'temperature': str(data['main']['temp']),
        'humidity': str(data['main']['humidity']),
        'timestamp': datetime.now().isoformat()
    }

    table.put_item(Item=item)

    return {
        'statusCode': 200,
        'body': json.dumps('Weather data stored')
    }