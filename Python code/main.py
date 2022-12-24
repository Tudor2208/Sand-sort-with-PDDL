from tkinter import *
import tkinter as tk
import random
import time

text_area = 0
list_of_actions = []
window = ""
my_canvas = ""
bottle_1_1 = ""
bottle_1_2 = ""
bottle_1_3 = ""

bottle_2_1 = ""
bottle_2_2 = ""
bottle_2_3 = ""

bottle_3_1 = ""
bottle_3_2 = ""
bottle_3_3 = ""

bottle_4_1 = ""
bottle_4_2 = ""
bottle_4_3 = ""

bottle_5_1 = ""
bottle_5_2 = ""
bottle_5_3 = ""

colors_in_bottles = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    ['white', 'white', 'white'],
    ['white', 'white', 'white']
]


def generate_game():
    red = 0
    green = 0
    blue = 0
    for j in range(3):
        for i in range(3):
            random_nr = random.randint(1, 3)
            if random_nr == 1 and red < 3:
                fill_bottle(j+1, i+1, "red")
                red += 1
            elif random_nr == 2 and green < 3:
                fill_bottle(j+1, i+1, "green")
                green += 1
            elif random_nr == 3 and blue < 3:
                fill_bottle(j+1, i+1, "blue")
                blue += 1
            elif red < 3:
                fill_bottle(j + 1, i + 1, "red")
                red += 1
            elif green < 3:
                fill_bottle(j + 1, i + 1, "green")
                green += 1
            elif blue < 3:
                fill_bottle(j + 1, i + 1, "blue")
                blue += 1

    for i in range(4, 6):
        fill_bottle(i, 1, 'white')
        fill_bottle(i, 2, 'white')
        fill_bottle(i, 3, 'white')

    text_area.delete(1.0, END)


def fill_bottle(rect_nr, level, color):
    global my_canvas
    colors_in_bottles[rect_nr - 1][level - 1] = color
    if level == 3:
        level = 1
    elif level == 1:
        level = 3

    bottle_name = "bottle_" + str(rect_nr) + "_" + str(level)
    global_vars = globals()
    my_var = global_vars[bottle_name]
    Canvas.itemconfig(my_canvas, fill=color, tagOrId=my_var)


def pour(bottle1, bottle2):
    # from bottle1 to bottle2
    level_white = 0
    level_non_white = 0
    for i in range(3):
        if colors_in_bottles[bottle2 - 1][i] == "white":
            level_white = i+1
            break

    for i in range(3, 1, -1):
        if colors_in_bottles[bottle1 - 1][i-1] != "white":
            level_non_white = i
            break

    text_area.insert('end', '> Pour bottle ' + str(bottle1) + " into bottle " + str(bottle2) + '\n')
    window.update()
    time.sleep(2)
    fill_bottle(bottle2, level_white, colors_in_bottles[bottle1 - 1][level_non_white-1])
    fill_bottle(bottle1, level_non_white, "white")


def do_actions():
    for bottle1, bottle2 in list_of_actions:
        pour(bottle1, bottle2)


def create_start_window():
    global my_canvas, window, text_area
    global bottle_1_1, bottle_1_2, bottle_1_3
    global bottle_2_1, bottle_2_2, bottle_2_3
    global bottle_3_1, bottle_3_2, bottle_3_3
    global bottle_4_1, bottle_4_2, bottle_4_3
    global bottle_5_1, bottle_5_2, bottle_5_3

    window = Tk()
    window.title("Sand-sort-puzzle")
    window.geometry("1300x800")
    window.resizable(False, False)
    window.configure(background='#ecf0ce')
    window_title = Label(text="Sort the sand!", font=('consolas', 30), background='#ecf0ce')
    window_title.pack(side=TOP)
    my_canvas = tk.Canvas(window, bg="#ecf0ce", height=800, width=1300)

    bottle_1_1 = my_canvas.create_rectangle(50, 150, 200, 230, outline="black", fill="white", width="2")

    bottle_1_2 = my_canvas.create_rectangle(50, 230, 200, 320, outline="black", fill="white", width="2")
    bottle_1_3 = my_canvas.create_rectangle(50, 320, 200, 400, outline="black", fill="white", width="2")

    bottle_2_1 = my_canvas.create_rectangle(250, 150, 400, 230, outline="black", fill="white", width="2")
    bottle_2_2 = my_canvas.create_rectangle(250, 230, 400, 320, outline="black", fill="white", width="2")
    bottle_2_3 = my_canvas.create_rectangle(250, 320, 400, 400, outline="black", fill="white", width="2")

    bottle_3_1 = my_canvas.create_rectangle(450, 150, 600, 230, outline="black", fill="white", width="2")
    bottle_3_2 = my_canvas.create_rectangle(450, 230, 600, 320, outline="black", fill="white", width="2")
    bottle_3_3 = my_canvas.create_rectangle(450, 320, 600, 400, outline="black", fill="white", width="2")

    bottle_4_1 = my_canvas.create_rectangle(650, 150, 800, 230, outline="black", fill="white", width="2")
    bottle_4_2 = my_canvas.create_rectangle(650, 230, 800, 320, outline="black", fill="white", width="2")
    bottle_4_3 = my_canvas.create_rectangle(650, 320, 800, 400, outline="black", fill="white", width="2")

    bottle_5_1 = my_canvas.create_rectangle(850, 150, 1000, 230, outline="black", fill="white", width="2")
    bottle_5_2 = my_canvas.create_rectangle(850, 230, 1000, 320, outline="black", fill="white", width="2")
    bottle_5_3 = my_canvas.create_rectangle(850, 320, 1000, 400, outline="black", fill="white", width="2")

    label_b1 = tk.Label(window, text="Bottle 1", font=("Times New Roman", 20), bg="#ecf0ce")
    label_b1.place(x="80", y="470")

    label_b2 = tk.Label(window, text="Bottle 2", font=("Times New Roman", 20), bg="#ecf0ce")
    label_b2.place(x="280", y="470")

    label_b1 = tk.Label(window, text="Bottle 3", font=("Times New Roman", 20), bg="#ecf0ce")
    label_b1.place(x="480", y="470")

    label_b1 = tk.Label(window, text="Bottle 4", font=("Times New Roman", 20), bg="#ecf0ce")
    label_b1.place(x="680", y="470")

    label_b1 = tk.Label(window, text="Bottle 5", font=("Times New Roman", 20), bg="#ecf0ce")
    label_b1.place(x="880", y="470")

    label_actions = tk.Label(window, text="Actions", font=("Times New Roman", 22), bg="#ecf0ce")
    label_actions.place(x="550", y="550")

    text_area = Text(window, height=5, width=70, font=("Times New Roman", 20))
    text_area.place(x="200", y="600")

    btn_solve = tk.Button(window, text="Solve", font=("Times New Roman", 22), command=do_actions, bg="#99baf0")
    btn_solve.place(x="1125", y="250")

    btn_new_game = tk.Button(window, text="New game", font=("Times New Roman", 22), command=generate_game, bg="#99baf0")
    btn_new_game.place(x="1100", y="350")

    my_canvas.pack()

    return window


if __name__ == '__main__':
    window = create_start_window()
    frame = Frame(window, background='#ecf0ce')
    frame.pack()

    generate_game()
    window.mainloop()
