def is_anagram(str1,str2):
        return sorted(str1.lower()) == sorted(str2.lower())

# take user input

word1=input("Enter the first strings :").replace("","").lower()
word2=input("Enter the second input strings :").replace("","").lower()

# Check if they are anagrams


if is_anagram(word1,word2):
    print("The strings are anagrams.")
else:
    print("The strings are NOT anagrams.")
    