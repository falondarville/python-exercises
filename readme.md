## Python Exercises

This is a set of Python exercises used to learn the language. These exercises were coded alongside Colt Steele's Python course on Udemy. 

### List Methods

Append is used to add an item to the end of a list and takes only one argument.

Extend is used to add multiple items to the end of a list. Hand items in a list, and the items will be added as individual items. 

Insert adds an item to the position you give it. This method takes two argument, the first is the index number and the second is the item to be added. 

Clear removes all items from a list and takes no arguments.

Pop deletes the last item in a list if you provide it no argument. If you hand the method an argument, it will delete the item at that index.

Remove deletes the first item in a list wherein the value matches what you handed it. If the item is not found in the list, a ValueError will be thrown. This is useful in cases where you don't know the location of an item. 

Index returns the index number of the item you are searching for. You can provide one, two, or three arguments to this method. If you provide two argument, the first argument will be searched for and the search will begin at the index position of the second argument. If provided a third argument, this will provide the ending index for the search.

Count returns the number of times that an item appears in a given list.

Reverse reverses the items in a list. Note that it does not make a duplicate, but replaces the original list. 

Sort will arrange the items alphabetically. 

Join will convert a list to a string. You can specify how you would like the items in the list to be concatenated. 

