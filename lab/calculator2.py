import tkinter
import math
import random

def add_f(f):                       # это для общего ввода
    x = enter.get()+str(f)
    if str(f) in '+/*':
        x = x[:-1]
        enter.delete(0, tkinter.END)
        enter.insert(0, x+f)
    else:
        enter.delete(0, tkinter.END)
        enter.insert(0, x)

def add_operation(f):               #это для операций
    x = enter.get()
    if x[-1] in '-/+*':
        x = x[:-1]
    enter.delete(0, tkinter.END)
    enter.insert(0, x+f)

def ecually():
    x = enter.get()
    if x[-1] in '+-*/': #если выражение имеет виж * 9-(пустое значение) *
        y = x[-1]
        x = x[:-1]
    elif '/0' in x: #проверка деления на 0
        enter.delete(0, tkinter.END)
        enter.insert(0, 'ERROR')
    elif x not in '0123456789+-%*()/!sincostan':
        enter.delete(0, tkinter.END)
        enter.insert(0, 'ERROR')
    elif '!' in x:
        x = x[:-1]
        y = math.factorial(int(x))
        enter.delete(0, tkinter.END)
        enter.insert(0, y)
    elif "sin(" in x or "cos(" in x or 'tan(' in x:
        add_sct()
    y = eval(x)
    enter.delete(0, tkinter.END)
    enter.insert(0, y)

def add_sct(f):
    x = enter.get() + str(f)
    if 'sin' in x:
        y = x.replace("sin(", "math.sin(math.radians(")
        enter.delete(0, tkinter.END)
        enter.insert(0, y)
    if 'cos' in x:
        y = x.replace("cos(", "math.cos(math.radians(")
        enter.delete(0, tkinter.END)
        enter.insert(0, y)
    if 'tan' in x:
        y = x.replace("tan(", "math.tan(math.radians(")
        enter.delete(0, tkinter.END)
        enter.insert(0, y)
    if 'lg' in x:
        y = x.replace('lg(','math.log(')
        enter.delete(0, tkinter.END)
        enter.insert(0, y)


def Clear():                            #очищает всю строку
    enter.delete(0,tkinter.END)
def ClearE():                           #очищает последний элемент
    x = enter.get()
    y = x[:-1]
    enter.delete(0, tkinter.END)
    enter.insert(0,y)

def buttonsNUM(f):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = f'#{r:02x}{g:02x}{b:02x}'
    return tkinter.Button(text=f,bd=5, font=('Arial', 18),relief='sunken',bg='#C0C0C0',activebackground=color,command=lambda: add_f(f))
def buttonsOP(z):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = f'#{r:02x}{g:02x}{b:02x}'
    return tkinter.Button(text=z,bd=5, font=('Arial', 18),relief='sunken',bg='#C0C0C0',activebackground=color,command=lambda: add_operation(z))
def buttonsSCT(f):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = f'#{r:02x}{g:02x}{b:02x}'
    return tkinter.Button(text=f,bd=5, font=('Arial', 18),relief='sunken',bg='#C0C0C0',activebackground=color,command=lambda: add_sct(f+'('))
def buttonsDOP(f):
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = f'#{r:02x}{g:02x}{b:02x}'
    return tkinter.Button(text=f,bd=5, font=('Arial', 18),relief='sunken',bg='#C0C0C0',activebackground=color,command=lambda: add_f(f))

root = tkinter.Tk()
root.geometry('580x500')
root.title('Инженерный калькулятор')
root.config(bg='#000000')
root.minsize(480,400)
#root.resizable(width=True, height=True)


for i in range(7):
    for j in range(5):
        root.columnconfigure(i, weight=1)
        root.columnconfigure(j, weight=1)
        root.rowconfigure(i, weight=1)
        root.rowconfigure(j, weight=1)

enter = tkinter.Entry(root,justify=tkinter.RIGHT,font=('Arial',25),width=20, bg='#808080')
enter.grid(row=0,column=0,columnspan=7,rowspan=2,stick='wens',padx=5)

r = random.randint(0, 255)
g = random.randint(0, 255)
b = random.randint(0, 255)
color2 = f'#{r:02x}{g:02x}{b:02x}'



buttonsNUM('0').grid(row=6, column=4,stick='wens',padx=8,pady=8)
buttonsNUM('1').grid(row=5, column=3,stick='wens',padx=8,pady=8)
buttonsNUM('2').grid(row=5, column=4,stick='wens',padx=8,pady=8)
buttonsNUM('3').grid(row=5, column=5,stick='wens',padx=8,pady=8)
buttonsNUM('4').grid(row=4, column=3,stick='wens',padx=8,pady=8)
buttonsNUM('5').grid(row=4, column=4,stick='wens',padx=8,pady=8)
buttonsNUM('6').grid(row=4, column=5,stick='wens',padx=8,pady=8)
buttonsNUM('7').grid(row=3, column=3,stick='wens',padx=8,pady=8)
buttonsNUM('8').grid(row=3, column=4,stick='wens',padx=8,pady=8)
buttonsNUM('9').grid(row=3, column=5,stick='wens',padx=8,pady=8)

