# how to raise an error in your code
def colorize(text, color):
	# these are the colors accepted by the program
	colors = ("red", "blue", "green", "yellow")
	# keep the error messages apart so that the user will know more specifically where the issue is arising. 
	if type(color) is not str:
		raise TypeError("Color must be a string.")
	if type(text) is not str:
		raise TypeError("Text must be a string.")
	if color not in colors:
		raise ValueError("Color is not valid.")
	print(f"Printed {text} in {color}")

colorize("hi", "purple")
