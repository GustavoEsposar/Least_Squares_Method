import tkinter as tk
from tkinter.font import Font
import tkinter.messagebox as messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import matplotlib.pyplot as plt


class JanelaAdaptavel(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Regressão Linear")
        self.iconbitmap("./figuras/calc_icon.ico")
        self.label = tk.Label(self, text="")
        self.label.grid(row=0, column=1, sticky="nsew")
        self.fig = Figure(figsize=(5, 5), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.resizable(False, False)

    def preencher_label(self, saida, X ,Y):
        fonte_label = Font(size=12)  # Altera o tamanho da fonte
        self.label.config(text=saida, font=fonte_label)
        coef = np.polyfit(X, Y, 1)
        polinomio = np.poly1d(coef)
        self.ax.scatter(X, Y, color='blue')
        self.ax.plot(X, polinomio(X), color='red')
        canvas = FigureCanvasTkAgg(self.fig, master=self)
        canvas.draw()
        canvas.get_tk_widget().grid(row=0, column=0)
        self.update()

    def run(self, saida, x, y):
        self.preencher_label(saida, x, y)
        self.mainloop()
