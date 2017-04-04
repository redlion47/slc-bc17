"""def is_prime(x):
    if x > 1:
        n = x // 2
        for i in range(2, n + 1):
            if x % i == 0:
                print (i) 
        

print(is_prime(76))"""

def is_prime(n):
	for i in range(1,n + 1):
		for t in range(2,i+1):
			if (i % t) == 0:
				break
		else:
			print(i)

print(is_prime(19))