def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

a=900
print(factorial(a))