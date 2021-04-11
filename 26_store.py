import termcolor2


def read_from_database():
    try:
        product_list = []
        file = open("database.csv", "r")
        file_read = file.read()
        product = file_read.split("\n")
        for i in range(len(product)):
            split = product[i].split(",")
            product_list.append({"id": split[0], "name": split[1], "price": split[2], "count": split[3]})

    except Exception as e:
        print(e)
        product_list = []

    return product_list


product_list = read_from_database()


def show_menu():
    menu = ["1_Add New Product", "2_Search", "3_Edit", "4_Remove", "5_Buy", "6_Show_all", "7_Exit"]
    for item in menu:
        print(item)


def add_product():
    id = int(input("Enter Id: "))
    name = input("Enter Name: ")
    price = int(input("Enter Price: "))
    count = int(input("Enter count: "))
    product_list.append({"id": id, "name": name, "price": price, "count": count})


def search():
    print(termcolor2.colored("*Id*  Or  *Name*", color="blue"))
    user_search = input("Enter Choice: ")

    for product in product_list:
        if product["id"] == user_search or product["name"] == user_search:
            print(termcolor2.colored(f"Desired Product: {product}", color="green"))
            break
    else:
        print(termcolor2.colored("No Product", color="red"))


def edit():
    print(termcolor2.colored("Product_Id  Or  Product_Name", color="blue"))
    user_edit = input("Enter Choice: ")

    for product in product_list:
        if product["id"] == user_edit or product["name"] == user_edit:
            print(termcolor2.colored(f"Product: {product}", color="green"))
        user_product = input("Which Part To Edit? ")
        if user_product == "id":
            id = int(input("Enter New Id: "))
            product["id"] = id
            break
        elif user_product == "name":
            name = input("Enter New Name: ")
            product["name"] = name
            break
        elif user_product == "price":
            price = input("Enter New Price: ")
            product["price"] = price
            break
        elif user_product == "count":
            count = input("Enter New Count: ")
            product["count"] = count
            break
    else:
        print(termcolor2.colored("No Product", color="red"))


def remove():
    print(termcolor2.colored("Product_Id  Or  Product_Name", color="blue"))
    user_remove = input("Enter Choice: ")
    for product in product_list:
        if product["id"] == user_remove or product["name"] == user_remove:
            print(termcolor2.colored(f"Product: {product}", color="green"))
            product_list.remove(product)
            print(termcolor2.colored("Was Deleted", color="red"))
            break
    else:
        print(termcolor2.colored("No Product", color="red"))


def buy():
    print(termcolor2.colored("Product_Id  Or  Product_Name", color="blue"))
    user_remove = input("Enter Choice: ")
    for product in product_list:
        if product["id"] == user_remove or product["name"] == user_remove:
            print(termcolor2.colored(f"Product: {product}", color="green"))
            user_count = input("Enter Number: ")
            if product["count"] > user_count:
                result = int(product["count"]) - int(user_count)
                print(termcolor2.colored(f"Your Cart:Count {result}", color="green"))
                break
            else:
                print(termcolor2.colored("Count Not Enough", color="red"))
                break
    else:
        print(termcolor2.colored("No Product", color="red"))


def show_all():
    for product in product_list:
        print(product)


def all_exit():
    user_exit = input(termcolor2.colored("Do You Want The Information To Be Saved: ", color="blue"))
    if user_exit == "yes":
        file = open("database.csv", "a")
        for product in product_list:
            file.write(str(f"\n{product}"))
            exit()
    else:
        exit()


while True:
    show_menu()
    user = int(input("\nEnter Number: "))
    if user == 1:
        add_product()
    elif user == 2:
        search()
    elif user == 3:
        edit()
    elif user == 4:
        remove()
    elif user == 5:
        buy()
    elif user == 6:
        show_all()
    elif user == 7:
        all_exit()
