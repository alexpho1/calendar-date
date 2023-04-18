from tkinter import *
from tkcalendar import Calendar

#create the gui object
tk = Tk()
#create shape of calendar
tk.geometry('700x700')

#add the calendar
cal = Calendar(tk, selectmode = 'day', year = 2023, month = 4, day = 18)

cal.pack(pady = 20, fill = 'both', expand = True)

savedDates = []
#Function to show the selected date
def grad_date():
    date.config(text = 'Selected Date is: ' + cal.get_date())
    savedDates.append(cal.get_date())


#Add button and label
Button(tk, text = 'Get Date', command = grad_date).pack(pady = 15)
date = Label(tk, text = '')
date.pack(pady = 20)

#execute line
tk.mainloop()


