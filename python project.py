name = lambda : print(" \n\t Wellcome you're in AQRA store \n" 
     "Enter your age and will show you the books that are appropriate for your age ")
age=18
deliver=10.0

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
name()
x=int(input("\nAge: " ))

list = ["Memories", "Brief history of time", "A thousand pices of you", "paper towns"]
list2 = ["Sisters story", "Sara and her friends","Exercise with sally","Learn to be friendly","English alphabet"]


if x >= 14:
    print(list)
elif x>=8 and x<=13:
    print(list2)
else:
    print("The book does not exist in list")

choose_book = str(input("\nChoose the book : "))

for key in list:
    if choose_book == key:
        print("The book name is " + key)

for key2 in list2:
    if choose_book == key2:
        print("The book name is " + key2)


def p():
    if choose_book == list[0]:
        print("The total price is ", deliver+22)

    elif choose_book == list[1]:
        print("The total price is ", deliver+34)

    elif choose_book == list[3]:
        print("The total price is ", deliver+25)

    elif choose_book == list[2]:
        print("The total price is ", deliver+33)

    elif choose_book == list2[0]:
        print("The total price is ", deliver+18)

    elif choose_book == list2[1]:
        print("The total price is ", deliver+12)

    elif choose_book == list2[3]:
        print("The total price is ", deliver+15)

    elif choose_book == list2[2]:
        print("The total price is ", deliver+20)

    elif choose_book == list2[4]:
        print("The total price is ", deliver+16)

p()









