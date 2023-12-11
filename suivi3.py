import os

print("installation des librairies...")
os.system("sudo apt install texlive")
os.system("sudo apt install python3-pip")
os.system("sudo apt install python3-tk")
os.system("python3 -m pip install --upgrade --break-system-packages pip")
os.system("python3 -m pip install --break-system-packages pathlib")

import tkinter as tk
from tkinter import filedialog as fd
import sys
from pathlib import Path
from tkinter import ttk
from tkinter import messagebox


def start():
    start_param()
    inputfile = input_text.get()
    entreprisefile = entreprise_text.get()
    outputpath = output_text.get()
    dict = {}
    dict2 = {}
    w = ""
    Line = []

    print("formatting csv...")
    inputfile = format_csv(inputfile)
    print("done")

    print("creating the model...")
    s = open("template1.tex", mode='r', encoding='utf-8-sig').read()
    open("template1.tex", mode='w', encoding='utf-8').write(s)
    with open("template1.tex", 'r', encoding="utf-8") as f:
        template1 = f.read()
    f.close()

    s = open("template2.tex", mode='r', encoding='utf-8-sig').read()
    open("template2.tex", mode='w', encoding='utf-8').write(s)
    with open("template2.tex", 'r', encoding="utf-8") as f:
        template2 = f.read()
    f.close()

    s = open("template3.tex", mode='r', encoding='utf-8-sig').read()
    open("template3.tex", mode='w', encoding='utf-8').write(s)
    with open("template3.tex", 'r', encoding="utf-8") as f:
        template3 = f.read()
    f.close()

    s = open("template4.tex", mode='r', encoding='utf-8-sig').read()
    open("template4.tex", mode='w', encoding='utf-8').write(s)
    with open("template4.tex", 'r', encoding="utf-8") as f:
        template4 = f.read()
    f.close()

    with open("img.tex", 'r', encoding="utf-8") as f:
        img = f.read()
    f.close()

    with open("nom.tex", 'r', encoding="utf-8") as f:
        name = f.read()
    f.close()

    with open("tuteur.tex", 'r', encoding="utf-8") as f:
        tuteur = f.read()
    f.close()

    with open("ma.tex", 'r', encoding="utf-8") as f:
        ma = f.read()
    f.close()

    with open("annexes.tex", 'r', encoding="utf-8") as f:
        annexes = f.read()
    f.close()

    print("done")

    print("reading " + inputfile)
    s = open(inputfile, mode='r', encoding='utf-8-sig').read()
    open(inputfile, mode='w', encoding='utf-8').write(s)
    with open(inputfile, 'r', encoding="utf-8") as f:
        for line in f:
            for char in line:
                if char == ';' or char == '\n':
                    Line.append(w)
                    w = ""
                else:
                    w += char
            if Line[0] not in dict:
                dict[Line[0]] = []
            dict[Line[0]].append(Line[1:])
            Line = []
    f.close()

    w = ""

    s = open(entreprisefile, mode='r', encoding='utf-8-sig').read()
    open(entreprisefile, mode='w', encoding='utf-8').write(s)
    with open(entreprisefile, 'r', encoding="utf-8") as f:
        for line in f:
            for char in line:
                if char == ';' or char == '\n':
                    Line.append(w)
                    w = ""
                else:
                    w += char
            if Line[0] not in dict2:
                dict2[Line[0]] = []
            dict2[Line[0]].append(Line[1:])
            Line = []
    f.close()
    print("done")
    print(dict2)

    with open("suivi.tex", 'w', encoding="utf-8") as f:
        f.write(template1)
        f.write("\n")
        f.write(name)
        f.write(template2)
        f.write("\n")
        f.write(tuteur)
        f.write("\n")
        f.write(ma)
        f.write("\n")
        f.write(template3)
        f.write("\n")
        f.write(img)
        f.write("\n")
        f.write(template4)
        f.write("\n")
    f.close()
    print("done")

    print("generating " + outputpath + "/carnet.pdf")
    s = open("suivi.tex", mode='r', encoding='utf-8-sig').read()
    open("suivi.tex", mode='w', encoding='utf-8').write(s)
    with open("suivi.tex", 'a', encoding="utf-8") as f:
        f.write("\chapter{Suivi académique}\n")
        for key in dict.keys():
            f.write("\section*{Semaine " + key + "}\n")
            f.write("\\" + "begin{tabular}{|l|l|l|l|}\n")
            f.write("\hline\n")
            f.write("Matière & Description & Evaluation & Commentaire \\\\ \n")
            f.write("\hline\n")
            for cat in dict[key]:
                f.write(cat[0] + " & " + cat[1] + " & " + cat[2] + " & " + cat[3] + " \\\\ \n")
                f.write("\hline\n")
            f.write("\end{tabular}\n")
            f.write("\n")
    f.close()

    s = open("suivi.tex", mode='r', encoding='utf-8-sig').read()
    open("suivi.tex", mode='w', encoding='utf-8').write(s)
    with open("suivi.tex", 'a', encoding="utf-8") as f:
        f.write("\chapter{Suivi en entreprise}\n")
        for key in dict2.keys():
            f.write("\section*{Semaine " + key + "}\n")
            f.write("\\" + "begin{tabular}{|l|l|l|l|}\n")
            f.write("\hline\n")
            f.write("Activité & Description & Evaluation & Commentaire \\\\ \n")
            f.write("\hline\n")
            for cat in dict2[key]:
                f.write(cat[0] + " & " + cat[1] + " & " + cat[2] + " & " + cat[3] + " \\\\ \n")
                f.write("\hline\n")
            f.write("\end{tabular}\n")
            f.write("\n")
    f.close()
    print("done")

    text = open("conclusion.txt", mode='r', encoding='utf-8').read()

    s = open("suivi.tex", mode='r', encoding='utf-8-sig').read()
    open("suivi.tex", mode='w', encoding='utf-8').write(s)
    with open("suivi.tex", 'a', encoding="utf-8") as f:
        f.write("\chapter{Conclusion}\n")
        f.write(text)
        f.write("\chapter{Annexes}\n")
        f.write(annexes)
        f.write("\end{document}")
    f.close()
    print("done")
    print("making pdf...")
    os.system("pdflatex suivi.tex")
    os.system("pdflatex suivi.tex")
    os.system("mv suivi.pdf " + outputpath)
    os.system("rm suivi.aux suivi.log suivi.toc suivi.tex format.csv")
    print("done")


