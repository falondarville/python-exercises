import requests

url = "https://icanhazdadjoke.com"

# use the header text/plain and it will display just the joke. Print using response.text
response = requests.get(url, headers={"Accept": "application/json"})

# this transforms the response into a Python dictionary. 
data = response.json()

# target the joke value of the dictionary
print(data['joke'])
# target the status value of the dictionary
print(f"status: {data['status']}")