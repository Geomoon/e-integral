from tkinter import *
from sympy import *
from sympy.abc import x

#Para el dibujado de ecuaciones
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class Calculadora:

    def __init__(self):
        matplotlib.use('TkAgg')
        init_printing(use_latex=True)
        self.font = ('Segoe UI', '12')

        self.root = Tk()
        self.root.resizable(0, 0)
        self.root.title(' Calculadora de Integrales ')
        self.root.iconbitmap('icon.ico')

        self.frame = Frame(self.root)
        self.frame.config(width = 620, height = 500, bg = '#457B9D')
        self.frame.pack(fill = 'both', expand = 1)

        self.panel = Frame(self.frame)
        self.panel.config(width = 620, height = 225, bg = '#EEEEEE')
        self.panel.place(x = 0, y = 0)

        Label(self.frame, bg='#457B9D', width=2, height=8).place(x=0, y=45)
        Label(self.frame, bg='#457B9D', width=2, height=8).place(x=600, y=45)

        Label(self.panel, text='∫', font=('Segoe UI', '52')).place(x=30, y=49)
        Label(self.panel, text='(', font=('Segoe UI', '48')).place(x=110, y=49)
        Label(self.panel, text=')', font=('Segoe UI', '48')).place(x=500, y=49)

        #Salida ecuaciones
        self.lb_canvas = Label(self.frame)
        self.lb_canvas.place(width=620, height=275, x=0, y=230)

        self.fig = matplotlib.figure.Figure(figsize=(4, 3), dpi=100)
        self.ax = self.fig.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.lb_canvas)
        self.canvas.get_tk_widget().pack()
        self.canvas._tkcanvas.pack()

        self.ax.get_xaxis().set_visible(False)
        self.ax.get_yaxis().set_visible(False)

        #CAMPOS DE ENTRADA
        self.sup = Entry(self.panel)
        self.sup.place(x=80, y=65, width=14, height=14)

        self.sub = Entry(self.panel)
        self.sub.place(x=80, y=140, width=14, height=14)

        self.text = Entry(self.panel, font=('Segoe UI', '10'))
        self.text.place(x=80, y=10, height=30, width=450)

        self.btn_calcular = Button(
            self.panel, 
            command = self.calcular, 
            text = 'Calcular',
            fg = '#1d3557',
            font = ('Arial Black', '11')
            ).place(x=270, y=180)

        self.root.bind('<KeyRelease>', self.p)

        self.root.mainloop()
    
    def calcular(self):
        f = self.reformat_in(self.text.get())
        r = integrate(f)
        self.graph(latex(r))

    def reformat_in(self, text):
        s = str(text)
        return s.replace('sen', 'sin')

    def p(self, t):
        print('Hello' , t)

    def graph(self, text):
        tmptext = "$"+text+"$"

        self.ax.clear()
        self.ax.text(0.1, 0.4, tmptext, fontsize = 30)  
        self.canvas.draw()

if __name__ == '__main__':
    v = Calculadora()
    print('exiting...')