import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk
from WaveFunction import WaveCalc
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#This is the list of available potentials
pot_select = ["Particle in a Box","Particle with a step potential", "Particle with a Barrier", "Particle in a Harmonic Potential", "Particle in a Morse Potential"]

root = Tk()
root.title("Physics GUI WireFrame")

#This is the main window tacked onto root
mainframe = ttk.Frame(root, padding=" 3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)	

#This is the potential selector
pot_var = StringVar(root)
pot_var.set(pot_select[0])
pot_selector = ttk.OptionMenu(mainframe, pot_var, *pot_select)
pot_selector.grid(column=1,row=2, sticky=NS)

#This is the call to the Wavefunction . . . function
E_val, E_vec, V, x = WaveCalc('Morse')

# This plots the Potential
V_figure = Figure(figsize=(2, 2), dpi=100)
V_plot = V_figure.add_subplot(1, 1, 1)
V_plot.plot(x,V)
V_canvas = FigureCanvasTkAgg(V_figure, mainframe)
V_canvas.get_tk_widget().grid(row=2, column=2)


#This Plots the first three EigenVectors
E_vec_0_figure = Figure(figsize=(2, 2), dpi=100)
E_vec_0 = E_vec_0_figure.add_subplot(1, 1, 1)
E_vec_0.plot(x,E_vec[:,0]**2,marker='x')
E_vec_0_canvas = FigureCanvasTkAgg(E_vec_0_figure, mainframe)
E_vec_0_canvas.get_tk_widget().grid(row=1, column=3)

E_vec_1_figure = Figure(figsize=(2, 2), dpi=100)
E_vec_1 = E_vec_1_figure.add_subplot(1, 1, 1)
E_vec_1.plot(x,E_vec[:,1]**2,marker='x')
E_vec_1_canvas = FigureCanvasTkAgg(E_vec_1_figure, mainframe)
E_vec_1_canvas.get_tk_widget().grid(row=2, column=3)

E_vec_2_figure = Figure(figsize=(2, 2), dpi=100)
E_vec_2 = E_vec_2_figure.add_subplot(1, 1, 1)
E_vec_2.plot(x,E_vec[:,2]**2,marker='x')
E_vec_2_canvas = FigureCanvasTkAgg(E_vec_2_figure, mainframe)
E_vec_2_canvas.get_tk_widget().grid(row=3, column=3)







for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
root.mainloop()


''' Below successfully displays the calculated plot
V, x = WaveCalc('Morse')
print(x)
plt.axis([0,200,0,.051])
plt.plot(x,V)
plt.show()
'''