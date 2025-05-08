"""
Data Structures
Student Project
Project Title:
"""

import random
import requests
import pp

based_url = "https://randomuser.me/api/"
response = requests.get(based_url)
body = response.json()


#This list is for using a random name for the users email#
#security = ["user", "oval", "deer", "pop", "code", "vail", "match", "fold"]

#This list is to use a random email address for extra security#
address = ["@gmail.com", "@yahoo.com", "@outlook.com", "@icloud.com", "@proton.me"]

#This list is for the password that the user uses for their email#
passworded = ["doe2025", "create123456", "jalmo963842", "student246810", "coder987654"]

#User creates their email with the decision to use a name from a list or custom one#
creation = input("Create a secure email, would you like to use the security email or create your own? Type yes to use security email. ")

#User is a name for their email at random#
if creation == "yes":
    #creation = creation.replace(creation, random.choice(security))
    body = response.json()
    creation = body["results"][0]["login"]["username"]
#User inputs a custom name for their email#
while creation == "":
    creation = input("Enter a name that can be used for the email...")

#Gives a random number that can be used alongside the email#
if creation.isalpha():
    creation += str(random.randint(1, 999))

#Uses a random email address for more security#
creation += random.choice(address)

#Added the email to the list#
address.append(creation)

#Email is fully created and added to the list to use#
print("Here is your new email, name is " + creation)

#User creates a custom password of their choice#
custom = input("Add a custom password to use for the new email. ")

#Letting the user know that their user and password are linked#
print("User and password linked successfully!")

#Add the custom password to the list#
passworded.append(custom)

print("Sign in with your email address and password")

#This is to check whether the email and passowrd is equal#
while True:
    email = input("Enter your email address. ")
    password = input("Enter your password for your email. ")
    if email in address and password in passworded:
        index = address.index(email)
        if passworded[index] == password:
            print("You have saved your email and password.")
            break

    #This is to say that the email is not connected to the password, the user will have to try again#
    print("Your email is not linked to your password, please try again...")
    continue

