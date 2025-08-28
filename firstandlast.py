# Write a program in a such way that first and last character should be displayed
text = "Hello World!"
check_variable = text.find("World")
print("Checking whether 'World' is present in the string:", check_variable)
if text.startswith("H") and text.endswith("!"):
    print("The string starts with 'H' and ends with '!'")
else:
    print("The string does not start with 'H' or does not end with '!'")
    
print("First character:", text[0], "Last character:", text[-1])
