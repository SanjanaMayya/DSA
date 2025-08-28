text = input("Enter a string :")
counts_vowels = 0
counts_consonants = 0
for char in text:
    if char.isalpha(): #Check if the character is a letter
        if char.lower() in "aeiou" : #Check if the character is a vowel
            print(f"{char} is a vowel")
            counts_vowels += 1
        else: #If it's not a vowel, it must be a consonant
            print(f"{char} is a consonant")
            counts_consonants += 1
    else:
        print(f"{char} is not a letter, skipping...")
print(f"Total vowels: {counts_vowels} and Total consonants: {counts_consonants}")