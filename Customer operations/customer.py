#imports
######################
from unicodedata import name
import json

#Global variables
##############

class Customer:
    def __init__(self, id , name, email, number, prods_bought, expenditure ):
        self.name = name
        self.id = id
        self.email = email
        self.number = number 
        self.prods_bought = prods_bought
        self.expenditure = expenditure
    


def new_customer():
    """
    Capturing user details
    """
    print("Kindly enter the details of the new customer: \n")
    name = input("Name: ")
    email = input("Email: ")
    number = input("Phone Number: ")

    new_user = Customer(name,email,number)


def inserting_new_user():
    def appending_user(data, filename = "customer.json"):
        with open (filename, "a") as f:
            json.dump(data, f, indent=4)

with open("customer.json", "r") as f:
    data = json.load(f)

print(data)