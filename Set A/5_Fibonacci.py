#Write a Python program to print the first 10 numbers of the Fibonacci series.
a=0
b=1
print("First 10 numbers of Fibonacci series are:")
print(a)
print(b)
for i in range(8):
    c=a+b
    a=b
    b=c
    print(c)

#Using while loop and upto n number
num=int(input("enter a number "))
a=0
b=1
print(f"Numbers of fibonacci series upto {num} are:")
print(a)
print(b)
while 1:
    c=a+b
    a=b
    b=c
    if c>num:
        break
    print(c)
