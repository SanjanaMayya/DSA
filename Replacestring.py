text = input("Enter the original string: ")
old_sub = input("Enter the substring to replace: ")
new_sub = input("Enter the new substring: ")

# Replace old_sub with new_sub in text
replaced_text = text.replace(old_sub, new_sub)

print("Modified string:", replaced_text)