# this dictionary has name for the movies for kids and rating for each movie
movies = {
    "sonic the movie": 4.5,
    "chip`n dale": 4,
    "the smurfs": 3.5
}
# to check if the user want to choose if he wants to watch or not
theMovie = input("Hi,welcome to cinema for kids are you excited to choose the movie? ").lower()
if theMovie == "yes":
    for a, b in movies.items():
        print(a, " ", b)
else:
    print("well, see you soon")
''''
Now to make if the user it write a right input
but before anything we have rule for this cinema
the kids age must be between 6 -10 
and by the end it prints the total of the tickes
the price of the ticket is 20.5
 
'''
chooseMovie = input("Choose the movie do you want for your wonderful kid :) ").lower()
while True:
    if chooseMovie not in movies.keys():
        print("we don`t have this movie")
        break
    else:

        age = int(input("before anything we want to check your kid age please write age "))


        def checkage(age):
            if age > 10:
                print("oohh :( we can`t take your kid, it must be between 10 - 6 we really sorry ")
            elif age <= 10 and age >= 6:
                print("let`s go to another check then :))")
            else:
                print("oohh :( we can`t take your kid, it must be between 10 - 6 we really sorry ")
            return age


        checkage(age)

        numb = int(input("If you please write how many tickes you want :) "))


        def numtick(numb):
            x = lambda a: a * 20.5
            print("the bill for the tickes is" , x(numb))


        numtick(numb)
        break
