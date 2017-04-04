def prime_no (n):
	if n>0: # Need to catch exception for negative numbers
		for i in range(1,n+1):
			for t in range(2,i): 
				if i%t==0:
					break
			else:
				print(i) # Need to create an empty list to append this numbers that happen to be primes
	#Use a return to return valie of the list of prime numbers detected

print (prime_no(15))
