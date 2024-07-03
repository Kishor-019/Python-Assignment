#Factorial Module
def factorial(a):
    factorial=1
    while a>1:
        factorial*=a
        a-=1
    return factorial
