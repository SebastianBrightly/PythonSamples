import tkinter as tk
from tkinter import messagebox

def open_todo_menu(root,tasks):
    todo_window = tk.Toplevel(root)
    todo_window.title("To-Do List")
    todo_window.minsize(300, 200)

    def show_tasks():
        if not tasks:
            task_display.config(text="No tasks in the list.")
        else:
            task_display.config(text="Tasks:\n" + "\n".join(tasks))

    def add_task():
        new_task = task_entry.get()
        if new_task:
            tasks.append(new_task)
            task_entry.delete(0, tk.END)
            messagebox.showinfo("Success", f"Task '{new_task}' added.")
            show_tasks()
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task():
        try:
            index = int(task_index_entry.get())
            if 1 <= index <= len(tasks):
                removed_task = tasks.pop(index - 1)
                messagebox.showinfo("Success", f"Task '{removed_task}' removed.")
                show_tasks()
            else:
                messagebox.showwarning("Warning", "Invalid task number.")
        except ValueError:
            messagebox.showwarning("Warning", "Please enter a valid task number.")

    task_label = tk.Label(todo_window, text="Enter task:")
    task_entry = tk.Entry(todo_window, width=30)
    add_button = tk.Button(todo_window, text="Add Task", command=add_task)

    task_index_label = tk.Label(todo_window, text="Enter task number to remove:")
    task_index_entry = tk.Entry(todo_window, width=5)
    remove_button = tk.Button(todo_window, text="Remove Task", command=remove_task)

    show_button = tk.Button(todo_window, text="Show Tasks", command=show_tasks)
    task_display = tk.Label(todo_window, text="", justify=tk.LEFT)

    task_label.pack()
    task_entry.pack()
    add_button.pack()

    task_index_label.pack()
    task_index_entry.pack()
    remove_button.pack()

    show_button.pack()
    task_display.pack()