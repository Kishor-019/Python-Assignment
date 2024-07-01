#Calling Module
import fact_module
num=int(input("Enter a positive number: "))

if num<0:
    print("There is no factorial for negative numbers.")

else:
    result=fact_module.factorial(num)
    print(f"Factorial of {num} is {result}")
