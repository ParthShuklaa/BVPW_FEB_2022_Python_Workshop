"""

It Is used to Store multiple items in a single variable.

Its is built-in datatype.

List items are ordered.

List items are Changeable .

We can have duplicate values in a list.

Demo : Creating a list
"""
my_List = ["Wings of Fire - Dr APJ Abdul Kalam","God of Small Things - Arundhati Roy",
           "Three mistakes of my Life - Chetan Bhagat"]


print(my_List)
def Display():
    for book in my_List:
        print(book)

Display()
print("Adding an Element inside a list___________")
my_List.append("The Monk who sold his ferari - Robin Sharma")
Display()
print("Changing Element of an list_________________")
print(my_List[3])
my_List[3]= "How to make friends and Influence people - Dale Carnegie"
Display()
print(my_List[-3:-1])
print("Checking for an element")
if "Three mistakes of my Life - Chetan Bhagat" in my_List:
    print("Yes, Book is found...")
else:
    print("No Such book found...")

print("Sorting List using Sort()")
my_List.sort()
Display()
print("Sorting in reverse order")
my_List.sort(reverse=True)
Display()