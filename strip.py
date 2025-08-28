text = "  hello world  "
text_original = text
# Remove spaces from a string
cleaned_text = text.strip().replace(" ", "") # Remove leading/trailing whitespace and spaces in between 
print("String with spaces : ", text_original)
print("String without spaces: ", cleaned_text)