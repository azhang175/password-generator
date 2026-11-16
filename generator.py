import string
import secrets

# print what is the password length?
# turn user answer into a number
length = int(input("What is the password length? "))

# make a pool of allowed characters
letters = string.ascii_letters

# start an empty string
password = ""

# repeat until it reach to number
for i in range(length):
    #pick a random letter
    letter = secrets.choice(letters)
#   add letter to string
    password += letter

# print string
print(password)