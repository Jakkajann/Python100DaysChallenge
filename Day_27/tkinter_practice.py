from struct import pack
import tkinter

window = tkinter.Tk()
window.title("My First GUI Progam")
window.minsize(width=500, height=300)

#Label

my_label = tkinter.Label(text="I'm a label", font=("Arial", 24, "bold"))
my_label.pack()

# Buttons

def button_clicked():
    print("I got clicked")
    my_label.config(text=input.get())

button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

# Entry

input = tkinter.Entry(width=20)
input.pack()

window.mainloop()