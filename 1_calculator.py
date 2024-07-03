#Write a Python program that simulates a basic calculator, performing addition, subtraction,
#multiplication, and division.
choice=int(input('''Please select the operation:
1.Addition
2.Substraction
3.Multiplication
4.Division
'''))

if choice==1:
    num1=int(input("Enter the first number:"))
    num2=int(input("Enter the second number:"))
    print(f"Sum of the numbers ({num1}+{num2}) is ",num1+num2)

elif choice==2:
        num1=int(input("Enter the first number:"))
        num2=int(input("Enter the second number:"))
        print(f"Difference between the numbers ({num1}-{num2}) is", num1-num2)
elif choice == 3:
    num1=int(input("Enter the first number:"))
    num2=int(input("Enter the second number:"))
    print(f"Multiple of the numbers ({num1}x{num2}) is ",num1*num2)

elif choice == 4:
    num1=int(input("Enter the first number:"))
    num2=int(input("Enter the second non zero number:"))
    if num2==0:
            print("Please enter a non zero number.")
    else:
            print(f"Division of the numbers ({num1}/{num2}) is ",num1/num2)
else:
    print("Please select a valid option")
