sent = input('Enter a sentence for the vowel count: ')

vowel= {
    "a" : 0,
    "e" : 0,
    "i" : 0,
    "o" : 0,
    "u" : 0
}

for letter in sent:
    if letter in vowel:
        vowel[letter] += 1

print(vowel)

