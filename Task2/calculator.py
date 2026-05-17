from tkinter import *

# Create window
window = Tk()
window.title("Simple Calculator")
window.geometry("300x300")

# Functions
def calculate():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    op = operation.get()

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero"
    else:
        result = "Invalid Operation"

    result_label.config(text="Result: " + str(result))

# Labels
label1 = Label(window, text="Enter First Number")
label1.pack()

# Entry for first number
entry1 = Entry(window)
entry1.pack()

# Label
label2 = Label(window, text="Enter Second Number")
label2.pack()

# Entry for second number
entry2 = Entry(window)
entry2.pack()

# Operation input
label3 = Label(window, text="Enter Operation (+, -, *, /)")
label3.pack()

operation = Entry(window)
operation.pack()

# Button
calc_button = Button(window, text="Calculate", command=calculate)
calc_button.pack(pady=10)

# Result label
result_label = Label(window, text="Result: ")
result_label.pack()

# Run window
window.mainloop()