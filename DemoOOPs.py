class MyClass:
    def __init__(self,name, age):#voidmain()
        self.name = name
        self.age = age
        x = 100
#__init__() this is being called automatically when the class
# is being used to crate a new object
    def myfunc(self):
        print("Hello my name is " + self.name)
#self parameter is a ref to the current instance of the class (this)

p1 = MyClass("John",25)
print(p1.name)
print(p1.age)
p1.myfunc()

p1.name = "Sachin Tendulkar"
#we can edit values directly
print(p1.name)

#del p1.age
#We can delete age property
print(p1.age)

#We can delete object also
#del p1

print(p1)

class student(MyClass): #Child Class
    pass

x = student ("Mike","Olsen")
x.myfunc()