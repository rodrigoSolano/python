def binarysearch(array,n):
    inicio = 0
    final = len(array)-1
        
    while inicio <= final:
        medio = (inicio + final)//2
        if array[medio] == n:
            return "Elemento encontrado"
        elif array[medio] < n:
            inicio = medio + 1
        elif array[medio] > n:
            final = medio - 1
    return False

array = [1,2,3,4,5,6,7,8,9]
print(binarysearch(array,4)) 