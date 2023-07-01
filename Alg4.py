#Двоичное представление

#def dual(x):
#    if x < 2:
#        print(x, end = '') 
        
#    else:      
#        dual(x // 2)
#        print(x % 2, end = '')    

#dual(13)
#print("")
#print("")





# Умножение

#def mult(x, y):
#    while y > 0:
#        return (x + mult(x, y -1))
#    else:
#        return 0
        
#print(mult(3, 22))





# Возведение в степень

def pow(x, y):
    while y > 0:
        return (x * pow(x, y - 1))
    else:
        return 1

print(pow(698, 9))