def format_csv(file):
    l = ""
    line_list = []

    s = open(file, mode='r', encoding='utf-8-sig').read()
    open(file, mode='w', encoding='utf-8').write(s)
    with open(file, 'r', encoding="utf-8") as f:
        for line in f:
            l = line
            line_list.append(l)
    f.close()

    w = open("format.csv", 'w', encoding="utf-8")
    for i in range(1, len(line_list)):
        if 48 <= ord(line_list[i][0]) <= 57:
            l = line_list[i][:-1]
            j = 1
            if i + j < len(line_list):
                while ord(line_list[i + j][0]) < 48 or 57 < ord(line_list[i + j][0]):
                    lint = line_list[i + j][:-1]
                    l += str(lint)
                    j += 1

            l = l.replace(", ", "|")
            l = l.replace(",", ";")
            l = l.replace("|", ", ")
            l = l.replace("&", "et")
            l = l.replace('"', '')
            w.write(l + "\n")
            l = ""
    w.close()
    return "format.csv"


def start_param():
    print("writing parameters...")
    write_img()
    write_name()
    write_tut_ac()
    write_ma()
    write_annexes()
    write_intro()
    write_conclusion()
    print("done")


def select_input():
    filetypes = (('Csv files', '*.csv'), ('All files', '*.*'))
    filename = fd.askopenfilename(title='Open a file', initialdir=Path(sys.executable).parent, filetypes=filetypes)
    input_text.set(filename)


def select_entreprise():
    filetypes = (('Csv files', '*.csv'), ('All files', '*.*'))
    filename = fd.askopenfilename(title='Open a file', initialdir=Path(sys.executable).parent, filetypes=filetypes)
    entreprise_text.set(filename)


def select_output():
    directory = fd.askdirectory()
    output_text.set(directory)


def select_img():
    filetypes = (('Jpg files', '*.jpg'), ('Png files', '*.png'), ('All files', '*.*'))
    filename = fd.askopenfilename(title='Open a file', initialdir=Path(sys.executable).parent, filetypes=filetypes)
    img_text.set(filename)


def select_annexes():
    annexes_directory = fd.askdirectory()
    annexes_text.set(annexes_directory)


def write_img():
    if (img_text.get() == ""):
        return False

    img_path = img_text.get()
    with open("img.tex", 'w', encoding="utf-8") as f:
        f.write("\includegraphics[width=\\textwidth]{" + img_path + "}\n")
    f.close()
    return True


def write_name():
    if (name_text.get() == ""):
        return False

    name = name_text.get()
    first = name.split(" ")[1] + "\\\\"
    last = "\\textsc{" + name.split(" ")[0] + "}"
    with open("nom.tex", 'w', encoding="utf-8") as f:
        f.write(last + " " + first)
        f.write("promotion 2023-2026")
    f.close()
    return True


