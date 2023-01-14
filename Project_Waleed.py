
# Project Waleed Mohammed Almutairi


# * Use (lists) or dictionaries or tuples or sets. ---- here we use lists
ListCars = ['Camry 2019','Accsent 2020','Rosh 2021','Charger 2020','Accord 2018']
Listprice = [85000,38000,74000,95000,77000]


def SaleCar():

    print("Welcome to Sale Service!")
    print('-------------------------')
    InformationCars()
    print('_________________________________')

    # * Use loops
    while True:
        global Sale
        Sale = input("choose the number from list cars: ")
        # * Use at least 3 different data types. ---- here we use integer data type     # * Use conditions.
        if  Sale.isdigit() and int(Sale) <= len(ListCars) and int(Sale) != 0 :
            break


    print(InfoPerson())
    Correct = input("Are you sure you buy a/an {}? Yes:'y' , No:'n' ").format(ListCars[int(Sale)-1])
    # * Use conditions.
    if Correct == 'y' or Correct == 'Y':
        print("Thank you for buying the car!")
        # * Use a Lambda function.      # * Use at least 3 different data types. ---- here we use float data type
        priceing = lambda x: (x*15)/100
        result = priceing(Listprice[int(Sale)-1])
        print('_________________________________')
        print("Your buying car is {} ".format(ListCars[int(Sale)-1]))
        print("TAX is : {}".format(result))
        print("Total is : ", result+Listprice[int(Sale)-1])
        ListCars.remove(ListCars[int(Sale)-1])
        Listprice.remove(Listprice[int(Sale)-1])
    elif Correct == 'n' or Correct == 'N':
        print("Ok , good luck")
    else:
        print("Ops")


# * Use functions that return an output.
def InfoPerson()->str:

    # * Use loops.
    while True:
        # * Use at least 3 different data types. ---- here we use String data type
        Name = input("Enter your name : ")
        MobileNumber = input("Enter your Phone Number : ")
        Info = 'Name is: {} and phone Number is : {}'.format(Name,MobileNumber)

        # * Use conditions.
        if Name.isalpha() and MobileNumber.isdigit():
            return Info



def InformationCars():
    # * Use at least 3 different data types. ---- here we use integer data type
    i = 0
    # * Use loops.
    for item in ListCars:
        price = float(Listprice[i])
        i += 1
        print('{}-'.format(i), item,'and the price is {} '.format(price) )





def main():
    SaleCar()


if __name__ == '__main__':
    main()