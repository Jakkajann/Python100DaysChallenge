# Google don't accept connection from apps anymore.

from calendar import week
import smtplib
import datetime as dt
import random

# my_email = "fermocrosky@gmail.com"
# my_password = "636322159a"

# connection = smtplib.SMTP("smtp.gmail.com", 587)
# connection.starttls()
# connection.login(user=my_email, password=my_password)
# connection.sendmail(from_addr=my_email, to_addrs="fernandobismaia@gmail.com", msg="Subject:Hello")
# connection.close()

MY_EMAIL = "email@email.com"
MY_PASSWORD = "pasword"

now = dt.datetime.now()
week_day = now.weekday()

if week_day ==0:
    with("Day_32/quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    # with smtplib.SMTP("smtp.gmail.com") as connection:
    #     connection.starttls()
    #     connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    #     connection.sendmail(from_addr=MY_EMAIL, to_addrs=MY_EMAIL, msg="Subject:Monday Motivation")