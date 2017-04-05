def find_max_min(T):
	maxi = 0
	#mini = 0
	if type(T) == list:
		for i in T:
			if maxi < i:
				maxi = i
		mini = maxi
		for i in T:
			if i< mini:
				mini = i
		print(maxi, mini)
	else:
		return "error"



print(find_max_min([5,6,5,8,8]))