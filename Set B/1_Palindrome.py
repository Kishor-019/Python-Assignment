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
