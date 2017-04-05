def words(line):
	t=list()

	if type(line)== str:#ensures that the input received is a string 
		"""if (x=="\n" for x in line ):
			break
		else:
			print (x)"""

		t = line.split()#splits the string into a list of the words
		
		dic = {i:t.count(i) for i in t} #counts each word and keeps it in a dictionary with its count

		print(dic)

	else:
		print("invalid input")


#words("¡Hola! ¿Qué tal? Привет!")

