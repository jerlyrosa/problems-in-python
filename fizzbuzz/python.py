# The FizzBuzz problem is a classic test given in coding interviews. The task is simple:

# Print integers 1 to N, but print “Fizz” if an integer is divisible by 3, “Buzz” if an integer is divisible by 5, and “FizzBuzz” if an integer is divisible by both 3 and 5.


def FizzBuzz(n):
    for fizzbuzz in n:
        if(fizzbuzz % 15 == 0): print("FizzBuzz")
        elif(fizzbuzz % 5 == 0 ): print("Fizz")
        elif(fizzbuzz % 3 == 0 ): print("Buzz")
        else: print(fizzbuzz)
FizzBuzz(range(100))
