import requests
import os
from dotenv import load_dotenv
from send_email import send_email

load_dotenv()
api_key = os.getenv('API_KEY')
topic = "tesla"

# make a request
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "sortBy=publishedAt&" \
      f"apiKey={api_key}&" \
      "language=en"

# Make the request
request = requests.get(url)

# Get the contents
content = request.json()

# print titles
body = "test"
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" \
               + article["description"] + "\n" \
               + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)
