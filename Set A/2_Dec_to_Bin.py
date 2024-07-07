#Write a Python program that converts a given decimal number to its binary equivalent.
def dec_to_bin(n):
    binary=""
    while n > 0:
        binary=str(n%2)+binary
        n=n//2
    return binary

num=int(input("Enter a decimal number: "))

if num==0:
    print("Binary: 0")
elif num==1:
    print("Binary: 1")
else:
    binary=dec_to_bin(num)
    print("Binary:", binary)
