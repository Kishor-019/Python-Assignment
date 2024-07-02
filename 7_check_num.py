#Write a Python program that takes three numbers as input and checks if the third number is the
#sum of the first two numbers using logical operators
num1=int(input("Enter first number:"))
num2=int(input("Enter first number:"))
num3=int(input("Enter first number:"))

if num1+num2==num3 or num2+num1==num3:
    print("Third number is the sum of first and second number.")
else:
    print("Third number is not equals to the sum of first and seond number.")
