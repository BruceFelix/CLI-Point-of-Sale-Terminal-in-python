# `CLI-Point-of-Sale-Terminal-in-python` #
## `SEPA Sprint 1` ##
A POS of system operated through the terminal
## Product Description ##
Create a command line driven point of sale terminal in Python.
The program's key features are:
  - Customers.
  - Products.
  - Purchases made by customers.
  
***GOAL OF THE PROGRAM***

Implement a python program that starts with a menu, gets user menu choice and proceeds to execute the subprogram associated with the menu.
The data will be stored in a json file.

# Final Product description
## Tools used
- Python
- Pycharm IDE
- Gmail
- JSON
## Main Menu
By running the main file the menu below is displayed.
![image](https://user-images.githubusercontent.com/44478872/197124400-d4787dbc-7873-4f6e-bf90-fa60b22ebaac.png)
Three operations will be displayed which the shop attendant can operate after login into the system.

## Customer operations
Customer operations include:
  1. To create New User.
  2. To delete User.
  3. To update User.
  4. To view users in the system.
  5. To search for a user in the system.
  
  Q. To return to the main program.
  

The following operations will be displayed in the customer menu.
![image](https://user-images.githubusercontent.com/44478872/197124790-e98d3753-ba82-4d0b-98da-96e6ed299392.png)

## Products operations
Products operations include:
  1. To create New product.
  2. To delete product.
  3. To update product.
  4. To view products in the system.
  5. To search a product in the system.
  
  Q. To return to the main program.
  
The following operations will be displayed in the products menu.
![image](https://user-images.githubusercontent.com/44478872/197125884-9180f160-420e-41fa-8645-9829b19f0a3d.png)

## Purchase product
This is the final operation of buying goods from the store.
![image](https://user-images.githubusercontent.com/44478872/197126172-e4ff2d48-dcb1-4701-9e06-c38ec280ea55.png)

### Required modules
- import pyfiglet - for banners
- from termcolor import colored - for colored texts
- from getpass import getpass - for hiding passwords while typing.
- from email.message import Emailmessage - for sending emails
- from twilio.rest import Client - for sending text messages
- import ssl - for connecting to the client email
- import smtplib 
- import re - for writing regex
- import json - for using json files
- import validate_email import validate_email - for email validation

# Product Setup
To run this program in your local machine, clone it to your local machine, install python and the required modules, then execute the following commands:

`$ git@github.com:BruceFelix/CLI-Point-of-Sale-Terminal-in-python.git`

`$ cd CLI-Point-of-Sale-Terminal-in-python`

`$ python main.py`
