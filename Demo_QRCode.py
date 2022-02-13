"""
Step 1: Include Pyqrcode package
Step2 :this is the string that represent QR code

Step3 :Genrating the QR Code

Step4 :Creating and Saving the svg file with "myqr.svg"

"""

import pyqrcode
#import png

my_email = "parth.shukla@9ledgepro.com\n"
my_number = "9599587014\n"
my_linkedin_id = "https://www.linkedin.com/in/parth-shukla-09205239/\n"
my_organisation_WebSite = "https://9ledgepro.com/\n"
twitter_handler = "https://twitter.com/parthshukl\n"
#this is the string that represent QR code
mystring = my_email + my_number + my_linkedin_id +my_organisation_WebSite + twitter_handler

#Genrating the QR Code
my_url = pyqrcode.create(mystring, version=12)

#Creating and Saving the svg file with "myqr.svg"
my_url.svg("myqr.svg", scale=10)

print("Congratulations..!!! You have Successfully Created your own QR Code .!!!!")
