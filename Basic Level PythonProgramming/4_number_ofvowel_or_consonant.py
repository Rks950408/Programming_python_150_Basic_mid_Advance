# 4. Write a Python program to count the number of vowels in a string.
import re
def count_vowel(string):
    return (re.findall(r'[aeiouAEIOU]', string))
input_string=input("Enter the String ")
# count vowel and cosonents

vowel_count=count_vowel(input_string)

print(f"Number of vowels in the string: {vowel_count}")
# answerr
    # Enter the String python
# Number of vowels in the string: ['o']