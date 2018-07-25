# Note that I did not have to have a pipfile for this to work. I simply used the command: python3 pip -m install termcolor in my terminal
import termcolor
# to just use colored, you can also use: from termcolor import colored

text = termcolor.colored("HI THERE", color="white", on_color="on_magenta")
print(text)

# use help(termcolor) to see options, including colors available