# Write a program to write the longest word in a string.
text = input("Enter a string: ")
words = text.split()
longest_word = max(words, key=len)
print("The longest word is:", longest_word)
