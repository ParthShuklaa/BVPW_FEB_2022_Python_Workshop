amount = 10000
if(amount > 4999):
    print("Purchase is done..!!!")

try:
    a= amount/10
except ZeroDivisionError:
    print("You can not divide a no by 0")
print(a)

a = [1,2,3]
try:
    print("Second Element = " +str(a[1]))
    print("Fourth Element = %d"%(a[3]))
except IndexError:
    print("INdex Error")
except:
    print(" An error Occured")
finally:
    print("This will execute irrespective of any error")