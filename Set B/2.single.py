#2.Given a non-empty array of integers nums, every element appears twice except for one. Find
#that single one.
def singleNum(nums):
    single_number=0
    for num in nums:
        single_number^=num
    return single_number

nums = [1,4,7,9,6,4,1,6,9]
print("The single number in the given list is:", singleNum(nums))
