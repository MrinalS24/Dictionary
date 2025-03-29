Un_pw = {
    "Mrinal" : '1234',
    "Aadya" : '2345',
    "Saimeera" : '3456',
    "Shreya" : '4567',
    "Samanga" : '5678',
    "Hiranya" : '6789',
    "Sanika" : '7890',
    "Aarna" : '9876',
    "Tanisha" : '8765',
    "Varshitha" : '7654'
}

User = input('What is your username?  ')

if User in Un_pw:
    Pass = input('What is your password?  ')
    if Pass in Un_pw[User]:
        print('You are now logged into the system')
    else:
        print('Incorrect password')

else:
    print('Not a valid user of this system')