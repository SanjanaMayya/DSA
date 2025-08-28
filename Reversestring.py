text = input("Enter a string to be reversed:")
"""reversed_text = text[::-1] #Reversing the string using slicing
print(f"Original string: {text}")
print(f"Reversed string: {reversed_text}")"""

reversed_string = reversed(text) #Using the reversed function
print("Reversed string using reversed function :", ''.join(reversed_string))