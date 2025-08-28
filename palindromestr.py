text = input("Enter a string: ")
# Remove spaces and convert to lowercase for accurate palindrome check
cleaned_text = text.replace(" " , "").lower()

if cleaned_text == cleaned_text[::-1]:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
