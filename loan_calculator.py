def loan_func(A, T, R):

	if R>0 and R<=100 and T>0 and T<=12 and A>0:#ensures that the values provided are within the stipulated limits
		rate = R
		time = T
		amount = A

		loan_payable = (amount + (amount * (rate/100) * (time/12)))#loan given plus the interest they accumulate in the given time

		return loan_payable
	
print (loan_func(100000,12,12))
