# vowel or consonant
char = input("Enter a single alphabet: ").lower()
if char in 'aeiou':
    print(f"{char} is a vowel")
else:
    print(f"{char} is a consonant")
