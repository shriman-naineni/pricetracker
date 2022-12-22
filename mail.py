import smtplib

mail = smtplib.SMTP("smtp.gmail.com",587)
mail.starttls()
mail.login("smtptestingdemo123@gmail.com", "fsqdxogmleonjdjo")
message = "hi whats up"
user = input("please enter your email: ")
mail.sendmail("smtptestingdemo123@gmail.com", user, message)
