import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("To-Do List ")
root.geometry("400x450")
root.config(bg="#f0f0f0")
tasks = []


def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected_index = listbox.curselection()[0]
        tasks.pop(selected_index)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")


title = tk.Label(root, text="🧠 Your To-Do List", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
title.pack(pady=10)

entry = tk.Entry(root, font=("Helvetica", 12), width=30)
entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Task", command=add_task, bg="#4CAF50", fg="white", width=20)
add_btn.pack(pady=5)

delete_btn = tk.Button(root, text="Delete Selected Task", command=delete_task, bg="#f44336", fg="white", width=20)
delete_btn.pack(pady=5)

listbox = tk.Listbox(root, font=("Helvetica", 12), width=40, height=12)
listbox.pack(pady=20)

root.mainloop()
