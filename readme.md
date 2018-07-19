## Python Exercises and Reference Guide

This is a set of Python exercises used to learn the language. These exercises were coded alongside [Colt Steele's Python course on Udemy](https://www.udemy.com/the-modern-python3-bootcamp/learn/v4/overview). All notes are based on the material learned in the course. 

### List Methods

A list is a Python data structure used to store a collection of items. Lists are ordered, iterable, and indexed. 

```
cities = ['Sacramento', 'Rocklin', 'Roseville']
```

**Append** is used to add an item to the end of a list and takes only one argument.

```
cities.append('Oakland')
```

**Extend** is used to add multiple items to the end of a list. It takes a list as an argument, adding the items individually. 

```
cities.extend(['San Francisco', 'Los Angeles', 'Riverside'])
```

**Insert** adds an item to the position you give it. This method takes two arguments; the first is the index number and the second is the item to be added. 

```
cities.insert(2, 'Lawndale')
```

**Clear** removes all items from a list and takes no arguments.

```
cities.clear()
```

**Pop** deletes the last item in a list if you provide it no argument. If you hand the method an argument, it will delete the item at that index.

```
cities.pop()
cities.pop(2)
```

**Remove** deletes the first item in a list wherein the value matches what you handed it. If the item is not found in the list, a ValueError will be thrown. This is useful in cases where you don't know the location of an item. 

```
cities.remove('Riverside')
```

**Index** returns the index number of the item you are searching for. You can provide one, two, or three arguments to this method. If you provide two arguments, the first argument will be searched for and the search will begin at the index position of the second argument. If provided a third argument, this will provide the ending index for the search.

```
cities.index('Sacramento', 0, 2)
```

**Count** returns the number of times that an item appears in a given list.

```
cities.count('Rocklin')
```

**Reverse** reverses the items in a list. Note that it does not make a duplicate, but replaces the original list. 

```
cities.reverse()
```

**Sort** will arrange the items alphabetically. 

```
cities.sort()
```

**Join** will convert a list to a string. You can specify how you would like the items in the list to be concatenated. 

```
', .join(cities)
```

### Dictionary Methods

A dictionary contains key value pairs. The keys describe the data and the values represent the data. Access values in a dictionary using the key. 

```
coffeeOrder = {
	'name': 'Falon',
	'drink': 'cold brew',
	'add_on': 'almond milk'
}

coffeeOrders['drink']
```
To access the keys, values, or items (keys and values), use the following built-in functions:

```
coffeeOrder.values()

coffeeOrder.keys()

coffeeOrder.items()
```
**Clear** deletes all the keys and values from a dictionary.

```
coffeeOrder.clear()
```
**Copy** makes a copy of a dictionary. This copy is stored in another part of memory. 

```
falonCoffeeOrder = coffeeOrder.copy()
```
**Fromkeys** is a method called on an empty dictionary that creates key value pairs from comma separated values. The values will all be set as the same. This is used to set default values oftentimes. 

```
newCoffeeOrder = {}.fromkeys(['name', 'drink', 'add_on'], None)
```
**Get**grabs the key in a dictionary. This is a good way to check if a key exists since it doesn't throw an error if the key doesn't exist. Instead, it returns None. Use this in conditional logic. 

```
coffeeOrder.get('drink')
```

**Pop** takes a key and deletes the corresponding key value pair. 

```
coffeeOrder.pop('add_on')
```

**Popitem** takes no arguments and removes a random key value pair from a dictionary.

```
coffeeOrder.popitem()
```

**Update** adds and replaces items in a dictionary.

```
coffeeOrder.update({'budget': 4.50})
```



