#Example 9: Python program that accepts a word from the user and reverses it.

word=str(input("Enter the word:"))
reversed_word=""
for i in word:
    reversed_word=i+reversed_word
print("Reverse of given word:",reversed_word)