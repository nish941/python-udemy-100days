import tkinter, math, time
from urllib import response
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BLUE = "#0000ff"
PURPLE = "#6a5acd"
timer = None
reps = 0
# ---------------------------- 4 - TIMER RESET ------------------------------- # 

def resettime():
    window.after_cancel(timer)  # in-built command
    canvas.itemconfig(new_text, text ="00:00")
    label1.config(text = "WORK")
    label3.config(text= "")
    global reps
    reps = 0

# ---------------------------- 3 - TIMER MECHANISM ------------------------------- # 

def starttime():
    global reps 
    reps+=1
    if reps ==1 or reps ==3 or reps ==5 or reps ==7:
        count = 25
    elif reps ==2 or reps ==4 or reps ==6:
        count = 5
        label2.config(text = "BREAK", fg= BLUE)
    else:
        count = 20
        label2.config(text = "BREAK", fg=PURPLE)

    countdown(count*60)
# ---------------------------- 2 - COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):
    min = math.floor(count/60)
    sec = count%60
    if sec<10:
        sec = f"0{sec}"
    canvas.itemconfig(new_text, text = f"{min}:{sec}")
    if count > -1:
        global timer
        timer = window.after(1000,countdown,count-1)  # we need to cancel it in case of reset
    else:
        starttime() # otherwise it will end only when reps = 1
        mark = " ✔ "
        for n in range(math.floor(reps/2)):
            textnow += mark
        label3.config(text = textnow)

# ---------------------------- 1 - UI SETUP ------------------------------- #

window = tkinter.Tk()
window.minsize(width = "250", height = "250")
window.title("Pomodoro Strategy")
window.config(padx = 100, pady = 100, bg = GREEN)

canvas = tkinter.Canvas(width = "220", height = "220",bg = GREEN) #, highlightthickness=0)
tomato_pic = tkinter.PhotoImage(file = "./pomodoro_strategy/tomato.png") # format conversion for canvas
canvas.create_image(110,110,image = tomato_pic)
new_text = canvas.create_text(110,130, text= "00:00", fill = "white" ,font = ("Courier", 25, "bold"))
canvas.grid(row = 2, column = 1)

label1 = tkinter.Label(text="TIMER", font = ("Ariel", 35, "bold"), fg = YELLOW, bg = GREEN)
label1.grid(row = 0, column = 1)

label2 = tkinter.Label(text="WORK", font = ("Ariel", 25, "bold"), fg = PINK, bg = GREEN)
label2.grid(row = 1, column = 1)

label3 = tkinter.Label( font = ("Ariel", 24, "bold"), bg = GREEN)
label3.grid(row = 4, column = 1)

button1 = tkinter.Button(text="START",font = ("Ariel", 24, "bold"), command = starttime)# like screen.listen()
button1.grid(row = 3, column = 0)

button2 = tkinter.Button(text="RESET",font = ("Ariel", 24, "bold"), command = resettime) # like screen.listen()
button2.grid(row = 3, column = 2)

window.mainloop()