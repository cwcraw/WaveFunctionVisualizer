from explanations import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk
from WaveFunction import WaveCalc
import matplotlib
matplotlib.use("TkAgg")

# Functions


def download_callback(val, vec):
    np.savetxt("E_val.csv", val, delimiter=",")
    np.savetxt("E_val_rel.csv", val/val[0], delimiter=",")
    np.savetxt("E_vec.csv", vec, delimiter=",")
    np.savetxt("E_vec_sq.csv", vec*vec, delimiter=",")


def make_display(q_num, row_num, col_num, Vec):
    E_vec_figure = Figure(figsize=(4, 4), dpi=70)
    E_vec_plot = E_vec_figure.add_subplot(
        1, 1, 1, xlabel='Position', title="Energy Level #{}'s Probablity Density".format(q_num+1))
    E_vec_plot.plot(x, Vec[:, q_num]**2)
    E_vec_canvas = FigureCanvasTkAgg(E_vec_figure, mainframe)
    E_vec_canvas.get_tk_widget().grid(row=row_num, column=col_num)
    return E_vec_canvas


def update_displays(*args):
    lower_text.configure(text="{}".format(pot_text[pot_var.get()]))
    E_val, E_vec, V, x = WaveCalc(pot_dict[pot_var.get()])
    # This plots the Potential initial potential for a particle in a box
    V_figure = Figure(figsize=(4, 4), dpi=70)
    V_plot = V_figure.add_subplot(
        1, 1, 1, xlabel='Position', title="Plot of Potential Energy")
    V_plot.plot(x, V)
    V_canvas = FigureCanvasTkAgg(V_figure, mainframe)
    V_canvas.get_tk_widget().grid(row=2, column=2)

    # This Plots the first 6 EigenVectors
    if(pot_var.get() == "Particle with a Barrier"):
        make_display(0, 1, 3, E_vec)
        make_display(2, 2, 3, E_vec)
        make_display(4, 3, 3, E_vec)
        make_display(6, 1, 4, E_vec)
        make_display(8, 2, 4, E_vec)
        make_display(10, 3, 4, E_vec)
    else:
        make_display(0, 1, 3, E_vec)
        make_display(1, 2, 3, E_vec)
        make_display(2, 3, 3, E_vec)
        make_display(3, 1, 4, E_vec)
        make_display(4, 2, 4, E_vec)
        make_display(5, 3, 4, E_vec)


root = Tk()
root.title("Basic Probability Densities for a particle in a box")


# This is the main window tacked onto root
mainframe = ttk.Frame(root, padding=" 3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Making the Title
Title = Label(mainframe, anchor=W, justify=CENTER,
              text="Doc Crawford's House of Wave Functions")
Title.config(font=("Courier", 20))
Title.grid(column=2, row=0, sticky=EW, columnspan=2)

# This is the list of available potentials and the dictionaries necessary to display them
pot_select = ["Particle in a Box", "Particle in a Box", "Particle with a Barrier", "Particle with a Large Barrier",
              "Particle in a Harmonic Potential", "Particle in a Morse Potential", "Particle with a step potential"]
pot_dict = {"Particle with a Large Barrier": "HiBar", "Particle in a Box": "Open", "Particle with a step potential": "Box",
            "Particle with a Barrier": "Bar", "Particle in a Harmonic Potential": "HO", "Particle in a Morse Potential": 'Morse'}
pot_text = {"Particle with a Large Barrier": HiBar, "Particle in a Box": Open, "Particle with a step potential": Box,
            "Particle with a Barrier": Bar, "Particle in a Harmonic Potential": HO, "Particle in a Morse Potential": Morse}


# This is the call to the Wavefunction . . . function
E_val, E_vec, V, x = WaveCalc("Open")

# This plots the Potential initial potential for a particle in a box
V_figure = Figure(figsize=(4, 4), dpi=70)
V_plot = V_figure.add_subplot(
    1, 1, 1, xlabel='Position', title="Plot of Potential Energy")
V_plot.plot(x, V)
V_canvas = FigureCanvasTkAgg(V_figure, mainframe)
V_canvas.get_tk_widget().grid(row=2, column=2)


# This Plots the first six EigenVectors
E_vec_canvas_1 = make_display(0, 1, 3, E_vec)
E_vec_canvas_2 = make_display(1, 2, 3, E_vec)
E_vec_canvas_3 = make_display(2, 3, 3, E_vec)
E_vec_canvas_4 = make_display(3, 1, 4, E_vec)
E_vec_canvas_5 = make_display(4, 2, 4, E_vec)
E_vec_canvas_6 = make_display(5, 3, 4, E_vec)


# This is the potential selector, added to the grid at the bottom to allow for extra padding
pot_var = StringVar(root)
pot_selector = ttk.OptionMenu(mainframe, pot_var, *pot_select, )
pot_var.trace("w", update_displays)

# #This is the download button, added to the grid at the bottom to allow for extra padding
download_button = Button(mainframe, text="Export Data",
                         command=download_callback(E_val, E_vec))

# This is the Upper text
upper_text = Label(mainframe, anchor=W, justify=LEFT,
                   wraplength=500, text=header_text)
upper_text.grid(column=1, row=1, sticky=W, columnspan=2)


# this is the Lower text
lower_text = Label(mainframe, anchor=W, justify=LEFT, wraplength=500)
lower_text.grid(column=1, row=3, sticky=W, columnspan=2)
lower_text.configure(text="The selected item is {}".format(Open))

# this is the download text
download_text = Label(mainframe, anchor=W, justify=LEFT, wraplength=200)

# padding all the widgets added so far
for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

# padding the buttons after padding everything else to make it look nice.
pot_selector.grid(column=1, row=2, sticky=N)
download_button.grid(column=1, row=2, sticky=N, pady=50)
download_text.grid(column=1, row=2, sticky=S, columnspan=1)
download_text.configure(text=export_text)

# Making the GUI
root.mainloop()
