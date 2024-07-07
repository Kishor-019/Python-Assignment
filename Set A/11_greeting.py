#Write a Python function that takes a name and an optional age parameter and prints a greeting.
#f the age is not provided, it should default to 25
def gretting(name, age=25):
    print(f"Hi {name}, Your age is {age}.")


name=input("What is your name? ")
age=int(input("Enter your age: "))

gretting(name,age)
