#Write a Python program to print a right-angled triangle of '*' with a given number of rows.
rows=int(input("Enter the number of rows:"))
for i in range(1,rows+1):
    for j in range(1,i+1):
        print("*",end="")
    print()

for i in range(1,rows+1):
    for j in range(1,i+1):
        print(j,end="")
    print()
