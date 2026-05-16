from tkinter import *

# Create window
window = Tk()

window.title("To-Do List")
window.geometry("400x400")

# List to store tasks
tasks = []

# Function to add task
def add_task():

    task = entry_box.get()

    if task != "":

        tasks.append(task)

        listbox.insert(END, task)

        entry_box.delete(0, END)

    else:

        status_label.config(text="Please enter a task")


# Function to delete task
def delete_task():

    selected = listbox.curselection()

    if selected:

        index = selected[0]

        listbox.delete(index)

        tasks.pop(index)

    else:

        status_label.config(text="Select a task to delete")


# Title label
title_label = Label(window, text="TO-DO LIST", font=("Arial", 18))

title_label.pack(pady=10)

# Entry box
entry_box = Entry(window, width=30, font=("Arial", 14))

entry_box.pack(pady=10)

# Add button
add_button = Button(window,
                    text="Add Task",
                    width=15,
                    command=add_task)

add_button.pack(pady=5)

# Listbox
listbox = Listbox(window,
                  width=40,
                  height=10,
                  font=("Arial", 12))

listbox.pack(pady=10)

# Delete button
delete_button = Button(window,
                       text="Delete Task",
                       width=15,
                       command=delete_task)

delete_button.pack(pady=5)

# Status label
status_label = Label(window,
                     text="",
                     fg="red")

status_label.pack()

# Run window
window.mainloop()