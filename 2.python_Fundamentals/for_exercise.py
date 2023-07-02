'''
print 1 to 100 (including 100)
But instead of printing multiples of 3, print fizz
Instead of printing multiples 5, print buzz
Instead of printing multiples of both 3 and 5 FizzBuzz'''
for n in range(1,101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 ==0:
        print("Buzz")
    else:
        print(n)