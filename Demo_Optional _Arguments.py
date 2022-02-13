"""
Working with Optional Arguments
We can call function weather by optional parameters or default parameters
"""

def my_func(a,b=9999):
    return a+b

print(my_func(10,20))
print(my_func(1))

def display_string(string1,string2 = "Thank You"):
    print(string1 + string2)

print(display_string("Hi i am Parth\t"))
print(display_string("Hi Iam parth","Hope You are learning something new"))