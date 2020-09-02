#The vowels/las vocales
letter = input("Enter a letter: ")
if len(letter)!=1:
    print("Just one letter")
elif letter.lower() in "aeiou":
    print("It's vowel")

