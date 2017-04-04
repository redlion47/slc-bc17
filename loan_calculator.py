def loan_func(A, T, R):

	if R>0 and R<=100 and T>0 and T<=12 and A>0:
		rate = R
		time = T
		amount = A

		loan_payable = (amount + (amount * (rate/100) * (time/12)))

		return loan_payable
	
print (loan_func(100000,12,12))
