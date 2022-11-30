import smtplib
import datetime as dt
import pandas as pd
import random

data = pd.read_csv("Day_32/birthdays.csv")
now = dt.datetime.now()
today = (now.month, now.day)

# birthday_dict = {new_key: new_value for (index, data_row) in data.iterrows()}

birthday_dict = {(data_row["month"], data_row["day"]):data_row for (index, data_row) in data.iterrows()}
if today in birthday_dict:
    birthday_person = birthday_dict[today]
    random_number = random.randint(1,3)
    file_path = f"Day_32/letter_templates/letter_{random_number}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    # test the message that would be sent via email.
    birthday_message = open("Day_32/message.txt", "w")
    birthday_message.write(contents)
    
    # with smtplib.SMTP("smtp.gmail.com") as connection:
    #     connection.starttls()
    #     connection.login(user="email@email.com", password="password")
    #     connection.sendmail(from_addr="email@email.com", to_addrs=birthday_person["email"], msg=f"Subject:Happy Birthday\n\n{contents}")