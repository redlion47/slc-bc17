def find_missing(list1, list2):
	if type(list1) == list and type(list2) == list:

		if len(list1) == 0 and len(list2) == 0:
			return 0

		else:
			for x in list1:
				list2.remove(x)
			
			if len(list2) == 0:
				return 0
			else:
				termin = list2[0]

				return termin

		
		#otpt = list.cmp(list1,list2)
		#print (otpt)


#print(find_missing([1, 2], [1, 2, 5,6]))