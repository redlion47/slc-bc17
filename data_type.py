def data_type(x=""):
	if x == '':
		return "no value"

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

print(data_type(196))