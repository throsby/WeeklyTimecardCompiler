import tkinter as tk
import weeklyTimecard as wT

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        self.weekendingDateAsDatetime = tk.Entry()
        self.weekendingDateAsDatetime.pack()
        self.weekendingDate = tk.StringVar()
        self.weekendingDate.set(wT.weekendingDate)

        self.but = tk.Button(root,text="Press Me!", command=self.helloCallback)
        self.but.pack()

        self.weekendingDateAsDatetime["textvariable"] = self.weekendingDate
        
        self.contents = tk.StringVar()
        
        self.contents.set("this is a variable")

        self.entrythingy["textvariable"] = self.contents

        self.entrythingy.bind('<Key-Return>', self.print_contents)

    def print_contents(self, event):
        print("Hi. The current event content is:", self.contents.get())

    def helloCallback(self):
        self.contents.set(wT.weekendingDate)
        print("Button pressed!")

root = tk.Tk()
myapp = App(root)

myapp.master.title("TimeCard Completer")
myapp.master.maxsize(200,200)

myapp.mainloop()