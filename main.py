import tkinter as tk
from tkinter import ttk


root = tk.Tk() # Declare the root object

def process():
    """
    Purpose
    --------
    To handle what pressing the button to process does.
    Retreves all the enterd marks of the user, and outputs them in the aggregate mark entry
    
    Variables
    ----------
    count - a counter variable
    num_subjects - counter for the number of subjects data is input for
    total_mark - used for totaling the mark of the user, to help with calculating aggregate marks
    agregate - holds the average marks of the user
    
    Lists
    ------
    output - list storing marks of the user per subject
    
    Global vars used
    -----------------
    aggregate_marks - a dictionary which is the aggregate_marks entry showing the answer of the calculation to the user
    entries.subjects = the dictionary that has the entries that user inputs their mark to
    """
    # Initialising Lists
    retrived_marks = [0 for _ in range(10)]
    # Initialising Variables
    subject_no = 0
    number_subjects_processed = 0
    total_of_all_marks = 0
    aggregate_marks = 0
    # Loop to retreve, store and total users marks and find the number of subjects user takes
    for element in entries.subjects:
        retrived_marks[subject_no] = float(entries.subjects[element].get())
        if retrived_marks[subject_no] != -1.0:
            number_subjects_processed += 1
            total_of_all_marks += retrived_marks[subject_no]
        subject_no += 1
    # Checks if the user did input data fr any subject and finds aggregate marks
    # avoids ZeroDivisionError
    # Outputs as a percentage of 100
    if number_subjects_processed != 0:
        aggregate_marks = (total_of_all_marks / (100 * number_subjects_processed)) * 100
    # Print to console as debug logs
    print(f'{number_subjects_processed} subjects detected')
    print(f'Users retreved marks are {retrived_marks}')
    print(f'Users aggregate marks (after calculation){aggregate_marks}')
    #  Display marks in the aggregate marks entry
    aggregate_marks['entry'].delete(0, 'end')
    aggregate_marks['entry'].insert(0, aggregate_marks)


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
