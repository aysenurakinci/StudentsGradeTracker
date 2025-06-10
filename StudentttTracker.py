import tkinter as tk  # Import tkinter library for GUI
from tkinter import messagebox  # Import messagebox for pop-up alerts

# Create the main window
root = tk.Tk()
root.title("Student Grade Tracker")
root.geometry("400x400")

# Function to calculate average and determine pass/fail
def calculate_result():
    name = entry_name.get()  # Getting the student's name from input
    grade1 = entry_grade1.get()  # Getting the first grade
    grade2 = entry_grade2.get()  # Getting the second grade

    try:
        grade1 = float(grade1)  # Converting grade1 to float
        grade2 = float(grade2)  # Converting grade2 to float
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter numeric grades.")
        return

    average = (grade1 + grade2) / 2  # Calculating average
    status = "Passed" if average >= 50 else "Failed"  # Determine status

    result = f"Student: {name}\nAverage: {average:.2f}\nStatus: {status}"  # Format result
    label_result.config(text=result)  # Showing result in the label

# GUI Elements
label_name = tk.Label(root, text="Student Name:")
label_name.pack()

entry_name = tk.Entry(root)
entry_name.pack()

label_grade1 = tk.Label(root, text="Grade 1:")
label_grade1.pack()

entry_grade1 = tk.Entry(root)
entry_grade1.pack()

label_grade2 = tk.Label(root, text="Grade 2:")
label_grade2.pack()

entry_grade2 = tk.Entry(root)
entry_grade2.pack()

btn_calculate = tk.Button(root, text="Calculate Result", command=calculate_result)
btn_calculate.pack(pady=10)

label_result = tk.Label(root, text="", font=("Arial", 12), fg="blue")
label_result.pack()

root.mainloop()  # Run the GUI event loop
