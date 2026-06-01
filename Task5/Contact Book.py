from tkinter import *
from tkinter import messagebox
import json
import os

# ---------------- SAVE FILE ----------------
FILE_NAME = "contacts.json"

# ---------------- LOAD CONTACTS ----------------
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        contacts = json.load(file)
else:
    contacts = []

# ---------------- SAVE CONTACTS ----------------
def save_contacts():
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)

# ---------------- ADD CONTACT ----------------
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name == "" or phone == "":
        messagebox.showerror("Error", "Name and Phone are required!")
        return

    contacts.append([name, phone, email, address])

    save_contacts()

    messagebox.showinfo("Success", "Contact Added Successfully!")

    clear_fields()
    view_contacts()

# ---------------- VIEW CONTACTS ----------------
def view_contacts():
    listbox.delete(0, END)

    for contact in contacts:
        listbox.insert(END, contact[0] + " - " + contact[1])

# ---------------- SEARCH CONTACT ----------------
def search_contact():
    search = search_entry.get().lower()

    listbox.delete(0, END)

    for contact in contacts:
        if search in contact[0].lower() or search in contact[1]:
            listbox.insert(END, contact[0] + " - " + contact[1])

# ---------------- SELECT CONTACT ----------------
def select_contact(event):
    selected = listbox.curselection()

    if selected:
        selected_text = listbox.get(selected[0])

        for index, contact in enumerate(contacts):
            contact_text = contact[0] + " - " + contact[1]

            if selected_text == contact_text:

                clear_fields()

                name_entry.insert(0, contact[0])
                phone_entry.insert(0, contact[1])
                email_entry.insert(0, contact[2])
                address_entry.insert(0, contact[3])

                global selected_index
                selected_index = index

# ---------------- UPDATE CONTACT ----------------
def update_contact():
    try:
        contacts[selected_index] = [
            name_entry.get(),
            phone_entry.get(),
            email_entry.get(),
            address_entry.get()
        ]

        save_contacts()

        messagebox.showinfo("Success", "Contact Updated Successfully!")

        clear_fields()
        view_contacts()

    except:
        messagebox.showerror("Error", "Please Select a Contact")

# ---------------- DELETE CONTACT ----------------
def delete_contact():
    try:
        contacts.pop(selected_index)

        save_contacts()

        messagebox.showinfo("Success", "Contact Deleted Successfully!")

        clear_fields()
        view_contacts()

    except:
        messagebox.showerror("Error", "Please Select a Contact")

# ---------------- CLEAR FIELDS ----------------
def clear_fields():
    name_entry.delete(0, END)
    phone_entry.delete(0, END)
    email_entry.delete(0, END)
    address_entry.delete(0, END)

# ---------------- MAIN WINDOW ----------------
root = Tk()
root.title("Colorful Contact Book")
root.geometry("700x650")
root.configure(bg="#1E1E2F")

# ---------------- TITLE ----------------
title = Label(
    root,
    text="📒 CONTACT BOOK",
    font=("Arial", 22, "bold"),
    bg="#1E1E2F",
    fg="gold"
)
title.pack(pady=15)

# ---------------- NAME ----------------
Label(root,
      text="Name",
      bg="#1E1E2F",
      fg="white",
      font=("Arial", 12, "bold")).pack()

name_entry = Entry(
    root,
    width=40,
    font=("Arial", 11),
    bg="#F5F5F5"
)
name_entry.pack(pady=5)

# ---------------- PHONE ----------------
Label(root,
      text="Phone",
      bg="#1E1E2F",
      fg="white",
      font=("Arial", 12, "bold")).pack()

phone_entry = Entry(
    root,
    width=40,
    font=("Arial", 11),
    bg="#F5F5F5"
)
phone_entry.pack(pady=5)

# ---------------- EMAIL ----------------
Label(root,
      text="Email",
      bg="#1E1E2F",
      fg="white",
      font=("Arial", 12, "bold")).pack()

email_entry = Entry(
    root,
    width=40,
    font=("Arial", 11),
    bg="#F5F5F5"
)
email_entry.pack(pady=5)

# ---------------- ADDRESS ----------------
Label(root,
      text="Address",
      bg="#1E1E2F",
      fg="white",
      font=("Arial", 12, "bold")).pack()

address_entry = Entry(
    root,
    width=40,
    font=("Arial", 11),
    bg="#F5F5F5"
)
address_entry.pack(pady=5)

# ---------------- BUTTON FRAME ----------------
button_frame = Frame(root, bg="#1E1E2F")
button_frame.pack(pady=15)

Button(
    button_frame,
    text="Add Contact",
    bg="#28A745",
    fg="white",
    font=("Arial", 10, "bold"),
    width=15,
    command=add_contact
).grid(row=0, column=0, padx=5)

Button(
    button_frame,
    text="Update Contact",
    bg="#007BFF",
    fg="white",
    font=("Arial", 10, "bold"),
    width=15,
    command=update_contact
).grid(row=0, column=1, padx=5)

Button(
    button_frame,
    text="Delete Contact",
    bg="#DC3545",
    fg="white",
    font=("Arial", 10, "bold"),
    width=15,
    command=delete_contact
).grid(row=0, column=2, padx=5)

# ---------------- SEARCH SECTION ----------------
Label(
    root,
    text="Search Contact",
    bg="#1E1E2F",
    fg="gold",
    font=("Arial", 12, "bold")
).pack(pady=5)

search_entry = Entry(
    root,
    width=40,
    font=("Arial", 11),
    bg="#F5F5F5"
)
search_entry.pack()

Button(
    root,
    text="Search",
    bg="#FFC107",
    fg="black",
    font=("Arial", 10, "bold"),
    width=15,
    command=search_contact
).pack(pady=10)

# ---------------- CONTACT LIST ----------------
listbox = Listbox(
    root,
    width=60,
    height=12,
    font=("Arial", 11),
    bg="#F8F9FA",
    fg="#000080",
    selectbackground="#6A5ACD"
)
listbox.pack(pady=10)

listbox.bind("<<ListboxSelect>>", select_contact)

# ---------------- VIEW BUTTON ----------------
Button(
    root,
    text="View All Contacts",
    bg="#17A2B8",
    fg="white",
    font=("Arial", 10, "bold"),
    width=20,
    command=view_contacts
).pack(pady=5)

# ---------------- LOAD CONTACTS ON START ----------------
view_contacts()

# ---------------- RUN WINDOW ----------------
root.mainloop()