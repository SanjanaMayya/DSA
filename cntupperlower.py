# Write a program to count uppercase, lowercase, digits and special characters in a string.
text = input("Enter a string: ")
# Initialize counters
upper_count = 0
lower_count = 0
digit_count = 0
special_count = 0
# Iterate through each character in the string
for char in text:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1
    elif char.isdigit():
        digit_count += 1
    else:
        special_count += 1
# Print the counts
print(f"Uppercase characters: {upper_count}")
print(f"Lowercase characters: {lower_count}")
print(f"Digits: {digit_count}")
print(f"Special characters: {special_count}")