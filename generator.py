import string
import secrets
import time

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

# start with an empty pool
characters = ""
yes_no=("y", "yes", "n", "no")
yes_no_dict={}
count = 0

while True:
    try:
        letters = str(input("Include letter? (y/n) ")).lower()
        yes_no_dict["letters"] = letters
    except ValueError:
        print("Please enter yes or no! ")
        continue
    if letters not in yes_no:
        print("Please enter yes or no! ")
        continue
    break

if letters.startswith("y"):
    characters += string.ascii_letters

while True:
    try:
        digits = str(input("Include digits? (y/n) ")).lower()
        yes_no_dict["digits"] = digits
    except ValueError:
        print("Please enter yes or no! ")
        continue
    if digits not in yes_no:
        print("Please enter yes or no! ")
        continue
    break

if digits.startswith("y"):
    characters += string.digits

while True:
    try:
        symbols = str(input("Include symbols? (y/n) ")).lower()
        yes_no_dict["symbols"] = symbols
    except ValueError:
        print("Please enter yes or no! ")
        continue
    if symbols not in yes_no:
        print("Please enter yes or no! ")
        continue
    break

if symbols.startswith("y"):
    characters += string.punctuation


    for i in yes_no_dict.values():
        if yes_no_dict.values(0)=="n":
            count += 1
    if count == 3:
        print("Must contain one of symbol, digits, symbols. ")
        continue


# start an empty string
password = ""

# repeat until it reach to number
for _ in range(length):
    #pick a random character
    #add character to string
    password += secrets.choice(characters)

# print string
print(password)