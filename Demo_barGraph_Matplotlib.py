import matplotlib.pyplot as plt
left = [1,2,3,4,5]
height = [60,20,30,45,55]

graph_label = ['One','Two','Three','Four','Five']

plt.bar(left,height,tick_label = graph_label , width=1,color = ['green','yellow'])

plt.xlabel ('x- Axis - Instagram users in 1000')
plt.ylabel('y - Axis - Revenue from paid Ad in Lakhs ')
plt.title("Instagram Advertisement budget")
plt.show()
"""
   We have Tick_Label for defining names to X-Axis coordinates 
   
"""