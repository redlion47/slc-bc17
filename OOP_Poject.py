class User_Input:
    def __init__(self):#initializing the class User_Input to get user input
    	num1 = int(input("Enter your first number here:==>  \n"))#takes in the first number
    	num2 = int(input("Enter your second number here:==>  \n"))#takes in the second number
    	print(":select from the list below a letter of what you would like done to the numbers above")#where the user is to select the required action
    	print("A - Addition")
    	print("B - Subtraction")
    	print("C - Multiplication")
    	print("D - Division")
    	operator = input("your selection please ==>  \n")#takes the choice of the user on how the numbers will be executed
    	Calc(num1,num2,operator)#calls the Calc class
    	main(operator)#calls the main class

class Calc(User_Input):#the class is meant to enable the calculations required to be executed for the given numbers
	"""docstring for Calc"""
	def __init__(self,num1,num2,operator):
		self.num1 = num1
		self.num2 = num2
		self.operator = operator
		main(self.operator)

	def Addition(self):#function called to add the numbers given by the user
		sum1 = self.num1 + self.num2
		return sum1

	def Subtraction(self):#finds the diffeerence of thee numbers
		diff = self.num1 - self.num2
		return diff

	def Multiplication(self):#finds the product of the numbers
		prod = self.num1 * self.num2
		return prod

	def Division(self):#divide the numbers together
		div = self.num1 / self.num2
		return div
		
class main(User_Input):#the clas that determines what the user has selected to happen to the numbers
	"""docstring for main"""
	def __init__(self,operator):
		self.operator = operator

	def calculate(self):
		if self.operator == "A":
			T = Calc().Addition()
			return T
                
User_Input()
