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

# make a pool of allowed characters
characters = (string.ascii_letters + string.digits
              + string.punctuation)

# start an empty string
password = ""

# repeat until it reach to number
for _ in range(length):
    #pick a random character
    #add character to string
    password += secrets.choice(characters)

# print string
print(password)