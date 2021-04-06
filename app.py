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
        Label(self.panel, text='(', font=('Segoe UI', '48')).place(x=100, y=49)
        Label(self.panel, text=')', font=('Segoe UI', '48')).place(x=500, y=49)

        #Salida ecuaciones
            #RESULTADO
        self.lb_canvas = Label(self.frame)
        self.lb_canvas.place(width=620, height=270, x=0, y=230)

        self.fig = matplotlib.figure.Figure(dpi=75)
        self.ax = self.fig.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.lb_canvas)
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        self.canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)

        self.ax.get_xaxis().set_visible(False)
        self.ax.get_yaxis().set_visible(False)

        #CAMPOS DE ENTRADA
        self.sup = Entry(self.panel)
        self.sup.place(x=70, y=68, width=30, height=14)

        self.sub = Entry(self.panel)
        self.sub.place(x=70, y=140, width=30, height=14)

        self.text = Entry(self.panel, font=('Segoe UI', '10'))
        self.text.place(x=140, y=80, height=40, width=350)

        self.btn_calcular = Button(
            self.panel, 
            command = self.tipo_integral, 
            text = 'Calcular',
            fg = '#1d3557',
            font = ('Arial Black', '11')
            ).place(x=270, y=180)

        self.root.bind('<KeyRelease>', self.p)

        self.root.mainloop()
    
    def calcular_normal(self):
        f = self.reformat_in(self.text.get())
        r = integrate(f, x)
        self.graph(latex(r))

    def calcular_num(self):
        f = self.reformat_in(self.text.get())
        r = integrate(f)
        self.graph(latex(r))
    
    def calcular_definida(self):
        f = self.reformat_in(self.text.get())
        r = integrate(f, (x, self.sup.get(), self.sub.get()))
        self.graph(latex(r))

    def reformat_in(self, text):
        s = str(text)
        return s.replace('sen', 'sin')

    def p(self, t):
        print('Hello' , t)

    def graph(self, text, tipo = 0):
        if tipo == 0:
            tmptext = "$"+text+"$"
        else:
            temptext = text

        self.ax.clear()
        self.ax.text(0.1, 0.4, tmptext, fontsize = 30)  
        self.canvas.draw()
    
    def tipo_integral(self):
        try:
            if self.sub.get() != '' and self.sup.get() != '':
                self.calcular_definida()
                return
            if str(self.text.get()).isnumeric():
                self.calcular_normal()
                return
            else:
                self.calcular_normal()
        except:
            self.graph('Nose puede integrar', 1)

if __name__ == '__main__':
    v = Calculadora()
    print('exiting...')