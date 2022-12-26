import subprocess
from tkinter import *
import tkinter as tk
import random
import time

reds = []
greens = []
blues = []

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

colors_in_bottles = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    ['white', 'white', 'white']
]


def convert_string_to_action(string):
    # string = (pour-3-to-0 bottle1 bottle4 g1 r3)
    tokens = string.split("bottle")
    if len(tokens) == 3:
        first_bottle = int(tokens[1])
        second_bottle = int(tokens[2][0])
        tpl = (first_bottle, second_bottle)
        return tpl

    return None


def parse_plan_file(file_path):
    with open(file_path, "r") as f:
        lines = [line.rstrip('\n') for line in f]
        for line in lines:
            action = convert_string_to_action(line)
            if action is not None:
                list_of_actions.append(action)


def get_init_statements():
    global reds, blues, greens
    reds = ["R1", "R2", "R3"]
    greens = ["G1", "G2", "G3"]
    blues = ["B1", "B2", "B3"]
    init_statements = ""

    top1 = ""
    top2 = ""
    top3 = ""

    for i in range(3):
        random_clr = ""
        if colors_in_bottles[i][2] == 'red':
            random_clr = random.choice(reds)
            init_statements += "(on-top bottle" + str(i + 1) + " " + random_clr + ") \n"
            reds.remove(random_clr)
        elif colors_in_bottles[i][2] == 'green':
            random_clr = random.choice(greens)
            init_statements += "(on-top bottle" + str(i + 1) + " " + random_clr + ") \n"
            greens.remove(random_clr)
        elif colors_in_bottles[i][2] == 'blue':
            random_clr = random.choice(blues)
            init_statements += "(on-top bottle" + str(i + 1) + " " + random_clr + ") \n"
            blues.remove(random_clr)

        if i == 0:
            top1 = random_clr
        elif i == 1:
            top2 = random_clr
        else:
            top3 = random_clr

    colors = []
    for i in range(3):
        for j in range(2):
            if colors_in_bottles[i][j] == "red":
                clr = random.choice(reds)
                colors.append(clr)
                reds.remove(clr)
            elif colors_in_bottles[i][j] == "green":
                clr = random.choice(greens)
                colors.append(clr)
                greens.remove(clr)
            else:
                clr = random.choice(blues)
                colors.append(clr)
                blues.remove(clr)

        if i == 0:
            colors.append(top1)
        elif i == 1:
            colors.append(top2)
        else:
            colors.append(top3)

    init_statements += "\n"

    for i in range(0, 7, 3):
        init_statements += "(is-on " + colors[i] + " " + colors[i+1] + ") \n"
        init_statements += "(is-on " + colors[i+1] + " " + colors[i+2] + ") \n"

    return init_statements


def generate_game():
    global list_of_actions
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
                fill_bottle(j+1, i+1, "red")
                red += 1
            elif green < 3:
                fill_bottle(j+1, i + 1, "green")
                green += 1
            elif blue < 3:
                fill_bottle(j+1, i+1, "blue")
                blue += 1

    fill_bottle(4, 1, 'white')
    fill_bottle(4, 2, 'white')
    fill_bottle(4, 3, 'white')

    statements = get_init_statements()
    generate_problem_file('../part1', '../part2', statements)
    subprocess.check_call(['./fast-downward.py', 'domain_sand_sort.PDDL', 'problem_sand_sort2.PDDL', '--search', "astar(blind())"], cwd='../downward')
    list_of_actions = []
    parse_plan_file('../downward/sas_plan')


def generate_problem_file(part1, part2, statements):
    with open(part1, "r") as f1:
        with open(part2, "r") as f2:
            file1 = f1.read()
            file2 = f2.read()
            new_file = file1 + statements + file2
            with open('../downward/problem_sand_sort2.PDDL', "w") as f:
                f.write(new_file)


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

    for i in range(3, 0, -1):
        if colors_in_bottles[bottle1 - 1][i-1] != "white":
            level_non_white = i
            break

    nr_of_lines = int(text_area.index('end').split('.')[0]) - 1
    if nr_of_lines == 6:
        text_area.delete(1.0, END)

    text_area.insert('end', '> Pour bottle ' + str(bottle1) + " into bottle " + str(bottle2) + '\n')
    window.update()
    time.sleep(1.5)
    fill_bottle(bottle2, level_white, colors_in_bottles[bottle1 - 1][level_non_white-1])
    fill_bottle(bottle1, level_non_white, "white")


def do_actions():
    text_area.delete(1.0, END)
    for bottle1, bottle2 in list_of_actions:
        pour(bottle1, bottle2)

    text_area.delete(1.0, END)
    text_area.insert('end', 'Done!')


def create_start_window():
    global my_canvas, window, text_area
    global bottle_1_1, bottle_1_2, bottle_1_3
    global bottle_2_1, bottle_2_2, bottle_2_3
    global bottle_3_1, bottle_3_2, bottle_3_3
    global bottle_4_1, bottle_4_2, bottle_4_3

    window = Tk()
    window.title("Sand-sort-puzzle")
    window.geometry("1200x800")
    window.resizable(False, False)
    window.configure(background='#ecf0ce')
    window_title = Label(text="Sort the sand!", font=('consolas', 30), background='#ecf0ce')
    window_title.pack(side=TOP)
    my_canvas = tk.Canvas(window, bg="#ecf0ce", height=800, width=1200)

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

    label_b1 = tk.Label(window, text="Bottle 1", font=("Times New Roman", 20), bg="#ecf0ce")
    label_b1.place(x="80", y="470")

    label_b2 = tk.Label(window, text="Bottle 2", font=("Times New Roman", 20), bg="#ecf0ce")
    label_b2.place(x="280", y="470")

    label_b3 = tk.Label(window, text="Bottle 3", font=("Times New Roman", 20), bg="#ecf0ce")
    label_b3.place(x="480", y="470")

    label_b4 = tk.Label(window, text="Bottle 4", font=("Times New Roman", 20), bg="#ecf0ce")
    label_b4.place(x="680", y="470")

    label_actions = tk.Label(window, text="Actions", font=("Times New Roman", 22), bg="#ecf0ce")
    label_actions.place(x="550", y="550")

    text_area = Text(window, height=5, width=70, font=("Times New Roman", 20))
    text_area.place(x="200", y="600")

    btn_solve = tk.Button(window, text="Solve", font=("Times New Roman", 22), command=do_actions, bg="#99baf0")
    btn_solve.place(x="1025", y="250")

    btn_new_game = tk.Button(window, text="New game", font=("Times New Roman", 22), command=generate_game, bg="#99baf0")
    btn_new_game.place(x="1000", y="350")

    my_canvas.pack()

    return window


if __name__ == '__main__':

    window = create_start_window()
    frame = Frame(window, background='#ecf0ce')
    frame.pack()

    generate_game()
    text_area.insert('end', 'Press the button "Solve" for sorting the sand...')
    window.mainloop()
