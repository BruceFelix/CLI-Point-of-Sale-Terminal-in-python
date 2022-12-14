from customeroperations.customer import create_new_user
from customeroperations.customer import goods_bought
from customeroperations.customer import user_json_file
from productoperations.products import display_shoes
from productoperations.products import goods_sold
from productoperations.products import products_json_file
from email.message import EmailMessage
from termcolor import colored
from twilio.rest import Client
import ssl
import smtplib

SID = "***************************"
Auth_Token = "********************************"
email_sender = "johndoe@gmail.com"
email_password = "***********"
email_receiver = "janedoe@gmail.com"
msg_body = "Receipt from Bruce's Luku shoe shop.\n\n"


def check_user(customer):
    """
    Checks if a user exist or not.
    """
    users = user_json_file()
    # print(users)
    for (index, entry) in enumerate(users):
        if customer == entry["email"]:  # remember to use users input
            return str(index)
        else:
            continue
    return False


def purchase_product():
    """
    Function used to purchase product.
    """
    users = user_json_file()
    shoes = products_json_file()
    print(colored("Remember to smile at the customer.", "green"))
    customer = input("Please enter the customer's email: \n")
    index = check_user(customer)
    main_cart = []
    if check_user(customer):
        while True:
            display_shoes()
            buyer_choice = input("\nWhich shoe do you want?\n")
            pairs = input("How many pairs do you need?\n")
            cart = [shoes[int(buyer_choice)]["name"], int(pairs), shoes[int(buyer_choice)]["price"],
                    int(pairs) * int(shoes[int(buyer_choice)]["price"])]
            main_cart.append(cart)
            print("Do you want to continue shopping? ")
            print("* yes ")
            print("* no ")
            user_choice = input("")
            if user_choice.lower() == "yes":
                continue
            elif user_choice.lower() == "no":
                break
            else:
                print("Please choose valid answer.")
        total_cost = 0
        for i in main_cart:
            total_cost += i[3]
        goods_sold(cart[0], cart[1])
        goods_bought(cart[1], total_cost, users[int(index)]["email"])
        the_join = ''.join([f"{i[0]}  -  {i[1]}  : {i[2]}  each\n" for i in main_cart])

        receipt = f"""
Customer Receipt
_________________________________________________
Customer name: {users[int(index)]["name"]}
_________________________________________________
Product   Quantity     price   
_________________________________________________   
{the_join}         
Total purchase cost  : {total_cost}
_________________________________________________   
Thank you for shopping with us.
        """

        print(receipt)
        recipient = input("Do you want the receipt to be sent to your email:\n ")
        if recipient.lower() == "yes":
            send_receipt_mail(receipt)
        # elif recipient.lower() == "sms":
        #     send_receipt_message(receipt)
        # print(colored("Transactions complete. Remember to thank them as you hand them the receipt :) ", "green"))

    else:
        print("The is no such user kindly register them first.")
        create_new_user()
        print("Thank you for registering you may proceed.")


def send_receipt_mail(receipt):
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_sender
    em['subject'] = email_sender
    em.set_content(msg_body + receipt)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())


# def send_receipt_message(receipt):
#     body = msg_body + receipt
#     cl = Client(SID, Auth_Token)
#     cl.messages.create(body=msg_body + receipt, from_="+13464822642", to="+254792743861")
#

