#step1 Defining a labda function

square  = lambda x: x*x

print("Square of 2 is :"+str(square(2)))

#implementing lamda as cube

cube = lambda func: func **3
print("Cube of 4 is "+str(cube(square(2))))