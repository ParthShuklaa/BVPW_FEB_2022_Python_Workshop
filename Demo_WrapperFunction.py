def hello_decorator(func):
    #inner1 is awrapper fucntion in which argument is called
    def inner1():
        print("Hello : This is before the function executes")
        #calling the actual function inside the wrapper function
        func()
        print("This  is after function execution ")
    return inner1

def function_to_be_Used():
    print("This is inside the function!!")
function_to_be_Used()
#paasing 'function_to_be_used' inside the decorator so that we can control its behavior
function_to_be_Used = hello_decorator(function_to_be_Used)
print("--------------After using decorator--------------------")
function_to_be_Used()