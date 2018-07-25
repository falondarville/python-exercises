# ASCII art exercise
from pyfiglet import Figlet
from termcolor import colored

# use a tuple here because these colors will never change
valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")

print("What would you like to say?")
saying = input()
print("What color would you like to say it in?")
color = input()

if color not in valid_colors:
	color = "blue"

f = Figlet(font="big")
input_saying = f.renderText(saying)
styled_string = colored(input_saying, color)
print(styled_string)