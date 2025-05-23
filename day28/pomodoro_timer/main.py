from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = 0

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    label_timer.config(text="Timer")
    label_check.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 == 0:
        count_down(long_break_sec)
        label_timer.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)   
        label_timer.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        label_timer.config(text="Work", fg=GREEN)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    
    count_min = math.floor(count / 60)
    count_sec = count % 60
    
    canvas.itemconfig(timer_text, text=f"{count_min:02}:{count_sec:02}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count -1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✔"
        label_check.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #

#window
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)



#image
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0 )
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112,image=tomato_img )
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.pack()


#Label timer
label_timer = Label(text="Timer", font=(FONT_NAME, 30, "bold"), bg=YELLOW, fg=GREEN)
label_timer.place(x=45,y=-50)


#label Check
label_check = Label(text="✔",font=(FONT_NAME, 20),bg=YELLOW ,fg=GREEN)



#button start
button_start = Button(text="Start", highlightthickness=0, command=start_timer)
button_start.place(x=-50 ,y=210)


#button reset
button_reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
button_reset.place(x=200 ,y=210)


window.mainloop()
