# this dictionary has name for the movies for kids and rating out of 5 for each movie
movies = {
    "Name of the movie":"The rating out of 5",
    "sonic the movie": 4.5,
    "chip`n dale": 4,
    "the smurfs": 3.5
}


''''
Now to make if the user it write a right input
but before anything we have rule for this cinema
the kids age must be between 6 -10 years old
and by the end it prints the total of the tickets, in which the price for the one ticket is 20.5
'''

# to check if the user want to choose if he wants to watch or not
theMovie = input("Hi,welcome to cinema for kids are you excited to choose the movie?(wirte yes) ").lower()
if theMovie == "yes":
    #print the dictionary if he doesn`t want will go to else at the end
    for a, b in movies.items():
        print(a, " ", b)
    chooseMovie = input("Choose the movie do you want for your wonderful kid :) ").lower()
    #check if the name of the movie is right or not
    if chooseMovie not in movies.keys():
        print("we don`t have this movie")
    else:

        age = int(input("before anything we want to check your kid age please write age "))

        # check the age by conditions if statements if it`s right will go to inside elif
        def checkage(age):
            if age > 10:
                print("oohh :( we can`t take your kid, it must be between 6 - 10 years old, we really sorry ")
            elif age <= 10 and age >= 6:
                print("let`s go to another check then :))")

                # time to calculate the tickets
                numb = int(input("If you please write how many tickets you want :) "))

                
                 x = lambda numb: numb * 20.5
                 print("the total for the tickes is", x(numb),"$")
                 print("Thank you :)")



            else:
                print("oohh :( we can`t take your kid, it must be between 6 - 10 years old, we really sorry ")
            return age


        checkage(age)


else:
    print("well, see you soon")



