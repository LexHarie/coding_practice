def factorial(n):
    if n == 1:
        return n
    else:
        n = n * factorial(n-1)
    return(n)

n = int(input("Please input an integer n: "))
print(factorial(n))