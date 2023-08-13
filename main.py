from tkinter import *


PROMPT = "in a faraway land a young hero sets out on an epic journey to save their village from a fearsome\n"\
                    " dragon they must find the legendary sword of light to defeat the dragon and restore peace to\n"\
                    " the land along the way they meet quirky companions who join them in their quest they face\n"\
                    " many challenges and dangers but their determination never wavers will they succeed in their\n"\
                    " mission or will the dragon's darkness consume them find out in this action-packed adventure full\n"\
                    " of bravery and magic let your imagination soar as you follow the hero's path in a world of mythical\n"\
                    " creatures and ancient legends"

TIMER = 60


def start():
    start_button.destroy()
    text.config(state="normal")
    timer(TIMER)


def timer(count):
    timer_label = Label(text=f"Time Left: {count}sec", font=("Courier", 10, "bold"))
    timer_label.grid(row=1, column=3)
    if count > 0:
        window.after(1000, timer, count-1)
    else:
        text.config(state="disabled")
        text_entry = text.get("1.0", END)
        check(text_entry)


def check(entry):
    prompt_list = PROMPT.split(" ")
    entry_list = entry.split(" ")
    correct_words = 0
    for i in range(len(entry_list)):
        if prompt_list[i] == entry_list[i]:
            correct_words += 1
    print(f"{correct_words} wpm")
    result(correct_words)


def result(wpm):
    intro_label.destroy()
    prompt.destroy()
    text.destroy()
    result_label = Label(text=f"Your typing speed is: {wpm} wpm.", font=("Arial", 25, "bold"))
    result_label.grid(row=2, column=2)


window = Tk()
window.title("Typing Speed Test")
window.config(padx=50, pady=50)

intro_label = Label(text="Type the following prompt:", font=("Arial", 15, "bold"))
intro_label.grid(row=1, column=1)

prompt = Label(text=PROMPT, font=("Arial", 13, "normal"))
prompt.grid(row=2, column=1, columnspan=3)

text = Text(height=15, width=100, state="disabled")
text.grid(row=3, column=1, columnspan=3)

start_button = Button(text="Start", command=start)
start_button.grid(row=1, column=2)
window.mainloop()