def write_tut_ac():
    if (tut_ac_text.get() == ""):
        return False

    civ = civilite.get()
    tut = ""
    if civ == "Mme." or civ == "Mlle.":
        tut = "Tutrice"
    else:
        tut = "Tuteur"
    t = tut_ac_text.get()
    text = "\emph{" + tut + " académique:}\\\\ " + civ + " \\textsc{" + t.split(" ")[0] + "} " + t.split(" ")[
        1] + "\\\\"
    with open("tuteur.tex", 'w', encoding="utf-8") as f:
        f.write(text)
    f.close()
    return True


def write_ma():
    if (ma_text.get() == ""):
        return False

    civ = civilite2.get()
    m = ma_text.get()
    text = "\emph{Maître d'apprentissage:}\\\\ " + civ + " \\textsc{" + m.split(" ")[0] + "} " + m.split(" ")[
        1] + "\\\\"
    with open("ma.tex", 'w', encoding="utf-8") as f:
        f.write(text)
    f.close()
    return True


def write_annexes():
    if (annexes_text.get() == ""):
        return False

    annexes_list = os.listdir(annexes_text.get())
    with open("annexes.tex", 'w', encoding="utf-8") as f:
        for annex in annexes_list:
            annex_path = annexes_text.get() + "/" + annex
            annex_extension = annex.split(".")[1]
            if annex_extension == "pdf":
                f.write("\includepdf[pages=-]{" + annex_path + "}\n")
            elif annex_extension == "jpg" or annex_extension == "png":
                f.write("\includegraphics[width=\\textwidth]{" + annex_path + "}\n")
            else:
                messagebox.showinfo("Erreur", "Le fichier " + annex_path + " n'est pas un fichier pdf, jpg ou png.")
    f.close()
    return True


def select_intro():
    filetypes = (('Texte', '*.txt'), ('All files', '*.*'))
    intro = fd.askopenfilename(title='Open a file', initialdir=Path(sys.executable).parent, filetypes=filetypes)
    intro_text.set(intro)


def write_intro():
    if (intro_text.get() == ""):
        return False

    intro_path = intro_text.get()
    w = open(intro_path, 'r', encoding="utf-8")
    text = w.read()
    w.close()

    f = open("template4.tex", mode='w', encoding='utf-8')
    f.write("\end{center}")
    f.write("\end{titlepage}")
    f.write("\setcounter{tocdepth}{1}")
    f.write("\\tableofcontents" + "\n")
    f.write("\chapter{Introduction}" + "\n")
    f.write(text)
    f.close()
    return True


def select_conclusion():
    filetypes = (('Texte', '*.txt'), ('All files', '*.*'))
    conclusion = fd.askopenfilename(title='Open a file', initialdir=Path(sys.executable).parent, filetypes=filetypes)
    conclusion_text.set(conclusion)


def write_conclusion():
    if (conclusion_text.get() == ""):
        return False

    conclusion_path = conclusion_text.get()
    w = open(conclusion_path, 'r', encoding="utf-8")
    text = w.read()
    w.close()

    f = open("conclusion.txt", mode='w', encoding='utf-8')
    f.write(text)
    f.close()
    return True


root = tk.Tk()
root.geometry("800x600")

title_label = ttk.Label(root, text="Générateur de carnet de suivi")

# csv entrée
input_label = ttk.Label(root, text="Fichier CSV académique")
input_text = tk.StringVar()
input_textfield = tk.Entry(root, width=50, textvariable=input_text)
# input_textfield.pack()
input_button = ttk.Button(root, text="Import du fichier CSV", command=select_input)
# input_button.pack(expand=True)

# csv entrprise
entreprise_label = ttk.Label(root, text="Fichier CSV entreprise")
entreprise_text = tk.StringVar()
entreprise_textfield = tk.Entry(root, width=50, textvariable=entreprise_text)
# entreprise_textfield.pack()
entreprise_button = ttk.Button(root, text="Import du fichier CSV", command=select_entreprise)
# entreprise_button.pack(expand=True)

# dossier sortie
output_label = ttk.Label(root, text="Dossier de sortie")
output_text = tk.StringVar()
output_textfield = tk.Entry(root, width=50, textvariable=output_text)
# output_textfield.pack()
output_button = ttk.Button(root, text="Export du fichier PDF", command=select_output)
# output_button.pack(expand=True)

start_button = ttk.Button(root, text="Lancer", command=start)
# start_button.pack(expand=True)

