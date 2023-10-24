import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')


url = "https://finance.yahoo.com"
request = requests.get(url)
content = request.text
print(content)

# URL=https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey=
