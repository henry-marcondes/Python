from Tkinter import *
from PIL import Image, ImageTk

root = Tk()

same = True
#n can't be zero, recommend 0.25-4
n=0.5

path = "/home/hr/Python/interface.gif" 
image = Image.open(path)
[imageSizeWidth, imageSizeHeight] = image.size

newImageSizeWidth = int(imageSizeWidth*n)
if same:
    newImageSizeHeight = int(imageSizeHeight*n) 
else:
    newImageSizeHeight = int(imageSizeHeight/n) 

image = image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
img = ImageTk.PhotoImage(image)

Canvas1 = Canvas(root)

Canvas1.create_image(newImageSizeWidth/2,newImageSizeHeight/2,image = img)      
Canvas1.config(bg="blue",width = newImageSizeWidth, height = newImageSizeHeight)
Canvas1.pack(side=LEFT,expand=True,fill=BOTH)

root.mainloop()
