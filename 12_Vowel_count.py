#Write a Python program to count the number of vowels in a given string.
def vowCount(string):
    count=0
    for letter in string:
        if letter=='a' or letter=='e' or letter=='i' or letter=='o' or letter=='u':
            count+=1
    return count

string=input("Write a sentence:")
vowel=vowCount(string)
print(f"Total is/are {vowel} vowel letters in the sentence.")
