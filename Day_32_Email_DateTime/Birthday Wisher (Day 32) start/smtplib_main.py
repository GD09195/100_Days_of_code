import smtplib_main

my_email = 'gdtest0912@gmail.com'
password = 'uantymuzhufwozwy'

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user= my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs='gd091295@gmail.com',
        msg='Subject:Hello \n\n Hello World'
)

#connection.close()

