from tkinter import Tk, Button, Label, DoubleVar, Entry


# Create application window
window = Tk()

# title function to add a name to the top of the app window
window.title('Feet to Meter Conversion Application')

# app window colour config
window.configure(background='light slate gray')

# set window size
window.geometry('320x320')

# prevent window to be resized
window.resizable(width=False, height=False)

# create & configure labels for feet units
ft_label = Label(window, text='Feet', bg='light slate grey', fg='black', width=8)
ft_label.grid(column=0, row=0, padx=10, pady=20)
ft_label.config(font=("Ariel", 22))

# define data type 
ft_value = DoubleVar()

# create entry widget with data type it should accept and set size
ft_entry = Entry(window, textvariable=ft_value, width=14)

# position entry window on column 1 and row 0
ft_entry.grid(column=1, row=0)

# functionality to clear entry widget at launch
ft_entry.delete(0, 'end')

# create & configure labels for meter units
m_label = Label(window, text='Meters', bg='light slate grey', fg='black', width=8)
m_label.grid(column=0, row=1)
m_label.config(font=("Ariel", 22))

# define data type 
m_value = DoubleVar()

# create entry widget with data type it should accept and set size
m_entry = Entry(window, textvariable=m_value, width=14)

# position entry window on column 1 and row 0
m_entry.grid(column=1, row=1, pady=30)

# functionality to clear entry widget at launch
m_entry.delete(0, 'end')

# create buttons that processes conversion logic
convert_btn = Button(window, text='Convert', highlightbackground='gray', fg='white', width=14, command='')
convert_btn.grid(column=0, row=3, padx=15)

# create buttons that processes clear text field logic
clear_btn = Button(window, text='CLEAR', highlightbackground='gray', fg='white', width=14, command='')
clear_btn.grid(column=1, row=3, padx=15)


# invoke mainloop() to run the app
window.mainloop()