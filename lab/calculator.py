#import tkinter
#
#def add_digit(f):
#    enter.insert(0,f)
#
#
#root = tkinter.Tk()
#root.geometry('290x290')
#root.title('Инженерный калькулятор')
#root.config(bg='#08e8de')
#root.resizable(width=False, height=False)
#
#btn_plus = tkinter.Button(root, text='+',bd=5)
#btn_minus = tkinter.Button(root, text='-',bd=5)
#btn_multiplication = tkinter.Button(root, text='×',bd=5)
#btn_division = tkinter.Button(root, text='÷',bd=5)
#btn_equally = tkinter.Button(root, text='=',bd=5)
#btn_point = tkinter.Button(root, text='.',bd=5)
#btn_procent = tkinter.Button(root, text='%',bd=5)
#bnt_root = tkinter.Button(root, text='√',bd=5)
#bnt_root2 = tkinter.Button(root, text='y√x',bd=5)
#bnt_square = tkinter.Button(root, text='x²',bd=5)
#bnt_cube = tkinter.Button(root, text='x³',bd=5)
#bnt_degree = tkinter.Button(root, text='x^y',bd=5)
#bnt_pi = tkinter.Button(root, text='π',bd=5)
#bnt_e = tkinter.Button(root, text='e',bd=5)
#bnt_sin = tkinter.Button(root, text='sin',bd=5)
#bnt_cos = tkinter.Button(root, text='cos',bd=5)
#bnt_tan = tkinter.Button(root, text='tan',bd=5)
#bnt_lg = tkinter.Button(root, text='lg',bd=5)
#bnt_factorial = tkinter.Button(root, text='!',bd=5)
#bnt_drob = tkinter.Button(root, text='1/x',bd=5)
###############################################
#tkinter.Button(root, text='0',bd=5,command=lambda: add_digit(0)).grid(row=6,column=4,stick='wens',padx=3,pady=3)
#tkinter.Button(root, text='1',bd=5,command=lambda: add_digit(1)).grid(row=5,column=3,stick='wens',padx=3,pady=3)
#tkinter.Button(root, text='2',bd=5,command=lambda: add_digit(2)).grid(row=5,column=4,stick='wens',padx=3,pady=3)
#tkinter.Button(root, text='3',bd=5,command=lambda: add_digit(3)).grid(row=5,column=5,stick='wens',padx=3,pady=3)
#tkinter.Button(root, text='4',bd=5,command=lambda: add_digit(4)).grid(row=4,column=3,stick='wens',padx=3,pady=3)
#tkinter.Button(root, text='5',bd=5,command=lambda: add_digit(5)).grid(row=4,column=4,stick='wens',padx=3,pady=3)
#tkinter.Button(root, text='6',bd=5,command=lambda: add_digit(6)).grid(row=4,column=5,stick='wens',padx=3,pady=3)
#tkinter.Button(root, text='7',bd=5,command=lambda: add_digit(7)).grid(row=3,column=3,stick='wens',padx=3,pady=3)
#tkinter.Button(root, text='8',bd=5,command=lambda: add_digit(8)).grid(row=3,column=4,stick='wens',padx=3,pady=3)
#tkinter.Button(root, text='9',bd=5,command=lambda: add_digit(9)).grid(row=3,column=5,stick='wens',padx=3,pady=3)
###############################################
#btn_scobaL = tkinter.Button(root, text='(',bd=5)
#btn_scobaR = tkinter.Button(root, text=')',bd=5)
###############################################
#bnt_C = tkinter.Button(root, text='C',bd=5)
#bnt_clear = tkinter.Button(root, text='CE',bd=5)
#
#enter = tkinter.Entry(root)
#
#
#btn_plus.grid(row=4,column=6,stick='wens',padx=3,pady=3)
#btn_minus.grid(row=3,column=6,stick='wens',padx=3,pady=3)
#btn_multiplication.grid(row=2,column=5,stick='wens',padx=3,pady=3)
#btn_division.grid(row=2,column=4,stick='wens',padx=3,pady=3)
#btn_equally.grid(row=5,column=6,rowspan=2,stick='wens',padx=3,pady=3)
#btn_point.grid(row=6,column=5,stick='wens',padx=3,pady=3)
#btn_procent.grid(row=6,column=3,stick='wens',padx=3,pady=3)
#bnt_root.grid(row=4,column=1,stick='wens',padx=3,pady=3)
#bnt_root2.grid(row=4,column=2,stick='wens',padx=3,pady=3)
#bnt_square.grid(row=3,column=0,stick='wens',padx=3,pady=3)
#bnt_cube.grid(row=3,column=1,stick='wens',padx=3,pady=3)
#bnt_degree.grid(row=3,column=2,stick='wens',padx=3,pady=3)
#bnt_pi.grid(row=5,column=1,stick='wens',padx=3,pady=3)
#bnt_e.grid(row=5,column=0,stick='wens',padx=3,pady=3)
#bnt_sin.grid(row=6,column=0,stick='wens',padx=3,pady=3)
#bnt_cos.grid(row=6,column=1,stick='wens',padx=3,pady=3)
#bnt_tan.grid(row=6,column=2,stick='wens',padx=3,pady=3)
#bnt_lg.grid(row=5,column=2,stick='wens',padx=3,pady=3)
#bnt_factorial.grid(row=4,column=0,stick='wens',padx=3,pady=3)
#bnt_drob.grid(row=2,column=2,stick='wens',padx=3,pady=3)
##btn0.grid(row=6,column=4,stick='wens',padx=3,pady=3)
##btn1.grid(row=5,column=3,stick='wens',padx=3,pady=3)
##btn2.grid(row=5,column=4,stick='wens',padx=3,pady=3)
##btn3.grid(row=5,column=5,stick='wens',padx=3,pady=3)
##btn4.grid(row=4,column=3,stick='wens',padx=3,pady=3)
##btn5.grid(row=4,column=4,stick='wens',padx=3,pady=3)
##btn6.grid(row=4,column=5,stick='wens',padx=3,pady=3)
##btn7.grid(row=3,column=3,stick='wens',padx=3,pady=3)
##btn8.grid(row=3,column=4,stick='wens',padx=3,pady=3)
##btn9.grid(row=3,column=5,stick='wens',padx=3,pady=3)
#btn_scobaL.grid(row=2,column=0,stick='wens',padx=3,pady=3)
#btn_scobaR.grid(row=2,column=1,stick='wens',padx=3,pady=3)
#bnt_C.grid(row=2,column=3,stick='wens',padx=3,pady=3)
#bnt_clear.grid(row=2,column=6,stick='wens',padx=3,pady=3)
#enter.grid(row=0,column=0,columnspan=7,rowspan=2,stick='wens',padx=3,pady=3)
#
#root.grid_columnconfigure(0,minsize=40)
#root.grid_columnconfigure(1,minsize=40)
#root.grid_columnconfigure(2,minsize=40)
#root.grid_columnconfigure(3,minsize=40)
#root.grid_columnconfigure(4,minsize=40)
#root.grid_columnconfigure(5,minsize=40)
#root.grid_columnconfigure(6,minsize=40)
#root.grid_columnconfigure(7,minsize=40)
#
#root.grid_rowconfigure(1,minsize=50)
#root.grid_rowconfigure(2,minsize=50)
#root.grid_rowconfigure(3,minsize=50)
#root.grid_rowconfigure(4,minsize=50)
#root.grid_rowconfigure(5,minsize=50)
#
#
#root.mainloop()
#import tkinter as tk
#import math
#
#
#def calculate():
#    try:
#        expression = entry.get()
#        if not expression:
#            return
#
#        # Заменяем символы для корректного вычисления
#        expression = expression.replace("^", "**").replace("√", "math.sqrt")
#
#        # Обработка тригонометрических функций (в градусах)
#        if "sin(" in expression:
#            expression = expression.replace("sin(", "math.sin(math.radians(") + ")"
#        if "cos(" in expression:
#            expression = expression.replace("cos(", "math.cos(math.radians(") + ")"
#        if "tan(" in expression:
#            expression = expression.replace("tan(", "math.tan(math.radians(") + ")"
#
#        # Обработка логарифмов
#        if "log(" in expression:
#            expression = expression.replace("log(", "math.log10(")
#        if "ln(" in expression:
#            expression = expression.replace("ln(", "math.log(")
#
#        # Вычисление
#        result = eval(expression)
#        entry.delete(0, tk.END)
#        entry.insert(tk.END, str(result))
#
#    except Exception as e:
#        entry.delete(0, tk.END)
#        entry.insert(tk.END, "Ошибка!")
#
#
#def add_to_entry(char):
#    entry.insert(tk.END, char)
#
#
#def clear_entry():
#    entry.delete(0, tk.END)
#
#
#root = tk.Tk()
#root.title("Инженерный калькулятор")
#
#entry = tk.Entry(root, width=30, font=("Arial", 14), borderwidth=5)
#entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)
#
#buttons = [
#    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3), ("C", 1, 4),
#    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3), ("^", 2, 4),
#    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3), ("√", 3, 4),
#    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3), ("(", 4, 4),
#    ("sin", 5, 0), ("cos", 5, 1), ("tan", 5, 2), ("log", 5, 3), (")", 5, 4),
#    ("ln", 6, 0), ("π", 6, 1), ("e", 6, 2), ("fact", 6, 3), ("DEL", 6, 4)
#]
#
#for (text, row, col) in buttons:
#    if text == "=":
#        btn = tk.Button(root, text=text, padx=20, pady=10, command=calculate)
#    elif text == "C":
#        btn = tk.Button(root, text=text, padx=20, pady=10, command=clear_entry)
#    elif text == "DEL":
#        btn = tk.Button(root, text=text, padx=15, pady=10, command=lambda: entry.delete(len(entry.get()) - 1))
#    elif text == "π":
#        btn = tk.Button(root, text=text, padx=20, pady=10, command=lambda: add_to_entry(str(math.pi)))
#    elif text == "e":
#        btn = tk.Button(root, text=text, padx=20, pady=10, command=lambda: add_to_entry(str(math.e)))
#    elif text == "fact":
#        btn = tk.Button(root, text=text, padx=15, pady=10, command=lambda: add_to_entry("math.factorial("))
#    else:
#        btn = tk.Button(root, text=text, padx=20, pady=10, command=lambda t=text: add_to_entry(t))
#
#    btn.grid(row=row, column=col)
#
#root.mainloop()




import math
from os import replace

y = '11845164811111111111111111110'
z = y.replace('1','9')
# Вычисляем синус 30 градусов (переводим в радианы)
sin_result = eval("math.sin(math.radians(90))")
print(sin_result)  # 0.5
print(z)