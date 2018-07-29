# ask for a joke topic
# query icanhazdadjokes to get 1 relevant joke at random and print the number of results available
# if no jokes are available on that topic, notify them
import requests
from random import choice
from pyfiglet import figlet_format
from termcolor import colored

header = figlet_format("DAD JOKE 3000")
header = colored(header, color="magenta")
print(header)

print("What to hear a dad joke? Pick a topic.")

user_input = input()

url = "https://icanhazdadjoke.com/search"

response = requests.get(url, headers={"Accept": "application/json"}, params={"term": user_input}).json()

num_jokes = response["total_jokes"]
results = response["results"]

if num_jokes > 1:
	print(f"There are {num_jokes} jokes about the topic {user_input}.")
	print(choice(results)["joke"])
elif num_jokes == 1:
	print(f"There is one joke about the topic {user_input}.")
	print(results[0]["joke"])
else:
	print(f"There are no jokes about the topic {user_input}.")