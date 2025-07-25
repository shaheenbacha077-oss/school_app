import tkinter as tk
from tkinter import messagebox
import json

file_name = "students.json"

def save_data(name, student_class, marks):
    if not name or not student_class or not marks:
        messagebox.showerror("Error", "Please fill all fields!")
        return
    try:
        marks = float(marks)
    except ValueError:
        messagebox.showerror("Error", "Marks must be a number!")
        return

    try:
        with open(file_name, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    data.append({
        "name": name,
        "class": student_class,
        "marks": marks
    })

    with open(file_name, "w") as f:
        json.dump(data, f, indent=4)

    messagebox.showinfo("Success", f"Record added for {name}")
    entry_name.delete(0, tk.END)
    entry_class.delete(0, tk.END)
    entry_marks.delete(0, tk.END)

# GUI
root = tk.Tk()
root.title("🎓 Student Record Entry")
root.geometry("400x300")
root.configure(bg="#f0f8ff")

title = tk.Label(root, text="Add Student Record", font=("Arial", 18, "bold"), bg="#f0f8ff", fg="#333")
title.pack(pady=10)

frame = tk.Frame(root, bg="#f0f8ff")
frame.pack(pady=5)

tk.Label(frame, text="Name:", bg="#f0f8ff", fg="#000").grid(row=0, column=0, sticky="e", padx=10, pady=5)
entry_name = tk.Entry(frame, width=30)
entry_name.grid(row=0, column=1)

tk.Label(frame, text="Class:", bg="#f0f8ff", fg="#000").grid(row=1, column=0, sticky="e", padx=10, pady=5)
entry_class = tk.Entry(frame, width=30)
entry_class.grid(row=1, column=1)

tk.Label(frame, text="Marks:", bg="#f0f8ff", fg="#000").grid(row=2, column=0, sticky="e", padx=10, pady=5)
entry_marks = tk.Entry(frame, width=30)
entry_marks.grid(row=2, column=1)

btn = tk.Button(root, text="➕ Add Record", bg="#007acc", fg="white", width=20,
                command=lambda: save_data(entry_name.get(), entry_class.get(), entry_marks.get()))
btn.pack(pady=20)

root.mainloop()
