import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk
from WaveFunction import WaveCalc
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from explanations import *

# Functions
def make_display(q_num,row_num,col_num,Vec):
    E_vec_figure = Figure(figsize=(4,4), dpi=70)
    E_vec_plot = E_vec_figure.add_subplot(1, 1, 1, xlabel = 'Position', title = "{} Energy Level's Wave Function".format(q_num))
    E_vec_plot.plot(x,Vec[:,q_num]**2)
    E_vec_canvas = FigureCanvasTkAgg(E_vec_figure, mainframe)
    E_vec_canvas.get_tk_widget().grid(row=row_num, column=col_num)

def update_display(*args):
    lower_text.configure(text="{}".format(pot_text[pot_var.get()]))
    E_val, E_vec, V, x = WaveCalc(pot_dict[pot_var.get()])
    # This plots the Potential initial potential for a particle in a box
    V_figure = Figure(figsize=(4,4), dpi=70)
    V_plot = V_figure.add_subplot(1, 1, 1, xlabel = 'Position', title = "Plot of Potential Energy")
    V_plot.plot(x,V)
    V_canvas = FigureCanvasTkAgg(V_figure, mainframe)
    V_canvas.get_tk_widget().grid(row=2, column=2)


    #This Plots the first three EigenVectors
    make_display(0,1,3,E_vec)
    # E_vec_0_figure = Figure(figsize=(4,4), dpi=70)
    # E_vec_0 = E_vec_0_figure.add_subplot(1, 1, 1, xlabel = 'Position', title = "1st Energy Level's Wave Function")
    # E_vec_0.plot(x,E_vec[:,0]**2)
    # E_vec_0_canvas = FigureCanvasTkAgg(E_vec_0_figure, mainframe)
    # E_vec_0_canvas.get_tk_widget().grid(row=1, column=3)

    E_vec_1_figure = Figure(figsize=(4,4), dpi=70)
    E_vec_1 = E_vec_1_figure.add_subplot(1, 1, 1, xlabel = 'Position', title = "2nd Energy Level's Wave Function")
    E_vec_1.plot(x,E_vec[:,1]**2)
    E_vec_1_canvas = FigureCanvasTkAgg(E_vec_1_figure, mainframe)
    E_vec_1_canvas.get_tk_widget().grid(row=2, column=3)

    E_vec_2_figure = Figure(figsize=(4,4), dpi=70)
    E_vec_2 = E_vec_2_figure.add_subplot(1, 1, 1, xlabel = 'Position', title = "3rd Energy Level's Wave Function")
    E_vec_2.plot(x,E_vec[:,2]**2)
    E_vec_2_canvas = FigureCanvasTkAgg(E_vec_2_figure, mainframe)
    E_vec_2_canvas.get_tk_widget().grid(row=3, column=3)

        #This Plots the 2nd  three EigenVectors
    E_vec_3_figure = Figure(figsize=(4,4), dpi=70)
    E_vec_3 = E_vec_3_figure.add_subplot(1, 1, 1, xlabel = 'Position', title = "1st Energy Level's Wave Function")
    E_vec_3.plot(x,E_vec[:,3]**2)
    E_vec_3_canvas = FigureCanvasTkAgg(E_vec_3_figure, mainframe)
    E_vec_3_canvas.get_tk_widget().grid(row=1, column=4)

    E_vec_4_figure = Figure(figsize=(4,4), dpi=70)
    E_vec_4 = E_vec_4_figure.add_subplot(1, 1, 1, xlabel = 'Position', title = "2nd Energy Level's Wave Function")
    E_vec_4.plot(x,E_vec[:,4]**2)
    E_vec_4_canvas = FigureCanvasTkAgg(E_vec_4_figure, mainframe)
    E_vec_4_canvas.get_tk_widget().grid(row=2, column=4)

    E_vec_5_figure = Figure(figsize=(4,4), dpi=70)
    E_vec_5 = E_vec_5_figure.add_subplot(1, 1, 1, xlabel = 'Position', title = "3rd Energy Level's Wave Function")
    E_vec_5.plot(x,E_vec[:,5]**2)
    E_vec_5_canvas = FigureCanvasTkAgg(E_vec_5_figure, mainframe)
    E_vec_5_canvas.get_tk_widget().grid(row=3, column=4)


