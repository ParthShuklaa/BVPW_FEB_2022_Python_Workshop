# """
# Step1: Opening a file using Open()
# Step2: Printing content of file
# Here Open Command Will open the file in read mode and for loop will print each line present in the file
#
#
# """
#
# myfile = open('Sampledata.txt','r')
# #print(myfile) this is not allowed
# for i in myfile:
#     print(i)
#
# #Using Read Method
def DisplayFileContent():
    file = open('Sampledata.txt','r')
#print(file.readline())
    print("Implementing Read() for printing every thing....")
    print(file.read())


# newfile = open('Sampledata.txt','a')
# newfile.write("In My free time, i read self help books and motivational Blogs...")
# #print(newfile.read())

print("Writing into a File ")
file1 = open('Sampledata.txt','w+')
file1.write("I am Feeling Lucky")
file1.write("Here we Are writing into a File....")

file1.close()

DisplayFileContent()

print("using a Write Along with the With() function")

with open('Sampledata.txt') as file1:
    data = file1.read()
    print(data)
    # for i in data:
    #     print(i)
