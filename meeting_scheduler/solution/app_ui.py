from tkinter import *
from tkinter import ttk
from app_state import App_State
from datetime import date
import datetime
import meeting_model


def set_user(event):
    main_app.current_user = main_app.users[event.widget.current()]
    print("set_user clicked")

def set_hour(event):
    main_app.selected_hour = event.widget.get()
    print(event.widget.get())
    print("set_hour clicked")

def set_length(event):
    main_app.selected_length = event.widget.get()
    print("set_length clicked")

def save_new_meeting():
    m = meeting_model.Meeting_Factory.create_meeting(main_app.selected_date,
                                                     main_app.selected_hour, main_app.selected_length,
                                                     main_app.text_element.get('1.0','end-1c'), main_app.current_user)
    main_app.send_message(meeting_model.Meeting_Factory.meeting_to_string(m).encode())


    global newWindow
    if newWindow is not None:
        newWindow.destroy()

    refresh_ui()


def refresh_ui():
    main_app.refresh_list()
    print(main_app.day_schedule.schedule)
    Lb1.delete(0,'end')
    for i in range(len(main_app.day_schedule.schedule)):
        Lb1.insert(i,f"{main_app.day_schedule.schedule[i].time}  {main_app.day_schedule.schedule[i].title}")
   


def createNewDateWindow():
    print("createNewDateWindow clicked")
    global newWindow
    if newWindow is not None:
        newWindow.destroy()
    newWindow = Toplevel(main_window)
    
    Label(newWindow,text = "User").grid(column=0, row=0)

    combo = ttk.Combobox(newWindow, values=main_app.users)
    combo.bind('<FocusIn>',set_user)
    combo.grid(column=1, row=0, pady=10, padx=10)
    combo.current(0)

    Label(newWindow,text = "Start Hour").grid(column=0, row=2)
    time_combo = ttk.Combobox(newWindow, values=get_hours())
    time_combo.bind('<FocusIn>',set_hour)
    time_combo.grid(column=1, row=2, pady=10, padx=10)
    time_combo.current(0)

    Label(newWindow,text = "Length").grid(column=0, row=3)
    length_combo = ttk.Combobox(newWindow, values=[x for x in range(1,5)])
    length_combo.bind('<FocusIn>',set_length)
    length_combo.grid(column=1, row=3, pady=10, padx=10)
    length_combo.current(0)

    Label(newWindow,text = "Info").grid(column=0, row=4)
    t = Text(newWindow, height=5,width=30)
    t.grid(column=1, row=4, pady=2, padx=2)
    main_app.text_element = t
    Button(newWindow, text="save", command=save_new_meeting).grid(row=5, column=3, padx=15, pady=10)


def date_changed(event):
    date_str_list = [int(x) for x in event.widget.get().split("-")]
    print(date_str_list)
    isValidDate = True
    try:
        datetime.datetime(date_str_list[0],date_str_list[1],date_str_list[2])
    except ValueError:
        isValidDate = False
    if(isValidDate) :
        print ("Input date is valid ..")
        main_app.set_date(event.widget.get())
        refresh_ui()
    else :
        print ("Input date is not valid..")

def get_hours():
    return [x.time for x in main_app.day_schedule.schedule]
    






if __name__ == '__main__':

    main_app = App_State()

    newWindow = None
    main_window = Tk()

    Label(main_window, text='Date').grid(row=2, padx=15, pady=10)

    date_entry = Entry(main_window)
    date_entry.bind("<KeyPress>", date_changed)
    date_entry.insert(0,date.today())
    date_entry.grid(row=2, column=1) 

    Lb1 = Listbox(main_window, width=30)
    for i in range(len(main_app.day_schedule.schedule)):
        Lb1.insert(i,f"{main_app.day_schedule.schedule[i].time}  {main_app.day_schedule.schedule[i].title}")

    Lb1.grid(row=3, column=0, columnspan=3)

    new_btn = Button(main_window, text="New", command=createNewDateWindow)
    new_btn.grid(row=4, column=2, padx=15, pady=10)

    main_window.mainloop()