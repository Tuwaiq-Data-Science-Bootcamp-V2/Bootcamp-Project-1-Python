
sign_list = ['Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo',
             'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces']
zodiac_cele = ('Reese Witherspoon', 'Adele', 'Kendrick Lamar', 'Selena Gomez', 'Kylie Jenner', 'Zendaya',
               'Halsey', 'Lorde', 'Nicki Minaj', 'Michelle Obama', 'Harry Styles', 'Rihanna')
month_day = {1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
month_list = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']

# Welcome message
print("Hello! Let's start!\n")


# date validation
def date_val():
    while True:
        day, month = input('Enter the day and the month in numbers(dd/mm):\n').split('/')
        if day.isdigit() and month.isdigit():
            day, month = int(day), int(month)
            if 1 <= month <= 12 and 1 <= day <= int(month_day.get(month)):

                print('you chose {},{} '.format(day, month_list[month - 1]))
                month_name = month_list[month - 1].lower()
                break
            else:
                print('This is an invalid date')
        else:
            print('Enter numbers only')
    return day, month, month_name


# Finding the sign zodiac
def sign_name(month_name, day):
    if month_name == 'december':
        sign = 'Sagittarius' if (day < 22) else 'capricorn'
    elif month_name == 'january':
        sign = 'Capricorn' if (day < 20) else 'aquarius'
    elif month_name == 'february':
        sign = 'Aquarius' if (day < 19) else 'pisces'
    elif month_name == 'march':
        sign = 'Pisces' if (day < 21) else 'aries'
    elif month_name == 'april':
        sign = 'Aries' if (day < 20) else 'taurus'
    elif month_name == 'may':
        sign = 'Taurus' if (day < 21) else 'gemini'
    elif month_name == 'june':
        astro_sign = 'Gemini' if (day < 21) else 'cancer'
    elif month_name == 'july':
        sign = 'Cancer' if (day < 23) else 'leo'
    elif month_name == 'august':
        sign = 'Leo' if (day < 23) else 'virgo'
    elif month_name == 'september':
        sign = 'Virgo' if (day < 23) else 'libra'
    elif month_name == 'october':
        sign = 'Libra' if (day < 23) else 'scorpio'
    elif month_name == 'november':
        sign = 'scorpio' if (day < 22) else 'sagittarius'

    print('your zodiac sign is {}.'.format(sign.capitalize()))
    x = sign.capitalize()
    y = sign_list.index(x)

    # Celebrities with the same sign
    print('celebrities share your astrological sign: {}'.format(zodiac_cele[y]))


# Call functions
def main():
    day, month, month_name = date_val()
    sign_name(month_name, day)

    while True:
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() == 'no':
            exit(print('\nSee you soon!!\n'))
            break
        elif restart.lower() != 'yes':
            print('\nEnter a valid answer\n')
        else:
            main()


if __name__ == "__main__":
    main()
