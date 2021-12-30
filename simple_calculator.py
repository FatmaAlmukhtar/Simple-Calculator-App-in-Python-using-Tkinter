import tkinter as tk

def button_click(number):
    current = e.get()
    e.delete(0, 'end')
    e.insert(0, str(current) + str(number))
    return

def button_clear():
    e.delete(0, 'end')

def button_add():
    first_number = e.get()
    global f_num
    global math
    math ='addition'
    f_num = int(first_number)
    e.delete(0, 'end')

def button_equal():
    second_number = e.get()
    e.delete(0, 'end')
    if math == 'addition':
        e.insert(0, f_num + int(second_number))
    if math == 'subtraction':
        e.insert(0, f_num - int(second_number))
    if math == 'multiplication':
        e.insert(0, f_num * int(second_number))
    if math == 'division':
        e.insert(0, f_num / int(second_number))

def button_subtract():
    first_number = e.get()
    global f_num
    global math
    math ='subtraction'
    f_num = int(first_number)
    e.delete(0, 'end')

def button_multiply():
    first_number = e.get()
    global f_num
    global math
    math ='multiplication'
    f_num = int(first_number)
    e.delete(0, 'end')

def button_divide():
    first_number = e.get()
    global f_num
    global math
    math ='division'
    f_num = int(first_number)
    e.delete(0, 'end')

root = tk.Tk()
root.title('Simple Calculator')
root.resizable(0, 0)

# Creating an input box widget
e = tk.Entry(root, width=35, bg='white', fg='black', borderwidth=5)
e.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
# Default value in text box
#e.insert(0, '')

# Create Buttons
button_1 = tk.Button(root, text='1', padx=20, pady=10, command=lambda: button_click(1))
button_2 = tk.Button(root, text='2', padx=20, pady=10, command=lambda: button_click(2))
button_3 = tk.Button(root, text='3', padx=20, pady=10, command=lambda: button_click(3))
button_4 = tk.Button(root, text='4', padx=20, pady=10, command=lambda: button_click(4))
button_5 = tk.Button(root, text='5', padx=20, pady=10, command=lambda: button_click(5))
button_6 = tk.Button(root, text='6', padx=20, pady=10, command=lambda: button_click(6))
button_7 = tk.Button(root, text='7', padx=20, pady=10, command=lambda: button_click(7))
button_8 = tk.Button(root, text='8', padx=20, pady=10, command=lambda: button_click(8))
button_9 = tk.Button(root, text='9', padx=20, pady=10, command=lambda: button_click(9))
button_0 = tk.Button(root, text='0', padx=105, pady=10, command=lambda: button_click(0))

button_add = tk.Button(root, text='+', padx=20, pady=10, command=button_add)
button_equal = tk.Button(root, text='=', padx=63, pady=10, command=button_equal)
button_clear = tk.Button(root, text='C', padx=63, pady=10, command=button_clear)

button_subtract = tk.Button(root, text='-', padx=20, pady=10, command=button_subtract)
button_multiply = tk.Button(root, text='x', padx=20, pady=10, command=button_multiply)
button_divide = tk.Button(root, text='/', padx=20, pady=10, command=button_divide)


# Put Buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0, columnspan=3)

button_add.grid(row=4, column=3)
button_subtract.grid(row=3, column=3)
button_multiply.grid(row=2, column=3)
button_divide.grid(row=1, column=3)
button_equal.grid(row=5, column=2, columnspan=2)
button_clear.grid(row=5, column=0, columnspan=2)


root.mainloop()
