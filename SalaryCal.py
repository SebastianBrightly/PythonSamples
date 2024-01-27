import tkinter as tk
from tkinter import ttk

def calculate_salary():
    try:
        hourly_rate = float(hourly_rate_entry.get() or 25)  # Default value: 25
        hours_worked = float(hours_worked_entry.get() or 40)  # Default value: 40
        work_weeks_per_year = float(work_weeks_entry.get() or 52)  # Default value: 52
        
        annual_salary = hourly_rate * hours_worked * work_weeks_per_year
        result_label.config(text=f"Annual Salary: ${annual_salary:,.2f}")
    except ValueError:
        result_label.config(text="Invalid input. Please enter valid numeric values.")

# Create main window
root = tk.Tk()
root.title("Hourly Rate to Salary Calculator")

# Create and place widgets
hourly_rate_label = ttk.Label(root, text="Hourly Rate:")
hourly_rate_label.grid(row=0, column=0, padx=10, pady=10)
hourly_rate_entry = ttk.Entry(root)
hourly_rate_entry.grid(row=0, column=1, padx=10, pady=10)

hours_worked_label = ttk.Label(root, text="Hours Worked per Day:")
hours_worked_label.grid(row=1, column=0, padx=10, pady=10)
hours_worked_entry = ttk.Entry(root)
hours_worked_entry.grid(row=1, column=1, padx=10, pady=10)

work_weeks_label = ttk.Label(root, text="Work Weeks per Year:")
work_weeks_label.grid(row=2, column=0, padx=10, pady=10)
work_weeks_entry = ttk.Entry(root)
work_weeks_entry.grid(row=2, column=1, padx=10, pady=10)

calculate_button = ttk.Button(root, text="Calculate", command=calculate_salary)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = ttk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# Set default values
hourly_rate_entry.insert(0, "25")
hours_worked_entry.insert(0, "40")
work_weeks_entry.insert(0, "52")

# Start GUI main loop
root.mainloop()
