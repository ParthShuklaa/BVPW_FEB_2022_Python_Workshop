"""
Step1: Importing Pandas package

"""
import pandas as pd

mydataset = {
    'cars' : ["BMW","Volvo","Ford"],
    'Pasing': [10,15,20]
}
myvar = pd. DataFrame(mydataset)
print(myvar)
print(pd.__version__)