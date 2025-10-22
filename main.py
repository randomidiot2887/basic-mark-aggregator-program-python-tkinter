import tkinter as tk
from tkinter import ttk


root = tk.Tk() # Declare the root object

def process():
    output = ['' for _ in range(10)]
    count = 0
    num_subjects = 0
    total_mark = 0
    for element in entries.subjects:
        output[count] = float(entries.subjects[element].get())
        if output[count] != -1.0:
            num_subjects += 1
            total_mark += output[count]
        count += 1
    agregate = 0
    if num_subjects != 0:
        agregate = (total_mark / (100 * num_subjects)) * 100
    
    print(output)
    print(agregate)
    aggregate_marks['entry'].delete(0, 'end')
    aggregate_marks['entry'].insert(0, agregate)


root.title('Marks aggregator v1.0') # makes the title of the window
Window_Title = ttk.Label(root, text='Marks aggregator') # Main heading of the window

class entries: # class containng entries for subjects where use inputs data
    subjects = {
        'english' : ttk.Entry(root),
        'dhivehi' : ttk.Entry(root),
        'mathematics' : ttk.Entry(root),
        'chemistry' : ttk.Entry(root),
        'physics' : ttk.Entry(root),
        'biology' : ttk.Entry(root),
        'marine science' : ttk.Entry(root),
        'business' : ttk.Entry(root),
        'accounting' : ttk.Entry(root),
        'economics' : ttk.Entry(root)
    }

class labels: # Class contaning labels for subjects
    subjects = {
        'english' : ttk.Label(root, text='English'),
        'dhivehi' : ttk.Label(root, text='Dhivehi'),
        'mathematics' : ttk.Label(root, text='Mathematics'),
        'chemistry' : ttk.Label(root, text='Chemistry'),
        'physics' : ttk.Label(root, text='Physics'),
        'biology' : ttk.Label(root, text='Biology'),
        'marine science' : ttk.Label(root, text='Marine Science'),
        'business' : ttk.Label(root, text='Business'),
        'accounting' : ttk.Label(root, text='Accounting'),
        'economics' : ttk.Label(root, text='Economics')
    }

aggregate_marks = { # Dictionary containing users agregate marks and its label
    'label' : ttk.Label(root, text='Aggregated Mark'),
    'entry' : ttk.Entry(root)
}

#aggregate_marks['entry'].config(state='readonly') # Sets aggregatemarks to read only
aggregate_marks['entry'].insert(0, '0') # Sets agregate marks entry value to 0

# sets the positions and arrangement of the entries, and labels
row_count = 1
for element in labels.subjects:
    entries.subjects[element].insert(0, '-1')
    entries.subjects[element].grid(row=row_count, column=1, padx=10, pady=5)
    labels.subjects[element].grid(row=row_count, column=0, padx=10, pady=5)
    row_count += 1
column_count = 0
for element in aggregate_marks:
    aggregate_marks[element].grid(row=row_count+1, column=column_count, padx=10, pady=5)
    column_count += 1
Window_Title.grid(row=0, column=0, columnspan=2)

# sets up the one button
calculate = ttk.Button(root, text='Calculate', command=process)
calculate.grid(row=row_count, column=0, columnspan=2, padx=5, pady=10)
root.mainloop()

# Fixes are needed