import tkinter as tk
from tkinter import messagebox
import math


def calculate_attendance():
    try:
        total = int(total_entry.get())
        attended = int(attended_entry.get())
        min_percentage = float(min_percentage_entry.get())

        # Input validation
        if total <= 0:
            messagebox.showerror("Error", "Total classes must be greater than 0")
            return

        if attended < 0:
            messagebox.showerror("Error", "Attended classes cannot be negative")
            return

        if attended > total:
            messagebox.showerror("Error", "Attended classes cannot be more than total classes")
            return

        if min_percentage < 0 or min_percentage > 100:
            messagebox.showerror("Error", "Minimum percentage must be between 0 and 100")
            return

        # Calculate current attendance percentage
        current_percentage = (attended / total) * 100
        current_result.config(text=f"Current Attendance: {current_percentage:.2f}%")

        # Check if already meeting minimum requirement
        if current_percentage >= min_percentage:
            status_label.config(text="✓ You already meet the minimum requirement!", fg="green")
            classes_needed_label.config(text="Classes needed: 0")
        else:
            # Calculate classes needed to reach minimum percentage
            # Formula: (attended + x) / (total + x) >= min_percentage/100
            # Solving: x >= (min_percentage * total - 100 * attended) / (100 - min_percentage)

            if min_percentage == 100:
                classes_needed_label.config(text="Classes needed: Impossible to reach 100%")
                status_label.config(text="✗ Cannot reach 100% attendance", fg="red")
                return

            numerator = (min_percentage * total) - (100 * attended)
            denominator = 100 - min_percentage

            if denominator <= 0:
                classes_needed_label.config(text="Classes needed: Cannot calculate")
                status_label.config(text="✗ Invalid calculation", fg="red")
                return

            classes_needed = math.ceil(numerator / denominator)

            if classes_needed <= 0:
                classes_needed = 0
                status_label.config(text="✓ You already meet the minimum requirement!", fg="green")
            else:
                status_label.config(text=f"✗ You need {classes_needed} more classes", fg="red")

            classes_needed_label.config(text=f"Classes needed: {classes_needed}")

            # Show what the attendance will be after attending required classes
            if classes_needed > 0:
                new_total = total + classes_needed
                new_attended = attended + classes_needed
                new_percentage = (new_attended / new_total) * 100
                future_result.config(text=f"Future Attendance: {new_percentage:.2f}%")
            else:
                future_result.config(text="Future Attendance: Already sufficient")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers")


def clear_fields():
    total_entry.delete(0, tk.END)
    attended_entry.delete(0, tk.END)
    min_percentage_entry.delete(0, tk.END)
    current_result.config(text="Current Attendance: --")
    future_result.config(text="Future Attendance: --")
    classes_needed_label.config(text="Classes needed: --")
    status_label.config(text="Status: --", fg="black")


# Create main window
root = tk.Tk()
root.title("Advanced Attendance Calculator")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

# Title
title_label = tk.Label(root, text="Attendance Calculator", font=("Arial", 18, "bold"), bg="#f0f0f0")
title_label.pack(pady=15)

# Input frame
input_frame = tk.Frame(root, bg="#f0f0f0")
input_frame.pack(pady=10)

# Total classes input
total_label = tk.Label(input_frame, text="Total Classes:", font=("Arial", 12), bg="#f0f0f0")
total_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
total_entry = tk.Entry(input_frame, width=15, font=("Arial", 12))
total_entry.grid(row=0, column=1, padx=5, pady=5)

# Attended classes input
attended_label = tk.Label(input_frame, text="Classes Attended:", font=("Arial", 12), bg="#f0f0f0")
attended_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
attended_entry = tk.Entry(input_frame, width=15, font=("Arial", 12))
attended_entry.grid(row=1, column=1, padx=5, pady=5)

# Minimum percentage input
min_percentage_label = tk.Label(input_frame, text="Minimum Required %:", font=("Arial", 12), bg="#f0f0f0")
min_percentage_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)
min_percentage_entry = tk.Entry(input_frame, width=15, font=("Arial", 12))
min_percentage_entry.grid(row=2, column=1, padx=5, pady=5)

# Button frame
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=15)

# Calculate button
calc_button = tk.Button(button_frame, text="Calculate", command=calculate_attendance,
                        bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), width=10)
calc_button.grid(row=0, column=0, padx=5)

# Clear button
clear_button = tk.Button(button_frame, text="Clear", command=clear_fields,
                         bg="#f44336", fg="white", font=("Arial", 12, "bold"), width=10)
clear_button.grid(row=0, column=1, padx=5)

# Results frame
results_frame = tk.Frame(root, bg="#f0f0f0")
results_frame.pack(pady=10)

# Current attendance display
current_result = tk.Label(results_frame, text="Current Attendance: --",
                          font=("Arial", 12, "bold"), bg="#f0f0f0")
current_result.pack(pady=5)

# Future attendance display
future_result = tk.Label(results_frame, text="Future Attendance: --",
                         font=("Arial", 12), bg="#f0f0f0")
future_result.pack(pady=5)

# Classes needed display
classes_needed_label = tk.Label(results_frame, text="Classes needed: --",
                                font=("Arial", 12, "bold"), bg="#f0f0f0")
classes_needed_label.pack(pady=5)

# Status display
status_label = tk.Label(results_frame, text="Status: --",
                        font=("Arial", 12, "bold"), bg="#f0f0f0")
status_label.pack(pady=10)

# Instructions
instructions = tk.Label(root,
                        text="Enter your details above and click Calculate to see how many\nmore classes you need to attend to reach minimum attendance",
                        font=("Arial", 10), bg="#f0f0f0", fg="gray")
instructions.pack(pady=10)

# Start the application
root.mainloop()