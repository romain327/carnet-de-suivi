import os
import platform
import sys
import tkinter as tk
from tkinter import filedialog as fd
from tkinter import ttk

system = platform.system()

def get_time():
    import time
    return time.strftime("%H:%M:%S") + " - "

def on_school_button_click():
    input_text.set(fd.askopenfilename(title="Sélectionner le fichier CSV académique"))

def on_company_button_click():
    entreprise_text.set(fd.askopenfilename(title="Sélectionner le fichier CSV entreprise"))

def on_export_button_click():
    output_text.set(fd.askdirectory(title="Sélectionner le dossier de sortie"))

def on_logo_button_click():
    img_text.set(fd.askopenfilename(title="Sélectionner le logo"))

def on_intro_button_click():
    intro_text.set(fd.askopenfilename(title="Sélectionner l'introduction"))

def on_eoc_button_click():
    eoc_text.set(fd.askdirectory(title="Sélectionner le dossier d'end of course"))

def on_syntheses_button_click():
    syntheses_text.set(fd.askdirectory(title="Sélectionner le dossier des synthèses"))

def on_conclusion_button_click():
    conclusion_text.set(fd.askopenfilename(title="Sélectionner la conclusion"))

def on_annexes_button_click():
    annexes_text.set(fd.askdirectory(title="Sélectionner le dossier des annexes"))

def read_config(params_names, config_file):
    _config = {}
    with open(config_file, "r") as file:
        for line in file:
            for param in params_names:
                if param in line:
                    _config[param] = line.split("=")[1].replace("\n", "")
    return _config

def format_csv(csv, filename):
    with open(csv, "r", encoding="utf-8") as f:
        lines = f.readlines()

    l = ""
    f = open(filename, 'w', encoding="utf-8")
    for line in lines:
        line = format_string(line)
        if l != "" and line[0].isdigit():
            if line[0].isdigit():
                f.write(l + " \n")
                l = line
        else :
            l += line
    return filename

def format_string(string):
    string = string.replace(", ", "|")
    string = string.replace(",", ";")
    string = string.replace("|", ", ")
    string = string.replace("&", "et")
    string = string.replace("\n", "")
    string = string.replace("\r\n", "")
    string = string.replace('"', "")
    string = string.replace("...", "\ldots")
    string = string.replace("%", "$\\%$")
    return string

def read_eoc(eoc_dir):
    eoc = {}
    for file in os.listdir(eoc_dir):
        with open(eoc_dir + "/" + file, "r", encoding='utf-8') as f:
            eoc[file.replace("_", " ").capitalize().replace(".txt", "")] = f.read()
    return eoc

def read_synthesis(syntheses_dir):
    syntheses = {}
    for file in os.listdir(syntheses_dir):
        with open(syntheses_dir + "/" + file, "r") as f:
            syntheses[file.split('.')[0]] = f.read()
    return syntheses

