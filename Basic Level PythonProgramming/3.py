# 3. Write a Python program to count the number of vowels in a string.
def check_character():
    char = input("Enter a single character: ").lower()  # Convert to lowercase for easy comparison

    if len(char) != 1 or not char.isalpha():  # Ensure it's a single alphabetic character
        print("Invalid input! Please enter a single alphabetic character.")
        return

    if char in "aeiou":
        print(f"'{char}' is a Vowel.")
    else:
        print(f"'{char}' is a Consonant.")

# Run the function
check_character()
