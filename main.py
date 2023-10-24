import requests
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv('API_KEY')

# make a request
url = f"https://newsapi.org/v2/everything?" \
      f"q=tesla&sortBy=publishedAt&apiKey={api_key}"

# Get the dict
request = requests.get(url)
content = request.json()

# print titles
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + article["description"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
