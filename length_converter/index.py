from tkinter import Tk, Button, Label, DoubleVar, Entry

# Create application window
window = Tk()

# title function to add a name to the top of the app window
window.title('Feet to Meter Conversion Application')

# app window colour config
window.configure(background="light slate gray")

# set window size
window.geometry('320x320')

# prevent window to be resized
window.resizable(width=False, height=False)


# invoke mainloop() to run the app
window.mainloop()