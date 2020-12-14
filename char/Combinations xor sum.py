import itertools
from math import factorial

def transform(A, x):
    mapa = list()
    suma = 0
    for element in A:
        mapa.append([element,x])
    
    for pair in mapa:
    	n = pair[0]
    	x = pair[1]
    	sum_com = sum_combinations(n,x)
    	suma = int(suma) ^ int(sum_com)

    return suma

def sum_combinations(n,x):
    suma = 0
    for i in range(x,n+1):
    	com = combination(i,x)
    	#print(f"n:{i} y x:{x}")
    	suma += com
    return suma

def combination(n,x):
	combination = factorial(n) / (factorial(x) * factorial(n-x))
	return combination


print(transform([1000, 60, 132, 998, 47], 1))

