#Write a Python function that takes a list of numbers and returns the maximum value in the list.
def maxNum(numbers):
    if not numbers:
        print("The list is empty.")
    max=numbers[0]
    for num in numbers:
        if num>max:
            max=num
    return max

num_list=[6,9,5,3,7,11,54,32,4,46]
max_num=maxNum(num_list)
print("Maximum number is ",max_num)
