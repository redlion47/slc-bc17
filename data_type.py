def data_type(x=""):
	if x == None :
		return "no value"

	elif x == '':
		return "empty string"

	elif type(x) == str:
		length = len(x)
		return length

	elif type(x) == bool:
		return x

	elif type(x) == int:
		if x<100:
			return "less than 100"

		elif x>100:
			return "more than 100"

		elif x==100:
			return "equal to 100"

	elif type(x) == list:
		if len(x) >= 3:
			return x[2]

		else:
			return None
	else :
		return "invalid type"

print(data_type())