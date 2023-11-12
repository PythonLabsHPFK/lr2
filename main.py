import random

word = input("Введіть своє слово: ")
shift = int(input("Введіть сдвиг: "))

text = ""
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for char in word:
    index_alphabe = alphabet.index(char.lower())
    index_alphabet_ne = index_alphabe + shift
    if index_alphabet_ne > 25:
        index_alphabet_ne -= 25
    text += alphabet[index_alphabet_ne]

print(text)

output = ""
i = 0

while output != word:
    output = ""
    for char in text:
        index_alphabet = alphabet.index(char.lower())
        index_alphabet_new = index_alphabet - i
        if index_alphabet_new < 0:
            index_alphabet_new -= 1
        output += alphabet[index_alphabet_new]
    print("Guess:", output)
    i += 1
