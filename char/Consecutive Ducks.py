def consecutive_ducks(n):
	if n % 2 != 0:
		number = int(n/2)
		if (number + (number+1) ) == n:
			print(n)
			print(f"{number} + {number+1} = {number+number+1}")
			return True  
	else:
		resuk = list()
		limit = int(n / 2) 




	return n in resuk			
def sum_a_from_b(start,end):
	gauss = ( (1 + end) / 2 ) * end
	gauss_2 = ( ( (1 + start ) / 2 ) * start ) 
	return gauss - gauss_2 + start


print(sum_a_from_b(205,210))