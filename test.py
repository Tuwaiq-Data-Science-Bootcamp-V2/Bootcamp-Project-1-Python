main_menu = "| Here is our avaliable services today: \n1. View today's baked goods\n2. Add to your cart\n3. Search for goods\n4. View your cart\n5. Checkout\n6. Exit"

VAT = 0.15

baked_goods = [
    ["cookies",11],
    ["chocolate cake",25],
    ["carrot cake", 25],
    ["apple pie", 20],
    ["mango tart", 20],
    ["dates tart", 20]
    ]

customer_cart = []

def print_menu(): # print the menu of the bakery
    print()
    print('------------ Our menu for today ------------')
    for index, item in enumerate(baked_goods): # for loop to go throgh the baked_goods list and print the items        
        print(index+1 ,"- ",item[0],": price ",item[1]," SAR")
    print('-------------------------------------------') 
    

def print_cart(): # print customer cart for checkout
    for item in customer_cart:
        print(item[0], 'Price: ',item[1],' SAR')
        

def add_to_cart(): # add to cart function to add items to cart
    item_code=-1
    while item_code != 0: # while loop to keep running until user enters 0 (back to main menu)
        # try except else block for user choice from baked goods menu
        try:
            print_menu()
            print("| Please enter the code for item you want to add (0 to back): ")
            item_code = int(input())
        except ValueError:
            print("Sorry invalid option please try again...")
            print()        
        else:
            if item_code == 0: # if the user enters 0
                print()
                break
            elif item_code >= len(baked_goods)+1: # if the user enters an item code bigger that the list size
                print("Sorry invalid option please try again...")
                print()

            else: # if the user enters valid item code
                add_answer="" 
                while add_answer !='n' or add_answer != 'N':
                    print("| Are you sure? [y/n]") # ask the user if he/she want to add the item
                    add_answer = input()
                    if add_answer == 'y' or add_answer=='Y': # if the user enter y or Y
                        for index, item in enumerate(baked_goods): 
                            if index+1 == item_code:
                                customer_cart.append([item[0],item[1]]) # add the item to custome cart list
                                print("Item added successfully...")
                                print()
                        break
                    elif add_answer =='n' or add_answer =='N': # if the user enter n  or N
                        break 
                    else: # if the user enter any other option
                        print("Sorry invalid option please try again...")
                        print()
            



calculate_total = lambda total: total * VAT # lambda function to calculate VAT amount 


def search_in_bakery(to_search):# search function to search about item
    item_count=0
    founded_items = [] # list to hold the founded items
    for item in baked_goods:
        if to_search in item[0]:
            item_count+=1
            founded_items.append([item[0],item[1]])
    if item_count == 0: # if there is no matching items
        print("!! No items founded...")
        print("Back to main menu...")
        print()
        return
    return founded_items # return the founded items list

# a Welcome logo for system
print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")
print("<>                      WELCOME TO SWEET & SUCH                           <>")
print("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>")

# start of while loop for the main menu
user_choice = 0
while user_choice != 6:

    # try except else block for user choice from main menu
    try:
        # ask the user to enter his choice form the main menu
        print(main_menu)
        print("| Please enter your choice: ")
        user_choice = int(input())


    except ValueError: # except when user enter string letters or symbols
        print("Sorry invalid option please try again...") 
        print()


    else: # if the user enter valid integer

        
        #START of choice 1
        if user_choice==1: # if the user choose 1 (view the menu)
            print_menu()

            answer="" 
            while answer !='n' or answer != 'N':
                print("| Would you like to add some to your cart? [y/n]") # to ask the user if he want to add items to his/her cart
                answer = input()
                if answer == 'y' or answer=='Y': # if the user enter y or Y
                    add_to_cart()
                    break
                elif answer =='n' or answer =='N': # if the user enter n or N
                    print("Back to main menu...")
                    break 
                else: # if the user enter any other options
                    print("Sorry invalid option please try again...")
                    print()
        #END of choice 1
        

        #START of choice 2
        elif user_choice == 2: # if the user choose 2 (add to cart)
            add_to_cart() # calling the add_to_cart function
        #END of choice 2
        

        #START of choice 3
        elif user_choice == 3: # if the user choose 3 (search for an item)
            print()
            print("| What would you like to search? ") # ask the user to enter the string or substring to search the items of list
            serached_item = input()
            founded_list = search_in_bakery(serached_item) # calling the search_in_bakery function to return any founded items
            if founded_list is not None: # if there is any items the match in the list
                print("Here are the goods that we could found: ")
                for item in founded_list:
                    print(item[0]," price: ", item[1], " SAR")
            print()
        #END of choice 3


        #START of choice 4
        elif user_choice == 4:# if the user choose 4 (view the cart)
            if len(customer_cart) == 0:
                print("You have no items in your cart yet...")
                print()
            else:
                print()
                print('---------- What you have so far -----------')
                print_cart() # calling the function to print customer cart
                print('-------------------------------------------')
                print()
        #START of choice 4



        #START of choice 5
        elif user_choice == 5:# if the user choose 5 (checkout)
            if len(customer_cart) == 0:
                print("You have no items in your cart yet...")
                print()
            else:
                print()
                print('-------------- Your invoice --------------')
                print_cart() # calling the function to print customer cart
                print('-------------------------------------------')
                # calculate the total of the items in the custome cart
                sum = 0 
                for item in customer_cart:
                    sum += item[1]
                
                # print the subtotal, VAT and grand total
                print("SubTotal is: ",sum)
                print("VAT: ",round(calculate_total(sum),2))
                print("GrandTotal is: ", sum+calculate_total(sum))
                print('-------------------------------------------')
                print()

                # ask the customer if he/she want to checkout
                answer_checkout="" 
                while answer_checkout !='n' or answer_checkout != 'N':
                    print("| Would you like checkout? [y/n]")
                    answer_checkout = input()
                    if answer_checkout == 'y' or answer_checkout=='Y':  # if the user enters y or Y
                        print("| Please provide your name for pick up time: ")
                        user_name = input()
                        print('-------------------------------------------')
                        print("Thank you ",user_name," for choosing Sweets and Such")
                        print("Please visit nearest bakery to pick up your order")
                        print("Have a nice day :)")
                        print('-------------------------------------------')
                        user_choice = 6
                        break
                    elif answer_checkout =='n' or answer_checkout =='N': # if the user enters n or N
                        print("Back to main menu...")
                        print()
                        break 
                    else: # if the user enters any other option
                        print("Sorry invalid option please try again...")
                        print()
        #END of choice 5


        #START of choice 6
        elif user_choice == 6: # if the  choose 6 (exit)
            print('-------------------------------------------')
            print("Thank you for choosing Sweets and Such")
            print("Have a nice day :)")
            print('-------------------------------------------')
            break
        #END of choice 6


        else: # if the user enters an option not avaliable on the menu 
            print("Sorry invalid option please try again...")
            print()

# end of the while loop for the main menu   