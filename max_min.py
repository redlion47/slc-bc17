def find_max_min(T):
	maxi = 0
	b = list()
	if type(T) == list:#ensures the data type we get is a list

		for i in T:#loops around to find the largest number in our list
			if maxi < i:
				maxi = i

		mini = maxi

		for i in T:#checks the smallest number in a list
			if i< mini:
				mini = i

		if maxi == mini:#checks if the list has the same number
			b.append(len(T))

		else:# place the maximum and minimum in a list
			b.append(mini)
			b.append(maxi)

		return(b)
	else:
		return "error"



print(find_max_min([4,4]))