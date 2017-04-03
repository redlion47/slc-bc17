def loan_func(A, T, R):
	rate = float(R)
	time = float(T)
	amount = float(A)
	
	loan_payable = (amount + (amount * (rate/100) * (time/12)))
	return loan_payable