param_label = ttk.Label(root, text="Paramètres")

# image
img_label = ttk.Label(root, text="Logo entreprise")
img_text = tk.StringVar()
img_textfield = tk.Entry(root, width=50, textvariable=img_text)
# img_textfield.pack()
img_button = ttk.Button(root, text="Import du logo", command=select_img)
# img_button.pack(expand=True)

# nom - prénom élève
name_label = ttk.Label(root, text="Nom et prénom de l'étudiant")
name_text = tk.StringVar()
name_textfield = tk.Entry(root, width=50, textvariable=name_text)
# name_textfield.pack()

# tuteur académique
tut_ac_label = ttk.Label(root, text="Nom et prénom du tuteur académique")
civilite = tk.StringVar(root)
civilite.set("Mme.")
w = tk.OptionMenu(root, civilite, "Mme.", "Mlle.", "M.")
# w.pack()
tut_ac_text = tk.StringVar()
tut_ac_textfield = tk.Entry(root, width=50, textvariable=tut_ac_text)
# tut_ac_textfield.pack()

# maître d'apprentissage
ma_label = ttk.Label(root, text="Nom et prénom du maître d'apprentissage")
civilite2 = tk.StringVar(root)
civilite2.set("Mme.")
w2 = tk.OptionMenu(root, civilite2, "Mme.", "Mlle.", "M.")
# w2.pack()
ma_text = tk.StringVar()
ma_textfield = tk.Entry(root, width=50, textvariable=ma_text)
# ma_textfield.pack()

# intro
intro_label = ttk.Label(root, text="Introduction")
intro_text = tk.StringVar()
intro_textfield = tk.Entry(root, width=50, textvariable=intro_text)
intro_button = ttk.Button(root, text="Introduction", command=select_intro)
# intro_textfield.pack()

# conclusion
conclusion_label = ttk.Label(root, text="Conclusion")
conclusion_text = tk.StringVar()
conclusion_textfield = tk.Entry(root, width=50, textvariable=conclusion_text)
conclusion_button = ttk.Button(root, text="Conclusion", command=select_conclusion)
# conclusion_textfield.pack()

# annexes
annexes_label = ttk.Label(root, text="Dossier des annexes")
annexes_text = tk.StringVar()
annexes_textfield = tk.Entry(root, width=50, textvariable=annexes_text)
# annexes_textfield.pack()
annexes_button = ttk.Button(root, text="Annexes", command=select_annexes)
# annexes_button.pack(expand=True)

close_button = ttk.Button(root, text="Fermer", command=root.destroy)
# close_button.pack(expand=True)

# positions
title_label.grid(row=0, column=0, columnspan=2, pady=10)
input_label.grid(row=1, column=0, pady=5)
input_button.grid(row=1, column=1, pady=5)
input_textfield.grid(row=1, column=2, pady=5)
entreprise_label.grid(row=2, column=0, pady=5)
entreprise_button.grid(row=2, column=1, pady=5)
entreprise_textfield.grid(row=2, column=2, pady=5)
output_label.grid(row=3, column=0, pady=5)
output_button.grid(row=3, column=1, pady=5)
output_textfield.grid(row=3, column=2, pady=5)
start_button.grid(row=4, column=0, pady=10)
param_label.grid(row=5, column=0, columnspan=2, pady=10)
img_label.grid(row=6, column=0, pady=5)
img_button.grid(row=6, column=1, pady=5)
img_textfield.grid(row=6, column=2, pady=5)
name_label.grid(row=7, column=0, pady=5)
name_textfield.grid(row=7, column=2, pady=5)
tut_ac_label.grid(row=8, column=0, pady=5)
w.grid(row=8, column=1, pady=5)
tut_ac_textfield.grid(row=8, column=2, pady=5)
ma_label.grid(row=9, column=0, pady=5)
w2.grid(row=9, column=1, pady=5)
ma_textfield.grid(row=9, column=2, pady=5)
intro_label.grid(row=10, column=0, pady=5)
intro_button.grid(row=10, column=1, pady=5)
intro_textfield.grid(row=10, column=2, pady=5)
conclusion_label.grid(row=11, column=0, pady=5)
conclusion_button.grid(row=11, column=1, pady=5)
conclusion_textfield.grid(row=11, column=2, pady=5)
annexes_label.grid(row=12, column=0, pady=5)
annexes_button.grid(row=12, column=1, pady=5)
annexes_textfield.grid(row=12, column=2, pady=5)
close_button.grid(row=13, column=0, pady=10)
root.mainloop()