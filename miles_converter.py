from tkinter import * 

window = Tk()
window.title("Convert miles to kms")
window.minsize(width = 150, height = 150)
window.config(padx = 15 ,pady = 15) # to add padding in whole window/ component

entry = Entry(width=20)
entry.insert(END, string = " ") # end is like a index which says text is gonna be there.
#entry.get() --> gets text in the input
entry.grid(row = 0, column = 1)

label1 = Label(text="Miles", font = ("Ariel", 18))
label1.grid(row = 0, column = 2)
label2 = Label(text="Kms", font = ("Ariel", 18))
label2.grid(row = 1, column = 2)
label3 = Label(text="is equal to", font = ("Ariel", 18))
label3.grid(row = 1, column = 0)
label4 = Label()
label4.grid(row = 1, column = 1)

def clicked():
    miles = entry.get()
    km = 1.609 * int(miles)
    label4.config(text = str(km), font = ("Ariel", 18))
button = Button(text="Calculate",font = ("Ariel", 18, "bold"), command = clicked) # like screen.listen()
button.grid(row = 2, column = 1)

window.mainloop() 
