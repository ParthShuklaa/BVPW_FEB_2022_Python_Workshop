my_tuple = ("Dell", "Acer","Apple","HP","Dell")
def Display():
    for computer in my_tuple:
        print(computer)

Display()
print(my_tuple[1])
print(my_tuple.count("Dell"))
print(my_tuple.count("HP"))
#my_tuple[0] = "Lenovo" #Assignment is not allowed
print(len(my_tuple))

print("Any Datatype can be used for creating Tuple ")
my_Fav_No = (5,25,1008)
tuple3 = (False,True,False)
tuple1 = ("Arjun")
print(type(tuple1))
tuple2 = ("DDLJ",)
print(type(tuple2))

final_tuple = tuple2 + tuple3 + my_Fav_No
print(final_tuple)

newtuple = final_tuple*2
print(newtuple)
