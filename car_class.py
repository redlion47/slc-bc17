class Car:
	
	def __init__(self, car_name= "General", car_model ="GM", car_type = None):
		self.name = car_name
		self.model = car_model
		self.type = car_type
		self.speed = 0

		if self.type == "trailer":
			self.num_of_wheels = 8
		else:
			self.num_of_wheels = 4

		if car_name == "Porshe" or car_name == "Koenigsegg":
			self.num_of_doors = 2
		else:
			self.num_of_doors = 4

	def is_saloon(self):
		if self.type != "trailer":
			car_type = "saloon"
		else:
			car_type = "trailer"

		return car_type

	def drive(self, n):
		if n == 7:
			self.speed = 77
		elif n== 3:
			self.speed = 1000

		return self


"""tr = car("toyota")
tr.display()"""
		