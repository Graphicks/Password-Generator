import random
import string # Package that contains all ascii letters

print("Welcome to Password Generator!\n\n")

# Variables 
lengthOfPassword = int(input("How long would like the password to be?   \n\n")) 

lowerCase = string.ascii_lowercase # All ascii lowercase characters
upperCase = string.ascii_uppercase # All ascii uppercase characters
numbers = string.digits # All ascii numbers
symbols = string.punctuation # All ascii puntucation

allCharacters = lowerCase + upperCase + numbers + symbols # combines all of these characters together

# Functions 

def generate_password(allCharacters, lengthofPassword):
    temp = random.sample(allCharacters, lengthOfPassword) # Random sample of all the characters
    password = ''.join(temp) # Joins these characters together 
    return password 

print(generate_password(allCharacters, lengthOfPassword))