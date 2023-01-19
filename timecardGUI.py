import tkinter as tk
import weeklyTimecard as wT

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        self.contents = tk.StringVar()
        self.contents.set("this is a variable")
        
        self.entrythingy["textvariable"] = self.contents
        self.entrythingy.bind('<Key-Return>', self.print_contents)

        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

        self.weekendingDateAsDatetime = tk.Entry()
        self.weekendingDateAsDatetime.pack()
        self.weekendingDate = tk.StringVar()
        self.weekendingDate.set(wT.weekendingDate)

        self.but = tk.Button(master,text="Press Me!", command=self.helloCallback)
        self.but.pack()

        self.weekendingDateAsDatetime["textvariable"] = self.weekendingDate

        for pair in wT.weeklyHoursAsDateTime:
            self.dayWorkedFrame = tk.Frame(master)
            self.dayWorked = tk.Label(self.dayWorkedFrame, text=pair[1])
            self.dayWorked.pack()
            self.dayWorkedFrame.pack()

            self.entry = tk.Entry(self.dayWorkedFrame)
            self.entry["width"] = 20
            self.entry.pack()

            self.hours = tk.StringVar()
            self.hours.set(pair[0])
            self.entry["textvariable"] = self.hours
            # self.hours.pack()
            # print(pair)

        
    def print_contents(self, event):
        print("Hi. The current event content is:", self.contents.get())

    def helloCallback(self):
        if (self.contents.get() == wT.weekendingDate): 
            self.but["text"] = "Press Me!"
            self.contents.set("Undone!")
            print("Button pressed!")
        else: 
            self.contents.set(wT.weekendingDate)
            self.but["text"] = "Change back"
            print("Button pressed!")


    

root = tk.Tk()
myapp = App(root)


myapp.master.title("TimeCard Completer")
myapp.master.maxsize(1000,1000)

myapp.mainloop()