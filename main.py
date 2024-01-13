import tkinter as tk
import math

# ---------------------------- CONSTANTS ------------------------------- #
CHECK_MARK = "\u2714"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 20
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
stage = 1
reset = None


# ---------------------------- TIMER RESET ------------------------------- #
def on_reset():
    print("reset")
    global reset
    global stage
    heat_text.config(text="Timer", fg=GREEN)
    m_label.config(text="----")
    canvMy.itemconfig(counter_text, text=f"00:00")
    windMy.after_cancel(reset)
    stage = 1


# ---------------------------- TIMER MECHANISM ------------------------------- #
def on_start():
    if stage == 1:
        heat_text.config(text="Work", fg=RED)
        count_down(WORK_MIN * 60)
    elif stage == 2:
        heat_text.config(text="Short Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
        m_label.config(text=CHECK_MARK + "---")
    elif stage == 3:
        heat_text.config(text="Work", fg=RED)
        count_down(WORK_MIN * 60)
    elif stage == 4:
        heat_text.config(text="Short Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
        m_label.config(text=CHECK_MARK + CHECK_MARK + "--")
    elif stage == 5:
        heat_text.config(text="Work", fg=RED)
        count_down(WORK_MIN * 60)
    elif stage == 6:
        heat_text.config(text="Short Break", fg=PINK)
        count_down(SHORT_BREAK_MIN * 60)
        m_label.config(text=CHECK_MARK + CHECK_MARK + CHECK_MARK + "-")
    elif stage == 7:
        heat_text.config(text="Work", fg=RED)
        count_down(WORK_MIN * 60)
    elif stage == 8:
        heat_text.config(text="Long Break", fg=GREEN)
        count_down(LONG_BREAK_MIN * 60)
        m_label.config(text=CHECK_MARK + CHECK_MARK + CHECK_MARK + CHECK_MARK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(times):
    global stage
    global reset

    if times >= 0:
        sec = round((times / 60 % 1) * 60)
        minuets = math.floor(times / 60)
        # adds 0 to digits with only one digit
        if len(str(minuets)) < 2:
            minuets = "0" + str(minuets)
        if len(str(sec)) < 2:
            sec = "0" + str(sec)
        # display digits
        canvMy.itemconfig(counter_text, text=f"{minuets}:{sec}")
        # callback function count_down in order to reduce counter
        reset = windMy.after(1000, count_down, times - 1)
        print(times - 1)
    else:
        stage += 1
        on_start()
    if stage == 9:
        stage = 1


# ---------------------------- UI SETUP ------------------------------- #
windMy = tk.Tk()
windMy.wm_minsize(400, 400)
windMy.wm_maxsize(400, 400)
windMy.wm_title("Pomodoro")
windMy.config(pady=10, padx=70, background=YELLOW)

heat_text = tk.Label(text='Timer', background=YELLOW, fg=GREEN, font=(FONT_NAME, 30, 'bold'))
heat_text.pack()

imgMy = tk.PhotoImage(file="tomato.png")
canvMy = tk.Canvas()
canvMy.config(height=240, width=200, background=YELLOW, highlightthickness=0)
canvMy.pack()
canvMy.create_image(100, 115, image=imgMy)
counter_text = canvMy.create_text(100, 130, text="00:00", fill='white', font=(FONT_NAME, 28, "bold"))
footer_canv = tk.Canvas()
footer_canv.pack()

l_but = tk.Button(footer_canv, text="Start", padx=12, command=on_start)
l_but.grid(row=0, column=0)
m_label = tk.Label(footer_canv, text="----", padx=12, background=YELLOW, font=(FONT_NAME, 20, "bold"), fg=GREEN)
m_label.grid(row=0, column=1)
r_but = tk.Button(footer_canv, text="Reset", padx=12, command=on_reset)
r_but.grid(row=0, column=2)

windMy.mainloop()
