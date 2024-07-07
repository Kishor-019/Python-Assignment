#Write a Python program that prints a multiplication table up to (numberx10).
num=int(input("Enter a number: "))

for i in range(1,11):
    print(f"{num} * {i} = {num * i}")