buttonsOP('+').grid(row=4, column=6,stick='wens',padx=8,pady=8)
buttonsOP('-').grid(row=3, column=6,stick='wens',padx=8,pady=8)
buttonsOP('*').grid(row=2, column=5,stick='wens',padx=8,pady=8)
buttonsOP('/').grid(row=2, column=4,stick='wens',padx=8,pady=8)

buttonsDOP('(').grid(row=2, column=0,stick='wens',padx=8,pady=8)
buttonsDOP(')').grid(row=2, column=1,stick='wens',padx=8,pady=8)
buttonsDOP('.').grid(row=6, column=5,stick='wens',padx=8,pady=8)

tkinter.Button(text='%',bd=5, font=('Arial', 12),relief='sunken',bg='#C0C0C0',activebackground=color2,command=lambda: add_f('%')).grid(row=6, column=3,stick='wens',padx=8,pady=8)
tkinter.Button(text='√',bd=5, font=('Arial', 15),relief='sunken',bg='#C0C0C0',activebackground=color2,command=lambda: add_f('**(1/2)')).grid(row=4, column=1,stick='wens',padx=8,pady=8)
tkinter.Button(text='y√x',bd=5, font=('Arial', 15),relief='sunken',bg='#C0C0C0',activebackground=color2,command=lambda: add_f('**(1/')).grid(row=4, column=2,stick='wens',padx=8,pady=8)
tkinter.Button(text='x²',bd=5, font=('Arial', 15),relief='sunken',bg='#C0C0C0',activebackground=color2,command=lambda: add_f('**2')).grid(row=3, column=0,stick='wens',padx=8,pady=8)
tkinter.Button(text='x³',bd=5, font=('Arial', 15),relief='sunken',bg='#C0C0C0',activebackground=color2,command=lambda: add_f('**3')).grid(row=3, column=1,stick='wens',padx=8,pady=8)
tkinter.Button(text='x^y',bd=5, font=('Arial', 12),relief='sunken',bg='#C0C0C0',activebackground=color2,command=lambda: add_f('**')).grid(row=3, column=2,stick='wens',padx=8,pady=8)
tkinter.Button(text='π',bd=5, font=('Arial', 15),relief='sunken',bg='#C0C0C0',activebackground=color2,command=lambda: add_f('3.14')).grid(row=5, column=1,stick='wens',padx=8,pady=8)
tkinter.Button(text='e',bd=5, font=('Arial', 15),relief='sunken',bg='#C0C0C0',activebackground=color2,command=lambda: add_f('2.711828')).grid(row=5, column=0,stick='wens',padx=8,pady=8)
tkinter.Button(text='!',bd=5, font=('Arial', 15),relief='sunken',bg='#C0C0C0',activebackground=color2,command=lambda: add_f('math.factorial(')).grid(row=4, column=0,stick='wens',padx=8,pady=8)

buttonsSCT('lg').grid(row=5, column=2,stick='wens',padx=8,pady=8)
buttonsSCT('sin').grid(row=6, column=0,stick='wens',padx=8,pady=8)
buttonsSCT('cos').grid(row=6, column=1,stick='wens',padx=8,pady=8)
buttonsSCT('tan').grid(row=6, column=2,stick='wens',padx=8,pady=8)

tkinter.Button(text='1/x',bd=5, font=('Arial', 15),relief='sunken',bg='#C0C0C0',activebackground=color2,command=lambda: add_f('**(-1)')).grid(row=2, column=2,stick='wens',padx=8,pady=8)

tkinter.Button(text='=',bd=5, font=('Arial', 15),relief='sunken',bg='#C0C0C0',activebackground=color2,command=lambda: ecually()).grid(row=5,column=6,rowspan=2,stick='wens',padx=8,pady=8)
tkinter.Button(text='CE',bd=5, font=('Arial', 10),relief='sunken',bg='#C0C0C0',activebackground=color2,command=lambda: ClearE()).grid(row=2, column=6,stick='wens',padx=8,pady=8)
tkinter.Button(text='C',bd=5, font=('Arial', 10),relief='sunken',bg='#C0C0C0',activebackground=color2,command=lambda: Clear()).grid(row=2, column=3,stick='wens',padx=8,pady=8)


root.grid_columnconfigure(0,minsize=40)
root.grid_columnconfigure(1,minsize=40)
root.grid_columnconfigure(2,minsize=40)
root.grid_columnconfigure(3,minsize=40)
root.grid_columnconfigure(4,minsize=40)
root.grid_columnconfigure(5,minsize=40)
root.grid_columnconfigure(6,minsize=40)


root.grid_rowconfigure(1,minsize=50)
root.grid_rowconfigure(2,minsize=50)
root.grid_rowconfigure(3,minsize=50)
root.grid_rowconfigure(4,minsize=50)
root.grid_rowconfigure(5,minsize=50)
root.grid_rowconfigure(6,minsize=50)


root.mainloop()