def on_generate_button_click():
    if test:
        config_file = "tests/config_test"
    else:
        config_file = "config"

    log_text_box.insert(tk.END, get_time() + "Start generation...\n")
    params_names = ["school_file", "company_file", "export_folder", "logo", "student_name", "school_tutor_name", "company_tutor_name", "introduction", "eoc", "synthesis", "conclusion", "annex"]
    params = [input_text.get(), entreprise_text.get(), output_text.get(), img_text.get(), name_text.get(), civilite_ac.get() + tut_ac_text.get(), civilite_ma.get() + ma_text.get(), intro_text.get(), eoc_text.get(), syntheses_text.get(), conclusion_text.get(), annexes_text.get()]

    log_text_box.insert(tk.END, get_time() + "Reading configuration file...\n")
    config = read_config(params_names, config_file)
    log_text_box.insert(tk.END, get_time() + "done.\n")

    for i in range(len(params)):
        if params[i] == "":
            params[i] = config[params_names[i]]

    log_text_box.insert(tk.END, get_time() + "Checking inputs...\n")
    for param in params:
        if param == "":
            log_text_box.insert(tk.END, get_time() + "Error: missing input\n")
            return
    log_text_box.insert(tk.END, get_time() + "done.\n")

    log_text_box.insert(tk.END, get_time() + "Writing configuration file...\n")
    with open(config_file, "w") as file:
        for i in range(len(params)):
            file.write(params_names[i] + "=" + params[i] + "\n")
    log_text_box.insert(tk.END, get_time() + "done.\n")

    log_text_box.insert(tk.END, get_time() + "Reading school file...\n")
    formatted_file = format_csv(params[0], 'format.csv')
    school_data = {}
    with open(formatted_file, "r") as file:
        for line in file:
            split_line = line.split(";")
            if split_line[0] not in school_data:
                school_data[split_line[0]] = []
            school_data[split_line[0]].append(split_line[1:])
    log_text_box.insert(tk.END, get_time() + "done.\n")

    log_text_box.insert(tk.END, get_time() + "Reading company file...\n")
    formatted_file = format_csv(params[1], 'format2.csv')
    company_data = {}
    with open(formatted_file, "r") as file:
        for line in file:
            split_line = line.split(";")
            if split_line[0] not in company_data:
                company_data[split_line[0]] = []
            company_data[split_line[0]].append(split_line[1:])
    log_text_box.insert(tk.END, get_time() + "done.\n")

    log_text_box.insert(tk.END, get_time() + "Reading intro file...\n")
    with open(params[7], "r") as file:
        intro = file.read()

    log_text_box.insert(tk.END, get_time() + "Formatting school data...\n")
    school_text = ""
    eoc = read_eoc(params[8])
    for key in school_data.keys():
        school_text += "\section*{Semaine " + key + "}\n"
        school_text += "{\\footnotesize"
        school_text += "\\" + "begin{tabular*}{\columnwidth}{@{\extracolsep{\\fill}} | p{2cm} | p{5cm} | p{2cm} | p{5cm} |}\n"
        school_text += "\hline\n"
        school_text += "Matière & Description & Evaluation & Commentaire \\\\ \n"
        school_text += "\hline\n"
        for cat in school_data[key]:
            tr = 0
            for i in range(1, len(cat[1])):
                if cat[1][i] == " " and cat[1][i - 1] == "-":
                    tr += 1
            if tr > 1:
                cat[1] = cat[1].replace("- ", " \\newline - ")
            print(cat)
            cat[-1] = cat[-1].replace("\n", "")
            school_text += (cat[0] + " & " + cat[1] + " & " + cat[2] + " & " + cat[3] + "\\\\ \n")
            school_text += "\hline\n"
        school_text += "\end{tabular*}}\n"
        school_text += "\n"
    for key in eoc.keys():
        school_text += "\paragraph*{" + key + ":}" + "\n"
        school_text += eoc[key] + "\\\\ \n"
    log_text_box.insert(tk.END, get_time() + "done.\n")

    log_text_box.insert(tk.END, get_time() + "Formatting company data...\n")
    company_text = ""
    synthesis = read_synthesis(params[9])
    for key in company_data.keys():
        company_text += "\\section*{Semaine " + key + "}\n"
        company_text += "{\\footnotesize"
        company_text += "\\begin{tabular*}{\columnwidth}{@{\extracolsep{\\fill}} | p{4cm} | p{4cm} | p{3cm} | p{3cm} |}\n"
        company_text += "\hline\n"
        company_text += "Activité prévue & Activité réalisée & Commentaire & Compétences \\\\ \n"
        company_text += "\hline\n"
        for cat in company_data[key]:
            tr = 0
            for i in range(1, len(cat[1])):
                if cat[1][i] == " " and cat[1][i - 1] == "-":
                    tr += 1
            if tr > 1:
                cat[1] = cat[1].replace("- ", " \\newline - ")
            cat[-1] = cat[-1].replace("\n", "")
            company_text += (cat[0] + " & " + cat[1] + " & " + cat[2] + " & " + cat[3] + "\\\\ \n")
            company_text += "\hline\n"
        company_text += "\end{tabular*}}\n"
        if key in synthesis:
            company_text += "\paragraph*{Synthèse " + key + ":}" + "\n"
            company_text += synthesis[key] + "\\\\ \n"
    log_text_box.insert(tk.END, get_time() + "done.\n")

    log_text_box.insert(tk.END, get_time() + "Writing conclusion...\n")
    with open(params[10], "r") as file:
        conclusion = file.read()
    log_text_box.insert(tk.END, get_time() + "done.\n")

    log_text_box.insert(tk.END, get_time() + "Writing annexes...\n")
    annexes = ""
    for file in os.listdir(params[11]):
        if file.endswith(".pdf"):
            annexes += "\includepdf{" + params[11] + "/" + file + "}\n"
        if file.endswith(".png"):
            annexes += '\includegraphics[width=\\textwidth]{' + params[11] + "/" + file + "}\n"
    log_text_box.insert(tk.END, get_time() + "done.")

    log_text_box.insert(tk.END, get_time() + "Writing to file...\n")
    with open("template.tex", "r") as file:
        template = file.read()

    template = template.replace("{{school_data}}", school_text)
    template = template.replace("{{company_data}}", company_text)
    template = template.replace("{{student_name}}", params[4])
    template = template.replace("{{school_tutor}}", params[5])
    template = template.replace("{{company_tutor}}", params[6])
    template = template.replace("{{logo}}", params[3].split('.')[0])
    template = template.replace("{{introduction}}", intro.replace('\n', '\\\\'))
    template = template.replace("{{conclusion}}", conclusion.replace('\n', '\\\\'))
    template = template.replace("{{annexes}}", annexes)
    filename = "suivi_" + params[4].replace(" ", "_") + ".tex"
    with open(filename, "w") as file:
        file.write(template)
    log_text_box.insert(tk.END, get_time() + "done.\n")

    log_text_box.insert(tk.END, get_time() + "Compiling PDF...\n")
    if system == "Windows":
        os.system("pdflatex --interaction=nonstopmode " + filename)
        os.system("pdflatex --interaction=nonstopmode " + filename)
        os.system("move " + filename.replace(".tex", ".pdf") + " " + params[2] + "/" + filename.replace(".tex", ".pdf"))
    else:
        os.system("pdflatex --interaction=nonstopmode " + filename)
        os.system("pdflatex --interaction=nonstopmode " + filename)
        os.system("mv " + filename.replace(".tex", ".pdf") + " " + params[2] + "/" + filename.replace(".tex", ".pdf"))
    log_text_box.insert(tk.END, get_time() + "done.\n")

    log_text_box.insert(tk.END, get_time() + "Cleaning up...\n")
    os.remove("format.csv")
    os.remove("format2.csv")
    os.remove(filename)
    os.remove(filename.replace(".tex", ".aux"))
    os.remove(filename.replace(".tex", ".log"))
    os.remove(filename.replace(".tex", ".toc"))
    log_text_box.insert(tk.END, get_time() + "done.\n")
    log_text_box.insert(tk.END, get_time() + "End generation.\n")

