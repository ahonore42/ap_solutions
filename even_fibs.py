# Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
# By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed forty, 
# find the sum of the even-valued terms.

def even_fib_sum(n):
    # HELPER FUNCTION to solve for fibonacci numbers
    def fib(even_fib):
        # RECURSIVE FUNCTION for finding fibonacci numbers
        # BASE CASE for fibonacci sequence
        if even_fib < 0:
            return 0
        if even_fib == 1 or even_fib == 2:
            return 1
        # RECURSIVE CASE for fibonacci sequence, repeat until base case is met
        else:
            return fib(even_fib - 1) + fib(even_fib - 2)
            # return the fibonacci number of the integer passed into the function

    fib_sum = 0
    # Set an initial variable for the sum that we will mutate 

    for i in range(0, n, 2):
    # for every integer in the range of 0 to n (40 in this case)
    # iterate upward by a step of 2
        fib_sum += fib(i)
        # Add the fibonacci number of each integer to the sum
        print(fib_sum)
    return fib_sum
    # return the sum of all numbers in the range
        

print(even_fib_sum(40))