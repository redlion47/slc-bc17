def prime_no (n):
	a = list()
	
	if type(n) is not int or n == '':
		return "invalid entry"

	if n<0:
		return "invalid input"

	if n==0 or n==1:
		return n," is not a prime number"

	if n>1:#ensure the number is not a negative and it is greater than zero
		for i in range(2,n+1):#get a list of all the numbers from 2 to my number
			for t in range(2,i):#check if each number is a prime number in my list
				if i%t==0:
					break
			else:#place the prime numbers in a list
				a.append(i)
	return a

print (prime_no(9))
