#httprequest
import requests

url = "https://www.google.com"
response = requests.get(url)
print(f"Request to {response} status {response.status_code}")