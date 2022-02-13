"""
Creating a Pie Chart
Step1: import a Package matplotlib.pyplot and numpy
Step2: Use function to Plot Pichart
Step3: Show Pie Chart

"""

import matplotlib.pyplot as plt
import numpy as np

y = np.array([25,50,12,13])
mylabel = ["Titan - 25%","Timex - 50%","Rado- 12%","Maxima- 13%"]
myexplode = [0.2,0.2,0.2,0.2]
plt.pie(y,labels= mylabel,explode= myexplode,shadow=True)
plt.legend(title = "Market SURVEY for WRIST WATCHES")
plt.show()