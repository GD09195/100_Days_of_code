import pandas as pd
import random as rd
import smtplib as smtp
import datetime as dt

source_mail = 'gdtest0912@gmail.com'
source_password = 'uantymuzhufwozwy'

def sent_mail(email: str, letter: str)->None:
    with smtp.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user= source_mail, password=source_password)
        connection.sendmail(
            from_addr=source_mail,
            to_addrs=email,
            msg=f'Subject:Happy Birthday! \n\n{letter}'
        )

def get_random_letter(name: str)->str:
    letter_name = f'letter_{rd.randint(1,3)}.txt'
    with open(f'./letter_templates/{letter_name}') as letter_file:
        letter = letter_file.read()
    return letter.replace('[NAME]', name)

def get_today_letters(birthdays: dict)->dict:

    birthday_letters = {}

    current_day = dt.datetime.now().day
    current_month = dt.datetime.now().month

    for name, info in birthdays.items():
        if current_month == info['birthday'].month and current_day == info['birthday'].day:
            letter = get_random_letter(name)
            birthday_letters.update({name: letter})

    return birthday_letters

def get_birthday_dict()->dict:
    #Read birthdays csv
    birthday_df = pd.read_csv('./birthdays.csv')

    #Save a List of Dictionaries {name: birthday}
    birthdays = {row['name']: {
                  'email': row['email'],
                  'birthday': dt.datetime(year=row['year'], month=row['month'], day=row['day'])
                  } for index, row in birthday_df.iterrows()
                 }

    return birthdays

def main()->None:

    birthday_list = get_birthday_dict()
    today_letters = get_today_letters(birthday_list)

    if len(today_letters) == 0:
        print('There are no birthdays today')
        return

    people_to_congratulate = list(today_letters.keys())

    for person in people_to_congratulate:
        sent_mail(email=birthday_list[person]['email'], letter= today_letters[person])


main()