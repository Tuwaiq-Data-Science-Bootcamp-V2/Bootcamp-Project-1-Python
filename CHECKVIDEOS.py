Videos = {
    "Name of the video": "The time for the video in minutes",
    "puss in boots: the last wish": 10,
    "الرسّام فدا: أدب رسم الشاحنات": 5,
    "world’s grumpiest cat": 2
}

'''''
In this code I choose a sample of videos in youtube but the maximum time is 10 minutes 
I create it for the people that want to watch a short videos but they don`t know what to watch :) (like me)
'''

# the welcome Message
check_user = input("Welcome to our website :) ,If you want to choose time of the video write 'yes' or if you want to see the list of videos write 'videos': ").lower()

# for check the input must choose between yes or videos or will he kick out of the website >:)
if check_user == "yes":
    print("ALRIGHT! all our videos in minutes the max one is 10 min :)")
    chosevideo = int(input("Please write the time you want: "))
    def checktime(chosevideo):
        if chosevideo <= 10 and chosevideo > 5:
            print("We suggest this video Puss in Boots: The Last Wish is 10 minutes")
            checkpay = input("do you want to sub to remove the adds in videos? :) write 'yes' or 'no' " ).lower()
            if checkpay == "yes":
                print("alright")
                payment = int(
                    input(
                        "for one month is 12.5 $ how many months do you want? please write it in numbers ex:1,2,...12: "))
                money1 = lambda payment: payment * 12.5
                print("your total is", money1(payment), "$ thanks for sub :) here your video enjoy 'https://youtu.be/bEoNNYyVNxc' ")
            else:
                print("it`s ok :(, but you can watch the video :) here your video enjoy 'https://youtu.be/bEoNNYyVNxc'")
        elif chosevideo <= 5 and chosevideo > 2:
            print("We suggest this video الرسّام فدا: أدب رسم الشاحنات is 5 minutes ")
            checkpay = input("do you want to sub to remove the adds in videos? :) write 'yes' or 'no' ").lower()
            if checkpay == "yes":
                print("alright")
                payment = int(
                    input(
                        "for one month is 12.5 $ how many months do you want? please write it in numbers ex:1,2,...12: "))
                money1 = lambda payment: payment * 12.5
                print("your total is", money1(payment), "$ thanks for sub :) here your video enjoy 'https://youtu.be/LRETIz9AaSQ' ")
            else:
                print("it`s ok :(, but you can watch the video :) here your video enjoy 'https://youtu.be/LRETIz9AaSQ' ")
        elif chosevideo <= 2:
            print("We suggest this video World’s Grumpiest Cat is 2 minutes")
            checkpay = input("do you want to sub to remove the adds in videos? :) write 'yes' or 'no' ").lower()
            if checkpay == "yes":
                print("alright")
                payment = int(
                    input(
                        "for one month is 12.5 $ how many months do you want? please write it in numbers ex:1,2,...12: "))
                money1 = lambda payment: payment * 12.5
                print("your total is", money1(payment), "$ thanks for sub :) here your video enjoy 'https://youtu.be/kgrV3_g9rYY' ")
            else:
                print("it`s ok :(, but you can watch the video :) here your video enjoy 'https://youtu.be/kgrV3_g9rYY' ")
        else:
            print("we only have videos from 10 to 2 min")
    checktime(chosevideo)
elif check_user == "videos":
    for p,q in Videos.items():
        print(p,"  ",q)
    chosing_vi = input("what do you like to choose? ").lower()
    while chosing_vi not in Videos.keys():
        print("we dont have it yet :( ,we will tell you in your email if we got it :) have good day")
        break
    else:
        print("good choose:) ",chosing_vi,",enjoy :)")

        checkpay = input("do you want to sub to remove the adds in videos? :) write 'yes' or 'no' ").lower()
        if checkpay == "yes":
            print("alright")
            payment = int(input("for one month is 12.5 $ how many months do you want? please write it in numbers ex:1,2,...12: "))
            money = lambda payment : payment * 12.5
            print("your total is",money(payment),"$ thanks for sub :) here your videos enjoy")
            url = {
                'World’s Grumpiest Cat (2 min)': 'https://youtu.be/kgrV3_g9rYY',
                'Puss in Boots: The Last Wish(10 min)': 'https://youtu.be/bEoNNYyVNxc',
                'الرسّام فدا أدب رسم الشاحنات ( 5 min)': 'https://youtu.be/LRETIz9AaSQ'}
            for z,x in url.items():
                print(z," ",x)

        else:
            print("it`s ok :(, but you can watch the video :) here your videos enjoy")
            url = {
                'World’s Grumpiest Cat (2 min)': 'https://youtu.be/kgrV3_g9rYY',
                'Puss in Boots: The Last Wish(10 min)': 'https://youtu.be/bEoNNYyVNxc',
                'الرسّام فدا أدب رسم الشاحنات ( 5 min)': 'https://youtu.be/LRETIz9AaSQ'}
            for z, x in url.items():
                print(z, " ", x)

else:
    print("well see you soon have a good day")