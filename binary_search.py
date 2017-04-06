class BinarySearch(list):
	"""docstring for BinarySearch"""
	
	def __init__(self, a, b):
		self.leng = 0
		self.start = b
		self.end = a
		#self.lst = list()
		#lst= list()

		for x in range(self.leng,a):#loop four to create a list with steps b and length a
			self.append(self.start)
			self.start += b#increase the number to be entered next by b
			#self.leng += 1#

		#self.lst = lst

		"""while self.leng < a:#loop one to create a list with steps b and length a
			self.append(self.start)
			self.start += b
			self.leng += 1#increase the length of the list to reach the required length

		while self.leng < a:#loop two to create a list with steps b and length a
			if self[self.leng] == None:
				self.append(self.start)
				self.start += b
			else:
				self.leng += 1

		if self.lst[self.leng] == None:#loop three to create a list with steps b and length a
			self.leng.append(self.start)
			self.start += b
		else:
			self.leng += 1"""

		self.length = len(self) #initialize the length of the list produced
		#print(self)

	def search(self, x):
		strt = 0 
		end = self.length - 1
		count = 0
		while strt <= end:#the binary search algorithm
			cntre = (strt + end) //2#find the centre of the list
			"""if x>(self.start * self.end) or x % self.start != 0:
				return dict(index = -1, count = count)
			el"""
			"""if x not in range(self.start,(self.start*self.end)+1):
				return dict(index = -1, count = count)"""

			if self[cntre] == x:#is the centre element the target element
				#print(count)
				return dict(index = cntre, count = count)#returns the index of the target and the number of times it took to find it
			elif self[cntre] < x:#if the target is larger than the centre element remove the left of the list
				strt = cntre + 1
			else:#if the target is smaller than the centre element remove the right side of the list
				end = cntre - 1 
		count +=1#number of times the loop is executed to find the target
			
		
"""obje = BinarySearch(100, 10)
print(obje)
print(obje.search(10000))
ser = obje.search(10000)
print(ser['count'])"""