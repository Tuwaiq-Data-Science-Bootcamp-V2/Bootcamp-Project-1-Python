
# import date & time to print them in the bill
import datetime 
now = datetime.datetime.now()

# Dictionary for service used two data types: String & Numeric
salonServices = [{'name': 'Brid Makeup', 'price': 150.00 },
    {'name': 'Over Makeup', 'price': 90.00},
    {'name': 'Natural Makeup', 'price':60.00},
    {'name': 'HairStyel', 'price': 77.00},
    {'name': 'Nails', 'price': 15.00},]
    
# Start a loop to avoid empty input , the loop will run until the user give input
while True:
    firstName = input('Please Enter Your First name to exist:')
    secondName = input(' Enter Your second name to exist: ')
    if firstName and secondName != '':
        break 

#Functions that return full name
def name (firstName , secondName):
    result = ' ' +firstName + ' ' + secondName
    return result

print(name(firstName , secondName),'Welcome to the online Beauty Salon!\n These are the avaliable services that we offer:\n')

#Functions to display the services in order
def displayServices(salonServices):
    for i, item in enumerate(salonServices):
        print(f"{i+1}. {item['name']} - ${item['price']}")

# initialize variables
anotherServices = 1
totalCost, total = 0, 0

# while loop used for many goals  
while anotherServices != 0:
    # call displayServices function to book & ask for number of customers & calculate the total
    displayServices(salonServices)
    option = int(input('Which service would you like to book ?: '))
    if option == 1:
            customersNum = int(input('Enter How many customers do you have?'))
            total = customersNum * 150.00
    elif option == 2:
            customersNum = int(input('Enter How many customers do you have?'))
            total = customersNum * 90.00
            print('The price is: ' + str(total))
    elif option == 3:
            customersNum = int(input('Enter How many customers do you have?'))
            total = customersNum * 60.00
            print('The price is: '  + str(total))
    elif option == 4:
            customersNum = int(input('Enter How many customers do you have?'))
            total = customersNum * 77.00
            print('The price is: '  + str(total))
    elif option == 5:
            customersNum = int(input('Enter How many customers do you have?'))
            total = customersNum * 15.00
            print('The price is: '  + str(total))
     #to cuse error if the user enter input invalid      
    elif len(t)>1 or len(t)<1:
        print('This is invalid number')
       
    #totalCost increment 
    totalCost += total
    #Lis for time available 
    time = ['2:00','2:30','3:00','3:30','4:00','4:30','5:00','5:30','6:00']
    print('Time available :')
    #for loop to display all the timw
    for values in time:
        print(values)
    t = int(input('Please enter the  time that you perefr : 1 for 2:00 and 2 for 2:30 and so on ...'))
    # conitions related to the list 
    if t == 1:
        t =time[0]
        print(t)
    elif t == 2:
        t= time[1]
    elif t == 3:
        t= time[2]
    elif t == 4:
        t= time[3]
    elif t == 5:
        t= time[4]
    elif t == 6:
        t= time[5]
    elif t == 7:
        t= time[6]
    elif t == 8:
        t= time[7]
    elif t == 9:
        t= time[8]

    #to cuse error if the user enter input invalid      
    elif len(t)>1 or len(t)<1:
        print('This is invalid number')
    elif not t.isnumeric():
        print('This is invalid number, contine letter')
    
    #to keep ask user for select another service
    anotherServices = int(input('Would you like another service ? enter Yes (1) or No (0):'))
    #calculat vat
    vat = totalCost * 0.15 
    #add vat the original total
    vat += totalCost
#prinnt bill
print('Thank you for your visit \n Total Cost : ', totalCost ,'\n Total Cost with vat (15%) :',vat ,  'At', t, 'PM')
#print time and date in the bill
print(now)
year = lambda x: x.year
month = lambda x: x.month
day = lambda x: x.day
t = lambda x: x.time()
print(year(now),month(now),day(now))
print(t(now))
 