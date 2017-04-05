def fizz_buzz(n):
	if n%3 == 0 and n%5 == 0 :#checks if the number is divisible by 3 and 5
		return "FizzBuzz"

	else:
		if n%3 == 0 :#checks if the number is divisible by 3
			return "Fizz"

		elif n%5 == 0 :#checks if the number is divisible by 5
			return "Buzz"

		else:
			return n #if not divisible by any return number

print(fizz_buzz(90))