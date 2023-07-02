def add(x , y = 2): #it will take the values given in below print commands even if give y=2 it don't take 
    total = x + y
    return total

print(add(5,6))
#print(add(x=5,y=2))
#print(add(5,y=2)) it's fine
#print(add(x=5,2)) if FIRST parameter have name, SECOND onwards should have name check with above case

print(1,2,3,4,5)
print(1,2,3,4,5, sep=" - ")


default_q = 3
def addition(p,q=default_q):
    addi = p + q
    print(addi)

addition(2)
default_q = 4 # even if change the default value q=4 function will store previous value the information
addition(2)