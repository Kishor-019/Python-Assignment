#Given an integer x, return true if x is a palindrome, and false otherwise.
print("First method")
num=int(input("Enter a number "))
count=0
temp=num
original=num
while 1:
    num=num//10
    count+=1
    if num==0:
        break
rnum=0
while 1:
    r=temp%10
    temp=temp//10
    rnum=rnum+r*(10**(count-1))
    count-=1
    if temp==0:
        break

if original==rnum:
    print("The given number is palindrome number.")
else:
    print("The given number is not a palindrome number.")

#OR
print("Second method")
def palindrome(num):
    num_str=str(num)

    return num_str==num_str[::-1]

number=int(input("Enter a number:"))
if palindrome(number):
    print(f"The number({number}) is palindrome.")
else:
    print(f"The number({number}) is not palindrome.")
