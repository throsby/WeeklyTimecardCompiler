import tkinter as tk
import weeklyTimecard as wT
from datetime import datetime
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import PyPDF2




class App(tk.Frame):
    
    def __init__(self, master):
        super().__init__(master)
        self.master.title("TimeCard Completer")
        self.master.maxsize(1000,500)
        self.pack()

        self.styler = ttk.Style()
        self.styler.configure("TEntry", foreground='black')
        # self.styler.map("TEntry", foreground=[('focussed')])


        self.entrythingy = tk.Entry()
        self.entrythingy.pack()

        self.contents = tk.StringVar()
        self.contents.set("this is a variable")
        
        self.entrythingy["textvariable"] = self.contents
        self.entrythingy.bind('<Key-Return>', self.print_contents)

        # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

        self.weekendingDateAsDatetime = tk.Entry()
        self.weekendingDateAsDatetime.pack()
        self.weekendingDate = tk.StringVar()
        self.weekendingDate.set(wT.weekendingDate)

        self.but = tk.Button(master,text="Press Me!", command=self.helloCallback)
        self.but.pack()

        self.weekendingDateAsDatetime["textvariable"] = self.weekendingDate

        # print(iter(wT.workWeekAsDict.values()))
        self.daysList = []
        self.hoursList = []
        self.workDaysColumn = tk.Frame(master, width=400, height=150, highlightbackground="blue", highlightthickness=2)
        self.workDaysColumn.pack(side="left")
        self.pdfView = tk.Frame(master, width=800, height=300 , highlightbackground="blue", highlightthickness=2)
        self.pdfView.pack(side="left")

        for day in wT.workWeekAsDict.values():
            print("The day: ", day)
            self.daysWorkedColumn = tk.Frame(self.workDaysColumn)

            # Anchor aligns the dates to right "east" 
            self.daysWorkedColumn.pack(side="top", anchor="e")
            self.dayWorkedRow = tk.Label(self.daysWorkedColumn, text=datetime.strftime(datetime.fromisoformat(day["Datetime"]), "%A %B %-d, %Y"))
            self.dayWorkedRow.pack(side="left")

            # print(self.daysWorkedColumn.configure())

            self.entry = tk.Entry(self.daysWorkedColumn, width=3, foreground='grey', name=datetime.strftime(datetime.fromisoformat(day["Datetime"]), "entry%Y_%m_%d"))
            self.entry.bind("<FocusIn>", self.changeToFocus)
            self.daysList.append(self.entry)

            self.entry.pack()

            self.hours = tk.StringVar()
            self.hoursList.append(self.hours)
            self.hours.set(day["hours"])
            self.entry["textvariable"] = self.hours

        print(self.daysList)



        self.saveHoursButton = tk.Button(self.workDaysColumn, text="Save Hours Worked")
        self.saveHoursButton.bind("<Button>",self.saveHours)
        self.saveHoursButton.pack()





    def changeToFocus(self, event):
        # print(event.widget)
        # event.widget.configure(foreground='black')
        for day in self.daysList:
            day.configure(foreground='black')
        self.saveHoursButton.configure(foreground='black')

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

    def saveHours(self, event):
        self.master.focus_force()
        print(self.daysList)
        print("Widget: ", event.widget)
        for day in self.daysList:
            day.configure(foreground='grey')
        print(event.widget.configure(foreground='grey'))
        for hour in self.hoursList:
            print(hour.get())
        print("Hours saved")



    

root = tk.Tk()
root.geometry("1100x800")
myapp = App(root)


myapp.mainloop()