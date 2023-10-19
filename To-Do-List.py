import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def remove_task():
    try:
        selected_task = task_listbox.get(task_listbox.curselection())
        task_listbox.delete(task_listbox.curselection())
        messagebox.showinfo("Task Removed", f"Task '{selected_task}' has been removed.")
    except:
        messagebox.showwarning("Warning", "Please select a task to remove.")

def update_task():
    try:
        selected_task = task_listbox.get(task_listbox.curselection())
        updated_task = task_entry.get()
        if updated_task:
            task_listbox.delete(task_listbox.curselection())
            task_listbox.insert(tk.ACTIVE, updated_task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task to update.")
    except:
        messagebox.showwarning("Warning", "Please select a task to update.")

root = tk.Tk()
root.title("To-Do List")
 
task_entry = tk.Entry(root, width=40)
add_button = tk.Button(root, text="Add Task", command=add_task)
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
update_button = tk.Button(root, text="Update Task", command=update_task)
task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40)

task_entry.grid(row=0, column=0, padx=10, pady=10)
add_button.grid(row=0, column=1, padx=10, pady=10)
remove_button.grid(row=0, column=2, padx=10, pady=10)
update_button.grid(row=0, column=3, padx=10, pady=10)
task_listbox.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

root.mainloop()
