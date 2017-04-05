class Car:
	
	def __init__(self, car_name= "General", car_model ="GM", car_type = None): #initializing the car properties
		self.name = car_name
		self.model = car_model
		self.type = car_type
		self.speed = 0

		if self.type == "trailer":#the loop that determines the number of wheels each car possesses
			self.num_of_wheels = 8
		else:
			self.num_of_wheels = 4

		if car_name == "Porshe" or car_name == "Koenigsegg":#the loop determines the number of doors each car has
			self.num_of_doors = 2
		else:
			self.num_of_doors = 4

	def is_saloon(self):#is the car a saloon or not
		if self.type != "trailer":
			car_type = "saloon"
		else:
			car_type = "trailer"

		return car_type

	def drive(self, n):#when the car is in drive mode
	#initializing constant speeds within the car's property
		if n == 7:
			self.speed = 77
		elif n== 3:
			self.speed = 1000

		return self

