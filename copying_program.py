# repeat all text until input = "stop copying me"
print("Hey how's it going?")
text = input()

# note the indendation on the print statement at the end. If the condition is met, print will run
while text != "stop copying me":
	print(text)
	text = input()
print("UGH FINE")