root = tk.Tk()
root.geometry("1440x900")

title_label = ttk.Label(root, text="Générateur de carnet de suivi")

# csv entrée
input_label = ttk.Label(root, text="Fichier CSV académique")
input_text = tk.StringVar()
input_textfield = tk.Entry(root, width=80, textvariable=input_text)
input_button = ttk.Button(root, text="Import du fichier CSV", command=on_school_button_click)

# csv entrprise
entreprise_label = ttk.Label(root, text="Fichier CSV entreprise")
entreprise_text = tk.StringVar()
entreprise_textfield = tk.Entry(root, width=80, textvariable=entreprise_text)
entreprise_button = ttk.Button(root, text="Import du fichier CSV", command=on_company_button_click)

# dossier sortie
output_label = ttk.Label(root, text="Dossier de sortie")
output_text = tk.StringVar()
output_textfield = tk.Entry(root, width=80, textvariable=output_text)
output_button = ttk.Button(root, text="Export du fichier PDF", command=on_export_button_click)

# image
img_label = ttk.Label(root, text="Logo entreprise")
img_text = tk.StringVar()
img_textfield = tk.Entry(root, width=80, textvariable=img_text)
img_button = ttk.Button(root, text="Import du logo", command=on_logo_button_click)

# nom - prénom élève
name_label = ttk.Label(root, text="Nom et prénom de l'étudiant")
name_text = tk.StringVar()
name_textfield = tk.Entry(root, width=80, textvariable=name_text)

# tuteur académique
tut_ac_label = ttk.Label(root, text="Nom et prénom du tuteur académique")
civilite_ac = tk.StringVar(root)
civilite_ac.set("")
civilite_ac_menu = tk.OptionMenu(root, civilite_ac, "", "Mme. ", "Mlle. ", "M. ")
tut_ac_text = tk.StringVar()
tut_ac_textfield = tk.Entry(root, width=80, textvariable=tut_ac_text)

# maître d'apprentissage
ma_label = ttk.Label(root, text="Nom et prénom du maître d'apprentissage")
civilite_ma = tk.StringVar(root)
civilite_ma.set("")
civilite_ma_menu = tk.OptionMenu(root, civilite_ma, "", "Mme. ", "Mlle. ", "M. ")
ma_text = tk.StringVar()
ma_textfield = tk.Entry(root, width=80, textvariable=ma_text)

# intro
intro_label = ttk.Label(root, text="Introduction")
intro_text = tk.StringVar()
intro_textfield = tk.Entry(root, width=80, textvariable=intro_text)
intro_button = ttk.Button(root, text="Introduction", command=on_intro_button_click)

