# we want to create a function that counts 1-4 repeatedly. 

def current_beat():
	max = 100
	nums = (1, 2, 3, 4)
	i = 0
	result = []
	while len(result) < max:
		if i >= len(nums): i = 0
		result.append(nums[i])
		i += 1
	return result

print(current_beat())
