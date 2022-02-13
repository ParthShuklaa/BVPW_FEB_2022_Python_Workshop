"""
Plotting graph in X-Y Plane
Step 1: We need to Install matplotlib.Pyplot package
Step 2: We need to Store Pints in X-Y Dimension
Step 3: Plotting graph
"""
import matplotlib.pyplot as plt
# X axis values
x = [1,2,3]
#y axis values
y= [10,15,5]

#plotting the points
plt.plot(x,y)
#plt.bar(x,y)
graphlabel = ['one','two','three']

plt.bar()
plt.xlabel("X axis - Distance in Kms ")

plt.ylabel("Y axis - Time in Hrs")
plt.title("Graph created using MatPlotlib - Python Package ")
#showing the plot
plt.show()