import tkinter as tk
from tkinter import messagebox
import ToDoListApp as tda
import weatherapi as weaapp

tasks = []


def open_sample_app(app_name,root):
    global tasks
    if app_name == "To-Do List":
        tda.open_todo_menu(root,tasks)
    elif app_name == "Weather App":
        weaapp.open_weather_app(root)
        #to do fix why this one is not opening


root = tk.Tk()
root.title("Sample App Selector")
root.minsize(200, 100)

app_label = tk.Label(root, text="Select an app sample:")
app_label.pack()

app_list = ["To-Do List","Weather App","Test"]  # Add more sample apps here if needed

for app_name in app_list:
    app_button = tk.Button(root, text=app_name, command=lambda name=app_name: open_sample_app(name,root))
    app_button.pack()

root.mainloop()
