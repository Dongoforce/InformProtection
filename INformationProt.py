from tkinter import*
from installer import*

try:
    (open("license.key", "r"))
except:
    (open("license.key", "w"))
is_have_license = check_CPUsum(get_CPUsum())

window = Tk()
window.title("License cheker")
window.geometry('400x250')
window["bg"] = "blue"
labl = Label(window, text="License:", font=("Arial Bold", 30), padx=120, fg="yellow", bg="blue")
labl.grid(column=1, row=1)

if is_have_license:
    labl2 = Label(window, text="SUCCESS", font=("Arial Bold", 30), padx=120, pady=60, fg="green", bg="blue")
    labl2.grid(column=1, row=2)
else:
    labl2 = Label(window, text="FALLS", font=("Arial Bold", 30), padx=120, pady=60, fg="red", bg="blue")
    labl2.grid(column=1, row=2)
window.mainloop()

