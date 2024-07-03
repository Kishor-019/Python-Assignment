#Write a Python program that takes two numbers as input and performs division, handling the
#case where the divisor is zero.
num1=int(input("Enter a number: "))
num2=int(input("ENter another number: "))

if num2<=0:
    print("Divisor should not be 0.")
else:
    print(f"{num1}/{num2} = {num1/num2}")
