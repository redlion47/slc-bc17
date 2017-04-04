class User_Input:
    def __init__(self):
    	num1 = input("Enter your first number here:==>  \n")
    	num2 = input("Enter your second number here:==>  \n")
    	print(":select from the list below a letter of what you would like done to the numbers above")
    	print("A - Addition")
    	print("B - Subtraction")
    	print("C - Multiplication")
    	print("D - Division")
    	operator = input("your selection please ==>  \n")
    	Calc(num1,num2,operator)
    	main(operator)

class Calc(User_Input):
	"""docstring for Calc"""
	def __init__(self,num1,num2,operator):
		self.num1 = num1
		self.num2 = num2
		self.operator = operator
		main(self.operator)

	def Addition(self):
		sum1 = self.num1 + self.num2
		return sum1

	def Subtraction(self):
		diff = self.num1 - self.num2
		return diff

	def Multiplication(self):
		prod = self.num1 * self.num2
		return prod

	def Division(self):
		div = self.num1 / self.num2
		return div
		
class main(User_Input):
	"""docstring for main"""
	def __init__(self,operator):
		self.operator = operator

	def calculate(self):
		if self.operator == "A":
			T = Calc().Addition()
			return T
                
User_Input()
