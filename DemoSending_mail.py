import smtplib

sender = "Parth.Shukla1989@gmail.com"
mypassword = "**********"
receivers = ['pagarsamruddhi09@gmail.com']
message = """ FROM : parth Shukla1989@gmail.com To: Samrudhi
Subject : SMTP Email Testing
This is a test email Message 
"""


smtpObj = smtplib.SMTP('smtp.gmail.com',587)
smtpObj.starttls()
smtpObj.login(sender,mypassword)
smtpObj.sendmail(sender,receivers,message)
print("Successfully sent mail")
smtpObj.quit()
