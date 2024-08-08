import tkinter as tk
from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("Light")  
customtkinter.set_default_color_theme("dark-blue")  

def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + str(number))

def calculate():  
    try:
        result = eval(display.get())
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except ZeroDivisionError:
        display.delete(0, tk.END)
        display.insert(0, "Error: Division by zero")
    except SyntaxError:
        display.delete(0, tk.END)
        display.insert(0, "Error: Invalid expression")
    except Exception as e:
        display.delete(0, tk.END)
        display.insert(0, f"Error: {str(e)}")

def clear():
    display.delete(0, tk.END)

def backspace():
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current[:-1])

root = tk.Tk()
root.title("Calculator")
root.geometry('280x400')
root.resizable(0,0)
#root.configure(background="#1A1D23")
root.configure(background="#FFFFFF")

# Create a label to display the result
display = tk.Entry(root, width=38, borderwidth=5)
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create a function to create a rounded button
def create_rounded_button(text, command):
    button = customtkinter.CTkButton(root, text=text, command=command, corner_radius=10)
    button.configure(width=69.45, height=69.45)
    return button

# Create buttons using the function
btn7 = create_rounded_button("7", lambda: button_click(7))
btn7.grid(row=1, column=0)
btn7.configure(font=('verdana', 14))

btn8 = create_rounded_button("8", lambda: button_click(8))
btn8.grid(row=1, column=1)
btn8.configure(font=('verdana', 14))

btn9 = create_rounded_button("9", lambda: button_click(9))
btn9.grid(row=1, column=2)
btn9.configure(font=('verdana', 14))

btn_add = create_rounded_button("+", lambda: button_click("+"))
btn_add.grid(row=1, column=3)
btn_add.configure(font=('verdana', 14))

btn4 = create_rounded_button("4", lambda: button_click(4))
btn4.grid(row=2, column=0)
btn4.configure(font=('verdana', 14))

btn5 = create_rounded_button("5", lambda: button_click(5))
btn5.grid(row=2, column=1)
btn5.configure(font=('verdana', 14))

btn6 = create_rounded_button("6", lambda: button_click(6))
btn6.grid(row=2, column=2)
btn6.configure(font=('verdana', 14))

btn_sub = create_rounded_button("-", lambda: button_click("-"))
btn_sub.grid(row=2, column=3)
btn_sub.configure(font=('verdana', 14))

btn1 = create_rounded_button("1", lambda: button_click(1))
btn1.grid(row=3, column=0)
btn1.configure(font=('verdana', 14))

btn2 = create_rounded_button("2", lambda: button_click(2))
btn2.grid(row=3, column=1)
btn2.configure(font=('verdana', 14))

btn3 = create_rounded_button("3", lambda: button_click(3))
btn3.grid(row=3, column=2)
btn3.configure(font=('verdana', 14))

btn_mul = create_rounded_button("*", lambda: button_click("*"))
btn_mul.grid(row=3, column=3)
btn_mul.configure(font=('verdana', 14))

btn0 = create_rounded_button("0", lambda: button_click(0))
btn0.grid(row=4, column=0)
btn0.configure(font=('verdana', 14))

btn_dot = create_rounded_button(".", lambda: button_click("."))
btn_dot.grid(row=4, column=1)
btn_dot.configure(font=('verdana', 14))

btn_div = create_rounded_button("/", lambda: button_click("/"))
btn_div.grid(row=4, column=2)
btn_div.configure(font=('verdana', 14))

btn_equal = create_rounded_button("=", lambda: calculate())
btn_equal.grid(row=4, column=3)
btn_equal.configure(font=('verdana', 14))

btn_clear = create_rounded_button("Clear", lambda: clear())
btn_clear.grid(row=5, column=0)
btn_clear.configure(font=('verdana', 14))



root.mainloop()