#end of course
eoc_label = ttk.Label(root, text="End of course")
eoc_text = tk.StringVar()
eoc_textfield = tk.Entry(root, width=80, textvariable=eoc_text)
eoc_button = ttk.Button(root, text="End of course", command=on_eoc_button_click)

# synthèses
syntheses_label = ttk.Label(root, text="Dossier des synthèses")
syntheses_text = tk.StringVar()
syntheses_textfield = tk.Entry(root, width=80, textvariable=syntheses_text)
syntheses_button = ttk.Button(root, text="Synthèses", command=on_syntheses_button_click)

# conclusion
conclusion_label = ttk.Label(root, text="Conclusion")
conclusion_text = tk.StringVar()
conclusion_textfield = tk.Entry(root, width=80, textvariable=conclusion_text)
conclusion_button = ttk.Button(root, text="Conclusion", command=on_conclusion_button_click)

# annexes
annexes_label = ttk.Label(root, text="Dossier des annexes")
annexes_text = tk.StringVar()
annexes_textfield = tk.Entry(root, width=80, textvariable=annexes_text)
annexes_button = ttk.Button(root, text="Annexes", command=on_annexes_button_click)

start_button = ttk.Button(root, text="Générer", command=on_generate_button_click)

close_button = ttk.Button(root, text="Fermer", command=root.destroy)

log_text_box = tk.Text(root, height=10, width=100)

# positions
title_label.grid(row=0, column=0, pady=10)
close_button.grid(row=0, column=2, pady=10)
input_label.grid(row=1, column=0, pady=5)
input_button.grid(row=1, column=1, pady=5)
input_textfield.grid(row=1, column=2, pady=5)
entreprise_label.grid(row=2, column=0, pady=5)
entreprise_button.grid(row=2, column=1, pady=5)
entreprise_textfield.grid(row=2, column=2, pady=5)
output_label.grid(row=3, column=0, pady=5)
output_button.grid(row=3, column=1, pady=5)
output_textfield.grid(row=3, column=2, pady=5)
img_label.grid(row=4, column=0, pady=5)
img_button.grid(row=4, column=1, pady=5)
img_textfield.grid(row=4, column=2, pady=5)
name_label.grid(row=5, column=0, pady=5)
name_textfield.grid(row=5, column=2, pady=5)
tut_ac_label.grid(row=6, column=0, pady=5)
civilite_ac_menu.grid(row=6, column=1, pady=5)
tut_ac_textfield.grid(row=6, column=2, pady=5)
ma_label.grid(row=7, column=0, pady=5)
civilite_ma_menu.grid(row=7, column=1, pady=5)
ma_textfield.grid(row=7, column=2, pady=5)
intro_label.grid(row=8, column=0, pady=5)
intro_button.grid(row=8, column=1, pady=5)
intro_textfield.grid(row=8, column=2, pady=5)
eoc_label.grid(row=9, column=0, pady=5)
eoc_button.grid(row=9, column=1, pady=5)
eoc_textfield.grid(row=9, column=2, pady=5)
syntheses_label.grid(row=10, column=0, pady=5)
syntheses_button.grid(row=10, column=1, pady=5)
syntheses_textfield.grid(row=10, column=2, pady=5)
conclusion_label.grid(row=11, column=0, pady=5)
conclusion_button.grid(row=11, column=1, pady=5)
conclusion_textfield.grid(row=11, column=2, pady=5)
annexes_label.grid(row=12, column=0, pady=5)
annexes_button.grid(row=12, column=1, pady=5)
annexes_textfield.grid(row=12, column=2, pady=5)
start_button.grid(row=13, column=0, columnspan=2, pady=10)
log_text_box.grid(row=14, column=0, columnspan=3, pady=10)

test = False
if len(sys.argv) > 1:
    if sys.argv[1] == "-t":
        test=True
        os.makedirs("tests/output", exist_ok=True)
        config_file = "tests/config_test"
        input_text.set("tests/school.csv")
        entreprise_text.set("tests/company.csv")
        output_text.set("tests/output")
        img_text.set("tests/logo.png")
        name_text.set("Kujo Jotaro")
        tut_ac_text.set("Brando DIO")
        ma_text.set("Polnareff Jean-Pierre")
        intro_text.set("tests/intro.txt")
        eoc_text.set("tests/eoc")
        syntheses_text.set("tests/syntheses")
        conclusion_text.set("tests/conclusion.txt")
        annexes_text.set("tests/annexes")
        log_text_box.insert(tk.END, get_time() + "Test mode enabled.\n")

root.mainloop()