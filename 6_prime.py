num=int(input("Enter a positive non zero number: "))

if num<0:
    print("Enter a positive number.")
elif num==0 and num==1:
    print(f"{num} is not a prime number")

else:
    count=0
    for i in range(2,num//2+1):
        if num%i==0:
            count+=1
            break

    if count==0:
        print(f"The number({num}) is a prime number.")
    else:
        print(f"The number({num}) is not a prime number.")
