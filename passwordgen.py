import random
import re
letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
numbers = ["1","2","3","4","5","6","7","8","9"]
symbols = ["!","@","#","$","%","^","&","*","(",")","-","_","+","=","~"]
passlength = input("Password length:")

while isinstance(passlength, int) == False:
    try:
        passlength = int(passlength)
    except:
        passlength = input("Password length:")
passnumber = input("How many passwords do you want generated?")
while isinstance(passnumber, int) == False:
    try:
        passnumber = int(passnumber)
    except:
        passnumber = input("How many passwords do you want generated?")
def generate(paslength):
    global letters
    global numbers
    global symbols
    password = ""

    for x in range(2, paslength):
        charType = random.randint(0,2)
        if charType == 0:
            password = password + letters[random.randint(0, len(letters) -1 )]
            
        elif charType == 1:
            password = password + numbers[random.randint(0, len(numbers) - 1)]

        else:
            password = password + symbols[random.randint(0, len(symbols) - 1)]

    randomint = random.randint(0,len(password)-1)
    password = password[:randomint] + letters[random.randint(0,len(letters)-1)] + password[randomint:]
    randomint = random.randint(0,len(password)-1)
    password = password[:randomint] + numbers[random.randint(0,len(numbers)-1)] + password[randomint:]
    randomint = random.randint(0,len(password)-1)
    password = password[:randomint] + symbols[random.randint(0,len(symbols) -1)] + password[randomint:]
    return password
for x in range(0, passnumber):
    password = generate(passlength)
    print(password)


