import Image
import ImageTk
import Tkinter as tk
import glob

class Resize:
    def __init__(self):

        self.image = Image.open("/home/hr/Python/interface1.png")
        self.root = tk.Tk()
        self.root.title("Shrink")
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        self.img = ImageTk.PhotoImage(self.image)
        self.label = tk.Label(self.root, image=self.img)
        self.label.pack()
        self.lab1 = tk.Label(self.root)
        self.lab1['text'] = "..."
        self.lab1.pack()
        self.listbox = tk.Listbox(self.root)
        self.listbox.pack(fill=tk.BOTH)
        for file in glob.glob("*.gif"):
            self.listbox.insert(0, file)
        self.lab2 = tk.Label(self.root, text="Insert ratio to shrink image (2=50%)")
        self.lab2.pack()
        self.entry = tk.Entry(self.root)
        self.entry.pack()
        self.root.mainloop()
        
Resize()


#app = GUI(image = "h:\\jupyter\\covermaker\\imgs\\python_big.png",
            #shrink_ratio = 2)
