def prime_no (n):
	if n>0:
		for i in range(1,n+1):
			for t in range(2,i):
				if i%t==0:
					break
			else:
				print(i)

print (prime_no(15))
