import datetime as dt
import smtplib as smtp
import random as rd


def open_file()->list[str]:
    with open('./quotes.txt') as quotes_file:
        quotes = quotes_file.readlines()
    return quotes

def send_mail(phrase: str)->None:
    email = 'gdtest0912@gmail.com'
    password = 'uantymuzhufwozwy'

    with smtp.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr=email,
            to_addrs=email,
            msg=f'Subject:Phrase of the day\n\n{phrase}'
        )

def get_random_phrase()->str:
    return rd.choice(open_file())


def main():

    current_day = dt.datetime.now().weekday()

    #Send Motivational quote on Mondays
    if current_day == 0:
        send_mail(get_random_phrase())

main()




