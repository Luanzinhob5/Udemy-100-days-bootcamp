import smtplib

my_email = "tatujeca635@gmail.com"
password = "jecatatu@01"

connection = smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=my_email,password=password)
connection.sendmail(from_addr=my_email, to_addrs="puq23245@jioso.com", msg="Hello")
connection.close()

# DONT WORK