from tkinter import *  # use in case of only one module to prevent errors
# you can do from tkinter import * to prevent defining tkinter everywhere

window = Tk()
window.title("Convert miles to kms")
window.minsize(width = 600, height = 400)
window.config(padx = 30 ,pady = 30) # to add padding in the whole program / element

# LABEL
label = Label(text="I am Label", font = ("Ariel", 24, "bold"))
label.pack() # text appers in the leftmost of first lne
# pack function can change side of text, type, position, add padding,etc.
label["text"] = "My text" # label.config(text = "New Text")

# BUTTON
def clicked():
    new_text = input.get()
    label.config(text = new_text) # add config don't write directly
button = Button(text="Click here!", command = clicked) # like screen.listen()
button.pack()

# ENTRY
entry = Entry(width=20)
entry.insert(END, string= "Some text.") # end is like a index which says text is gonna be there.
#entry.get() --> gets text in the input
entry.pack()
entry.focus() # to add cursor 

#Text
text = Text(height=5, width=30)  #Puts cursor in textbox. #5 lines visible at a time
text.focus() #Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
#Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()

#Spinbox
def spinbox_used():
    print(spinbox.get())  #gets the current value in spinbox.
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
def scale_used(value):
    print(value)  #Called with current scale value.
scale = Scale(from_=0, to=100, command=scale_used)
scale.pack(side = "right")

#Checkbutton
def checkbutton_used():
    print(checked_state.get()) #Prints 1 if On button checked, otherwise 0
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#Listbox
def listbox_used(event):
    print(listbox.get(listbox.curselection())) # Gets current selection from listbox

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

# in case of grid, row means column and column means row

window.mainloop() # same functionality as turtle's screen.clickonexit()