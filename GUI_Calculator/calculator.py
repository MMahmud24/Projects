import tkinter as tk

class Calculator:
    def __init__(self, main):
        main.title("Calculator")
        main.geometry('285x360')
        main.config(bg='#373737')
        main.resizable(False,False)

        self.equation = tk.StringVar()
        self.entry_val = ''
        tk.Entry(width=17, bg='black', fg='white',font=('Arial',28) , textvariable=self.equation).place(x=0,y=0)
        
        buttonframe = tk.Frame(main)
        buttonframe.columnconfigure(0, weight=1)
        buttonframe.columnconfigure(1, weight=1)
        buttonframe.columnconfigure(2, weight=1)
        buttonframe.columnconfigure(3, weight=1)

        tk.Button(width=3,height=2, text='1', relief='flat',font=('Arial', 18), command = lambda:self.show(1)).place(x=0,y=50)
        tk.Button(width=3,height=2, text='2', relief='flat',font=('Arial', 18), command = lambda:self.show(2)).place(x=72,y=50)
        tk.Button(width=3,height=2, text='3', relief='flat',font=('Arial', 18), command = lambda:self.show(3)).place(x=144,y=50)
        tk.Button(width=3,height=2, text='+', relief='flat',font=('Arial', 18), command = lambda:self.show("+")).place(x=216,y=50)
        tk.Button(width=3,height=2, text='4', relief='flat',font=('Arial', 18), command = lambda:self.show(4)).place(x=0,y=110)
        tk.Button(width=3,height=2, text='5', relief='flat',font=('Arial', 18), command = lambda:self.show(5)).place(x=72,y=110)
        tk.Button(width=3,height=2, text='6', relief='flat',font=('Arial', 18), command = lambda:self.show(6)).place(x=144,y=110)
        tk.Button(width=3,height=2, text='-', relief='flat',font=('Arial', 18), command = lambda:self.show("-")).place(x=216,y=110)
        tk.Button(width=3,height=2, text='7', relief='flat',font=('Arial', 18), command = lambda:self.show(7)).place(x=0,y=170)
        tk.Button(width=3,height=2, text='8', relief='flat',font=('Arial', 18), command = lambda:self.show(8)).place(x=72,y=170)
        tk.Button(width=3,height=2, text='9', relief='flat',font=('Arial', 18), command = lambda:self.show(9)).place(x=144,y=170)
        tk.Button(width=3,height=2, text='*', relief='flat',font=('Arial', 18), command = lambda:self.show("*")).place(x=216,y=170)
        tk.Button(width=3,height=2, text='C', relief='flat',font=('Arial', 18), command = self.clear).place(x=0,y=230)
        tk.Button(width=3,height=2, text='0', relief='flat',font=('Arial', 18), command = lambda:self.show(0)).place(x=72,y=230)
        tk.Button(width=3,height=2, text='.', relief='flat',font=('Arial', 18), command = lambda:self.show(".")).place(x=144,y=230)
        tk.Button(width=3,height=2, text='/', relief='flat',font=('Arial', 18), command = lambda:self.show("/")).place(x=216,y=230)
        tk.Button(width=3,height=2, text='(', relief='flat',font=('Arial', 18), command = lambda:self.show("(")).place(x=0,y=290)
        tk.Button(width=3,height=2, text=')', relief='flat',font=('Arial', 18), command = lambda:self.show(")")).place(x=72,y=290)
        tk.Button(width=3,height=2, text='^', relief='flat',font=('Arial', 18), command = lambda:self.show("**")).place(x=144,y=290)
        tk.Button(width=3,height=2, text='=', relief='flat',font=('Arial', 18), command = self.solve).place(x=216,y=290)
        


    def show(self,value):
        self.entry_val+=str(value)
        self.equation.set(self.entry_val)

    def clear(self):
        self.entry_val = ''
        self.equation.set(self.entry_val)

    def solve(self):
        result = eval(self.entry_val)
        self.equation.set(result)

root=tk.Tk()
Calculator = Calculator(root)
root.mainloop()
