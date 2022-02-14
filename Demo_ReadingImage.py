"""

Step1: Importing package matplotlib
Step2: Reading an Image
Step3: Displaying the Content of Image
"""

import matplotlib.image as img
import matplotlib.pyplot as plt
myimage = img.imread("AZ-204.png")
plt.imshow(myimage)
plt.show()
plt.imshow(myimage)
print("Displaying Image....")

