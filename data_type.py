def data_type(x=""):
	if x == None :#checks if the input is equivalent to None 
		return "no value"

	elif x == '':#checks if the input is an empty string
		return "empty string"

	elif type(x) == str:#checks if the input is a string
		length = len(x)
		return length

	elif type(x) == bool:#checks if the input is a boolean value
		return x

	elif type(x) == int:#checks if the input is an integer
		if x<100:#is the number less than 100
			return "less than 100"

		elif x>100:#is the number greater than 100
			return "more than 100"

		elif x==100:#is the nuber 100
			return "equal to 100"

	elif type(x) == list:#is the input a list
		if len(x) >= 3:#does the input have 3 or more elements
			return x[2]

		else:
			return None
	else :#catches the exception when a different data type is input
		return "invalid type"

print(data_type())