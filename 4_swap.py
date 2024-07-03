#Write a Python program to swap the values of two variables without using a third variable.
a=7
b=39

print(f'''Before swaping:
a={a}
b={b}''')

a=a+b
b=a-b
a=a-b

print(f'''After swaping:
a={a}
b={b}''')
