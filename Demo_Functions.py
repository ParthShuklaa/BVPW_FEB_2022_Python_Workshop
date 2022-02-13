# #msg = "I am Feeling Lucky"#This is a Global Variable
#
# #Function Decalration
# def DisplayMsg():
#     global msg #making this variable global
#     msg = "I am Feeling Happy"#Local Variable
#     print(msg)
#
# DisplayMsg()
# print('Demo for Function Implementation')
# print(msg)
#
# DisplayMsg()
# def newdisplay():
#     print(msg)
# print("using new Display()")
# newdisplay()
#msg = "I am Feeling Lucky"
def Display():
    global msg
    msg = "I am Feeling happy"
    print(msg)

Display()

def NewDisplay():
    print(msg)

NewDisplay()