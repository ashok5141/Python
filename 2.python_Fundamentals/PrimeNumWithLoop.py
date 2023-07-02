for n in range(2,10):
    #print("First loop",n)
    for x in range(2,n):
        #print("Second loop",x)
        if n % x == 0:
            print(f"{n} equals {x}*{n//x}")
            break
    else:
        print(f"{n} is a prime number")