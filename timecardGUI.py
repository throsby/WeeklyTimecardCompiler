import tkinter as tk
import weeklyTimecard as wT

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master.title("TimeCard Completer")
        self.master.maxsize(1000,500)
        self.pack()

        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        self.contents = tk.StringVar()
        self.contents.set("this is a variable")
        
        self.entrythingy["textvariable"] = self.contents
        self.entrythingy.bind('<Key-m><Key-Return>', self.print_contents)

        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

        self.weekendingDateAsDatetime = tk.Entry()
        self.weekendingDateAsDatetime.pack()
        self.weekendingDate = tk.StringVar()
        self.weekendingDate.set(wT.weekendingDate)

        self.but = tk.Button(master,text="Press Me!", command=self.helloCallback)
        self.but.pack()

        self.weekendingDateAsDatetime["textvariable"] = self.weekendingDate

        for pair in wT.weeklyHoursAsDateTime:
            self.daysWorkedColumn = tk.Frame(master)
            self.daysWorkedColumn.pack(side="top")
            self.dayWorkedRow = tk.Label(self.daysWorkedColumn, text=pair[1])
            self.dayWorkedRow.pack(side="left")

            self.entry = tk.Entry(self.daysWorkedColumn, width=3)
            self.entry.pack()


            self.hours = tk.StringVar()
            self.hours.set(pair[0])
            self.entry["textvariable"] = self.hours
            # self.hours.pack()
            # print(pair)
        self.saveHoursButton = tk.Button(master, text="Save Hours Worked", command=self.saveHours)
        self.saveHoursButton.pack()

        
    def print_contents(self, event):
        print(event)
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

    def saveHours(self):
        self.master.focus_force()
        print("Hours saved")



    

root = tk.Tk()
myapp = App(root)

myapp.mainloop()