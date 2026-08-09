##################### Normal Starting Project ######################

import datetime as dt
import pandas as pd
import random
import smtplib
import os

BASE_DIR = os.path.dirname(__file__)
BIRTHDAYS_CSV = os.path.join(BASE_DIR, "birthdays.csv")
LETTER_DIR = os.path.join(BASE_DIR, "letter_templates")

today = dt.datetime.now()
today_tuple = (today.month, today.day,today.hour,today.minute)

birthdays = pd.read_csv(BIRTHDAYS_CSV)
birthdays_dict = {
    (row["month"], row["day"], row["hour"], row["minute"]): row
    for (_, row) in birthdays.iterrows()
}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    name = birthday_person["name"]
    email = birthday_person["email"]

    letter_number = random.randint(1, 3)
    letter_path = os.path.join(LETTER_DIR, f"letter_{letter_number}.txt")
    with open(letter_path, "r", encoding="utf-8") as letter_file:
        letter_text = letter_file.read().replace("[NAME]", name)

    my_email = "systemkali741@gmail.com"
    my_password = "ixabnpinpimljfoa"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        subject = "Happy Birthday From Md Shameel"
        message = f"Subject: {subject}\n\n{letter_text}"
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=message
        )

   
