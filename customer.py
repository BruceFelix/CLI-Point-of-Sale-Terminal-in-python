#imports
######################
import json


def new_customer():
    """
    Capturing user details
    """
    user = {}
    print("Kindly enter the details of the new customer: \n")
    user["name"] = input("Name: ")
    user["email"] = input("Email: ")
    user["number"] = input("Phone Number: ")
    user["products"] = 0
    user["expenditure"] = 0
    return user
def add_new_user(filename = "customer.json"):
    with open(filename) as file:
        data = json.load(file)
        temp = data["customers"]
        temp.append(new_customer())
    with open (filename, "w") as f:
        json.dump(data, f, indent=4)
