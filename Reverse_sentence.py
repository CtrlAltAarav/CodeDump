# reverse_words.py
sentence = input("Enter a sentence: ")
words = sentence.split()
reversed_sentence = ' '.join(reversed(words))
print("Reversed Sentence:", reversed_sentence)
