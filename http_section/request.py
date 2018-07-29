import requests

# note that http must always be included in the url
url = "http://www.google.com"
response = requests.get(url)

print(f"Your request to {url} came back with status code {response.status_code}")
