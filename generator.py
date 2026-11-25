import string
import secrets
import time

#Filter out all other words
yes_no=("y", "yes", "n", "no")

#Function to ask the user if they want to include a certain character type in the password
def choosing_characters(character):
    while True:
            try:
                character = str(input("Include" + character + "? (y/n) ")).lower().strip()
            except ValueError:
                print("Please enter yes or no! ")
                continue
            if character not in yes_no:
                print("Please enter yes or no! ")
                continue
            break
    return character


#Ask the user for the input until they enter a whole
# number greater than 0
while True:
    try:
        length = int(input("What is the password length? "))
    except ValueError:
        print("Please enter a number!")
        #for readability in the console
        time.sleep(1)
        continue
    if length <= 0:
        print("Please enter a number greater than 0.")
        time.sleep(1)
        continue
    break

#Determine which characters are to be included in the password
while True:
    characters = ""
    letters = choosing_characters("letters")
    digits = choosing_characters("digits")
    symbols = choosing_characters("symbols")
    
    if letters.startswith("y"):
        characters += string.ascii_letters

    if digits.startswith("y"):
        characters += string.digits

    if symbols.startswith("y"):
        characters += string.punctuation

    if len(characters) == 0:
        print("Please select at least one character type! ")
        continue
    break

# start an empty string
password = ""

# repeat until it reach to number
for _ in range(length):
    #pick a random character
    #add character to string
    password += secrets.choice(characters)

# print string
print(password)