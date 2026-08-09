import smtplib
import datetime as dt   
import random
import os

quotes_file = os.path.join(os.path.dirname(__file__), "quotes.txt")
with open(quotes_file, "r", encoding="utf-8") as file:
    quotes = [line.strip() for line in file if line.strip()]

my_email = "systemkali741@gmail.com"
my_password = "ixabnpinpimljfoa"
recipient_email = "mdshameel740@gmail.com"

now = dt.datetime.now()
weekday = now.weekday()


with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()
    connection.login(user=my_email, password=my_password)

    if weekday == 7:  # Check if today is Monday (0 represents Monday)
        #-----email content-----#
        subject = "Happy Birthday"
        body = random.choice(quotes)
        message = f"Subject: {subject}\n\n{body}"

        #-----send email-----#
        connection.sendmail(
            from_addr=my_email,
            to_addrs=recipient_email,
            msg=message
        )






