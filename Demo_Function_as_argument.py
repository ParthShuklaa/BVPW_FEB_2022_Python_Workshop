"""
Function As an Argument
"""
def Message(text):
    return text.upper()
print(Message("I am feeling Lucky"))
Speak = Message
#Here A function is assigned to a Variable
#It takes the function object referenced by message and creates a second name pointing to it
#Speak
print(Speak("I am Feeling Hungry"))
def newmessage(text):
    return text.lower()
#Higher order Fucntion
def Greeting(func):
    #storing a function in a Variable
    Mygreetings = func("Hi - Message from a function as an argument ")
    print(Mygreetings)
Greeting(Message)
Greeting(newmessage)