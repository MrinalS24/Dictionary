Textbook = {
    "Math" : 170,
    "Chemistry" : 150,
    "Biology" : 230,
    "Physics" : 210,
    "SST" : 130
}

Textbook["Physics"] = 200


Textbook["Art"] = 80
Textbook["Music"] = 110


pbook = input('Which book do you want to know the price of? ')
if pbook in Textbook:
    print(Textbook[pbook])
else:
    print('Book does not exist.')


print(Textbook)