root = Tk()
root.title("Basic Probability Densities for a particle in a box")

#This is the main window tacked onto root
mainframe = ttk.Frame(root, padding=" 3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)



#This is the list of available potentials and the dictionaries necessary to display them
pot_select = ["Particle in a Box","Particle with a step potential", "Particle with a Barrier", "Particle in a Harmonic Potential", "Particle in a Morse Potential"]
pot_dict = {"Particle in a Box":"Open","Particle with a step potential":"Box", "Particle with a Barrier":"Bar", "Particle in a Harmonic Potential":"HO", "Particle in a Morse Potential":'Morse'}
pot_text = {"Particle in a Box":Open,"Particle with a step potential":Box, "Particle with a Barrier":Bar, "Particle in a Harmonic Potential":HO, "Particle in a Morse Potential":Morse}

#This is the potential selector, added to the grid at the bottom to allow for extra padding
pot_var = StringVar(root)
pot_selector = ttk.OptionMenu(mainframe, pot_var, *pot_select, )
pot_var.trace("w",update_display)

# #This is the submit button, added to the grid at the bottom to allow for extra padding
# submit_button = Button(mainframe,text="Calculate Wavefunctions")

#This is the call to the Wavefunction . . . function
E_val, E_vec, V, x = WaveCalc("Open")

# This plots the Potential initial potential for a particle in a box
V_figure = Figure(figsize=(4,4), dpi=70)
V_plot = V_figure.add_subplot(1, 1, 1, xlabel = 'Position', title = "Plot of Potential Energy")
V_plot.plot(x,V)
V_canvas = FigureCanvasTkAgg(V_figure, mainframe)
V_canvas.get_tk_widget().grid(row=2, column=2)


#This Plots the first three EigenVectors
E_vec_0_figure = Figure(figsize=(4,4), dpi=70)
E_vec_0 = E_vec_0_figure.add_subplot(1, 1, 1, xlabel = 'Position', title = "1st Energy Level's Wave Function")
E_vec_0.plot(x,E_vec[:,0]**2)
E_vec_0_canvas = FigureCanvasTkAgg(E_vec_0_figure, mainframe)
E_vec_0_canvas.get_tk_widget().grid(row=1, column=3)

E_vec_1_figure = Figure(figsize=(4,4), dpi=70)
E_vec_1 = E_vec_1_figure.add_subplot(1, 1, 1, xlabel = 'Position', title = "2nd Energy Level's Wave Function")
E_vec_1.plot(x,E_vec[:,1]**2)
E_vec_1_canvas = FigureCanvasTkAgg(E_vec_1_figure, mainframe)
E_vec_1_canvas.get_tk_widget().grid(row=2, column=3)

E_vec_2_figure = Figure(figsize=(4,4), dpi=70)
E_vec_2 = E_vec_2_figure.add_subplot(1, 1, 1, xlabel = 'Position', title = "3rd Energy Level's Wave Function")
E_vec_2.plot(x,E_vec[:,2]**2)
E_vec_2_canvas = FigureCanvasTkAgg(E_vec_2_figure, mainframe)
E_vec_2_canvas.get_tk_widget().grid(row=3, column=3)



#This is the Upper text
upper_text = Label(mainframe,anchor=W, justify=LEFT, wraplength=500, text = header_text)
upper_text.grid(column=1, row=1, sticky=W,columnspan = 2)


#this is the Lower text
lower_text = Label(mainframe,anchor=W, justify=LEFT, wraplength=500)
lower_text.grid(column=1, row=3, sticky=W,columnspan = 2)
lower_text.configure(text="The selected item is {}".format(Open))

# padding all the widgets added so far
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

# padding the buttons after padding everything else to make it look nice.
# submit_button.grid(column=1,row=2, sticky=S,pady=100)
pot_selector.grid(column=1,row=2, sticky=N,pady=100)

# Making the GUI
root.mainloop()

