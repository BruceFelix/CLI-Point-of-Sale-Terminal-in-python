from customeroperations.customer import  user_json_file
from customeroperations.customer import  create_new_user
from productoperations.products import  products_json_file
from productoperations.products import  display_shoes
from productoperations.products import  goods_sold
from customeroperations.customer import goods_bought

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
    customer = input("Please enter your email: \n")
    index = check_user(customer)
    main_cart = []
    if check_user(customer):
        while True:
            display_shoes()
            buyer_choice = input("Which shoe do you want?\n")
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
        print(f"""
-------------------------------------------------
Customer Receipt
-------------------------------------------------
| Customer name: {users[int(index)]["name"]}
|           Products Bought
_________________________________________________
        """)
        print("""
| Product  Quantity     price        
        """)
        for i in main_cart:
            print(f"""
| {i[0]} - {i[1]}  : {i[2]}  each
            """)
        print("""
_________________________________________________            
            """)
        print(f"""
| Total purchase cost  : {total_cost}
        """)
    else:
        print("The is no such user kindly register them first.")
        create_new_user()
        print("Thank you for registering you may proceed.")
        # purchase_product()
