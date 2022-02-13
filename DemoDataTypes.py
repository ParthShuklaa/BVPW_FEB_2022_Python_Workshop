# # x = "Hello World" #str
# # x = 50 # int
# # x = 20.123 # float
# # x = 4j #complex number
# # x = ["Dell","Apple","Sony"] #List
# # x = ("Delhi","Mumbai","Pune") #Tuple
# # x = range(10) #range
# # x = {"Tesla","BMW","Ferrari"} #Set
# # x = frozenset({"Tesla","BMW","Ferrari"}) #frozenSet
# # x = False #boolean
# # x = b"Hello"
# # x = bytearray(5)
# # x = memoryview(bytes(5))
#
# print("Working with String in python")
#
# name = 'parth'
# surname = "Shukla"
# city = """ DELHI,
# India,
# PIN - 110001"""
#
# print(name + surname + city)
# print(name[1])
# #print(name[:1])
# print("Looping around Array ")
# for x in name:
#     print(x)
#
# print("Length of City is "+str(len(city)))
#
# mydetails = {
#     "Name" : "Parth",
#     "Surname" :"Shukla",
#     "City" : "Delhi",
#     "Pin" : "110001"
# }
#
# print(mydetails)
# print(mydetails["City"])
# print(len(mydetails))
#
# for i in mydetails:
#     print(i)
#
# #Checking inside a string
# myFile = "    the Quik Brown Fox jumps over the lazy dog      "
#
# print("dog" in myFile)
# print( "Tiger" in myFile)
#
# if "Fox" in myFile:
#     print("Yes!!, FOX is Present ")
#
# if "Tiger" not in myFile:
#     print("Tiger, Is not present")
#
# #Slicing a string
# print(myFile[5:20])
# print(myFile[-10:-2])
#
# print(myFile.upper())
# print(myFile.lower())
# print(myFile.strip())
# print(myFile.split(" "))
#

age = 20
#name = "David beckham"
output = "David beckham{}"
print(output)
#We can perform it with the help of format()

print(output.format(age))

day = "25th"
month = "Dec"
year = 1991
DOB = "My Day od Birth is {} Month is {} and year is {}"
print(DOB.format(day,month,year))