from PIL import Image
#PIL: Python Imaging Library

img = Image.open('AZ-204.png')

img.show()

print(img.format)
print(img.mode)