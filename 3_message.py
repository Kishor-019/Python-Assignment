age=int(input("Enter your age: "))

if age<0:
    print("Please enter a valid age.")
elif age<18:
    print("You are a minor.")
elif age >=18 and age<60:
    print("You are an adult.")
else:
    print("You are a senior.")
