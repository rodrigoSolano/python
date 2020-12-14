def min_sum(arr):
	result = list()
	arr.sort()
	while len(arr) != 0:
		result.append(min(arr)*max(arr))
		print(arr)
		arr.pop()
		arr.pop(0)
	return sum(result)



print(min_sum([12,6,10,26,3,24]))