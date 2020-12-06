#! /usr/bin/env python3

import csv
import time
from tkinter import *

root = Tk()

root.geometry('800x900')
root.configure(bg='gray7')
root.resizable(1,1)
root.title("CSV File Inspector")

# Function to print filepath and name to tkinter text widget for correctness
def get_file_name(filepath, filename):

    try:
        # Prompt for filename if entry box is empty
        if filename == "":
            text_output_window.insert(END, "\nPlease Enter a File Name ...")
            
        else: # combine filepath and filename and send to tkinter text widget
            msg = filepath + filename
            text_output_window.insert(END, '\n' + msg + '\n')
    # Handle exceptions and send errors to tkinter text widget       
    except Exception as err:
        msg = '\nPlease Enter A Valid File Path and Name ...'
        text_output_window.insert(END, msg )
        text_output_window.insert(END, err)
        
# Function to determine correct file encoding   
def get_encoding(filepath, filename):
    # Combine file and path for file
    csv_doc = str(filepath + filename)

    try:  # Open file in read mode and retrieve file encoding  
        with open(csv_doc, 'r', errors='ignore') as file:
            fencode = file.encoding
            text_output_window.insert(END, fencode + '\n')
            
            return(fencode)
    
    except Exception:
        msg = '\nPlease Enter A Valid File Path and Name ...'
        text_output_window.insert(END, msg)
        
        
def get_file_headers(filepath, filename):
    # Create variable for filepath and filename combined
    file = filepath + filename
    fencode = get_encoding(filepath, filename) # Get encoding

    try:
        with open(file, 'r', encoding=fencode, errors='ignore', 
            newline='') as f:
            
            reader = csv.reader(f)
            header_row = next(reader) # Read headers
            
            count = 0
            
            for row in header_row:
                
                header_string = ("Header Index " + str(count) + " " + 
                    row + '\n')
                text_output_window.insert(END, header_string)
                
                count += 1
                
    except Exception:
        msg = '\nPlease Enter A Valid File Path and Name ...'
        text_output_window.insert(END, msg)   
                

def text_print(filepath, filename):

    new_file = (filepath + filename + '.txt')
     
    date = time.strftime('%B %d, %Y')
    clock_time = time.strftime('%I:%M %p')
     
    phrase1 = ("                   'CSV File Inspector' \n" + 
        "                    Author: promontorycoder \n" + 
        "                    Author Email: promontorycoder@tutanota.com \n" +
        "                    GitHub: https://github.com/promontorycoder \n" +
        "\nCSV File Results Produced On ")
    phrase2 = " at "
    
    doc_write = (phrase1 + date + phrase2 + clock_time + '\n' + 
        text_output_window.get(1.0, END))
    
    with open(new_file, 'w') as file_object:
        file_object.write(doc_write)

def search_csv(filepath, filename, search_criteria):
    
    file = filepath + filename
    fencode = get_encoding(filepath, filename)
    search_term = search_criteria.upper()
    
    try:
        with open(file, 'r', encoding=fencode, errors='ignore',
            newline='') as f:
            
            reader = csv.reader(f)
            
            included_cols = []
            
            columns = [int(x) for x in entry_columns.get().split()]
            for column in columns:
                included_cols.append(column)
            
            for row in reader:
                if search_term in row:
                    content = list(row[i] for i in included_cols)
                    text_output_window.insert(END, content)
                    text_output_window.insert(END, '\n')
           
                
    except Exception as err:
        text_output_window.insert(END, '\n' + str(err))
        text_output_window.insert(END, '\nSearch Criteria Not Found ...')


def whole_column(filepath, filename):
    
    file = filepath + filename
    fencode = get_encoding(filepath, filename)
        
    try:
        with open(file, 'r', encoding=fencode, errors='ignore',
            newline='') as f:
            
            reader = csv.reader(f)
            
            included_cols = []
            
            columns = [int(x) for x in entry_columns.get().split()]
            for column in columns:
                included_cols.append(column)
            
            for row in reader:
                content = list(row[i] for i in included_cols)
                text_output_window.insert(END, content)
                text_output_window.insert(END, '\n')
           
                
    except Exception as err:
        text_output_window.insert(END, '\n' + str(err))
        text_output_window.insert(END, '\nSearch Criteria Not Found ...')
        text_output_window.insert(END, '\nPlease enter column to be returned.')
    

def read_file(filepath, filename):
    
    file = filepath + filename
    fencode = get_encoding(filepath, filename)
    
    fields = []
    rows = []
    
    try:
        with open(file, 'r', encoding=fencode, errors='ignore', 
            newline='') as f:
        
            reader = csv.reader(f)
            
            fields = next(reader)
            for row in reader:
                rows.append(row)
            
            rows_num = ("\nTotal No. of rows: %d"%(reader.line_num))    
            text_output_window.insert(END, rows_num)
            text_output_window.insert(END, '\n')
        
        op_fields = ("Field names are: " + ', '.join(field for field in fields))
        text_output_window.insert(END, op_fields)
        text_output_window.insert(END, '\n')
        
        for row in rows:
            for col in row:
                op_print = ("%10s"%col)
                # text_output_window.insert(END, '\n'
                text_output_window.insert(END, op_print)
            text_output_window.insert(END, '\n')
                
    except Exception as err:
        text_output_window.insert(END, '\n' + str(err))
        text_output_window.insert(END, '\nUnable to process file ...')


def read_part(filepath, filename):
    
    file = filepath + filename
    fencode = get_encoding(filepath, filename)
    
    fields = []
    rows = []
    
    try:
        with open(file, 'r', encoding=fencode, errors='ignore', 
            newline='') as f:
        
            reader = csv.reader(f)
            
            fields = next(reader)
            for row in reader:
                rows.append(row)
            
            rows_num = ("\nTotal No. of rows: %d"%(reader.line_num))    
            text_output_window.insert(END, rows_num)
            text_output_window.insert(END, '\n')
        
        op_fields = ("Field names are: " + ', '.join(field for field in fields))
        text_output_window.insert(END, op_fields)
        text_output_window.insert(END, '\n')
        text_output_window.insert(END, 'First 5 rows are:\n')
        
        for row in rows[:5]:
            for col in row:
                op_print = ("%10s"%col)
                # text_output_window.insert(END, '\n'
                text_output_window.insert(END, op_print)
            text_output_window.insert(END, '\n')
                
    except Exception as err:
        text_output_window.insert(END, '\n' + str(err))
        text_output_window.insert(END, '\nUnable to process file ...')


def clear_output():
    text_output_window.delete(1.0, END)
    

def clear_filepath():
    entry_filepath.delete(0, 'end')


def clear_filename():
    entry_filename.delete(0, 'end')


def clear_search():
    entry_search_criteria.delete(0, 'end')


def clear_columns():
    entry_columns.delete(0, 'end')


def Exit():
    exit()


# Create tkinter Labels
label_enter_filename = Label(root, 
    text = "Enter Filename: ", 
    font = 'arial 10', 
    bg='gray7', 
    fg='lime green'
    )
    
label_output = Label(root, 
    text = "Output: ", 
    font = 'arial 14 bold', 
    bg='gray7', 
    fg='lime green'
    )

label_enter_filepath = Label(root, 
    text = "Enter File Path: ", 
    font = 'arial 10', 
    bg='gray7', 
    fg='lime green'
    )

label_enter_search_criteria = Label(root, 
    text = "Enter Search Criteria:", 
    font = 'arial 12', 
    bg='gray7', 
    fg='lime green'
    )

label_columns = Label(root, 
    text = "Enter columns to be RETURNED, separated by spaces: ", 
    font = 'arial 10', 
    bg='gray7', 
    fg='lime green'
    )

label_output_filepath = Label(root, 
    text = "Enter file path for printing output:", 
    font = 'arial 10', 
    bg='gray7', 
    fg='lime green'
    )

label_output_filename = Label(root, 
    text = "Enter file name for printing output:", 
    font = 'arial 10', 
    bg='gray7', 
    fg='lime green'
    )

label_enter_filename.place(x=50, y=55)
label_output.place(x=50, y=120)
label_enter_filepath.place(x=50, y=5)
label_enter_search_criteria.place(x=400, y=55)
label_columns.place(x=400, y=5)
label_output_filepath.place(x=350, y=760)
label_output_filename.place(x=350, y=800)


# Create tkinter text output widget
text_output_window = Text(root, 
    height=35, 
    width=85, 
    borderwidth=1, 
    relief='ridge', 
    bg='gray7', 
    fg='lime green'
    )

text_output_window.place(x=50, y=150)

# Create Scrollbar for text widget
scrollbar = Scrollbar(root)
scrollbar.place(x=750, y=400)

# Configure commands for scrollbar and tie to text widget
text_output_window.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=text_output_window.yview, 
    bg='gray7', 
    activebackground='lime green', 
    highlightcolor='lime green', 
    width=15
    )


# Create Entry Boxes
entry_filepath = Entry(root, 
    font = 'arial 10', 
    width=25, 
    bg='gray7', 
    fg='lime green'
    )

entry_filename = Entry(root, 
    font = 'arial 10', 
    width=25, 
    bg='gray7', 
    fg='lime green'
    )
    
entry_search_criteria = Entry(root, 
    font = 'arial 10', 
    width=50, 
    bg='gray7', 
    fg='lime green'
    )

entry_columns = Entry(root, 
    font = 'arial 10', 
    width=50, 
    bg='gray7', 
    fg='lime green'
    )

entry_output_filepath = Entry(root, 
    font = 'arial 10', 
    width=40, 
    bg='gray7', 
    fg='lime green'
    )

entry_output_filename = Entry(root, 
    font = 'arial 10', 
    width=40, 
    bg='gray7', 
    fg='lime green'
    )

# Place entry boxes in tkinter window frame
entry_filename.place(x=50, y=80)
entry_filepath.place(x=50, y=30)
entry_search_criteria.place(x=400, y=80)
entry_columns.place(x=400, y=30)
entry_output_filepath.place(x=350, y=780)
entry_output_filename.place(x=350, y=820)


# Create Buttons
btn_get_file = Button(root, 
    command = lambda: get_file_name(entry_filepath.get(), entry_filename.get()),
    text = 'Get File',
    font = 'arial 10', 
    bg='gray7', 
    fg='lime green'
    )

btn_get_encoding = Button(root, 
    command = lambda: get_encoding(entry_filepath.get(), entry_filename.get()),
    text = 'Get File Encoding', 
    font = 'arial 10', 
    bg='gray7', 
    fg='lime green'
    )

btn_get_file_headers = Button(root, 
    command = lambda: get_file_headers(entry_filepath.get(), entry_filename.get()), 
    text = 'Get File Headers', 
    font = 'arial 10', 
    bg='gray7', 
    fg='lime green'
    )
    
btn_clear_filepath = Button(root, 
    command = clear_filepath, 
    text = 'Clear File Path', 
    font = 'arial 8', 
    bg='gray7', 
    fg='lime green'
    )

btn_clear_filename = Button(root, 
    command = clear_filename, 
    text = 'Clear File Name', 
    font = 'arial 8', 
    bg='gray7', 
    fg='lime green'
    )

btn_clear_output = Button(root, 
    command = clear_output, 
    text = 'Clear Output', 
    font = 'arial 8', 
    bg='gray7', 
    fg='lime green'
    )

btn_clear_search = Button(root, 
    command = clear_search, 
    text = 'Clear Search', 
    font = 'arial 8', 
    bg='gray7', 
    fg='lime green'
    )

btn_search = Button(root, 
    command = lambda: search_csv(entry_filepath.get(), entry_filename.get(), 
        entry_search_criteria.get()), 
    text = 'SEARCH', 
    font = 'arial 10', 
    bg='lime green', 
    fg='gray7'
    )

btn_exit = Button(root, 
    command = Exit, 
    text = 'EXIT', 
    font = 'arial 10 bold', 
    bg = 'OrangeRed', 
    width=6, 
    padx=2, 
    pady=1
    )

btn_print = Button(root, 
    command = lambda: text_print(entry_output_filepath.get(), entry_output_filename.get()), 
    text = 'Print', 
    font = 'arial 10', 
    bg='royal blue', 
    fg='lime green'
    )

btn_clear_columns = Button(root, 
    command = clear_columns, 
    text = 'Clear Columns', 
    font = 'arial 8', 
    bg='gray7', 
    fg='lime green'
    )

btn_read_file = Button(root, 
    command = lambda: read_file(entry_filepath.get(), entry_filename.get()), 
    text = 'Read File', 
    font = 'arial 10', 
    bg='lime green', 
    fg='gray7'
    )

btn_read_5_rows = Button(root, 
    command = lambda: read_part(entry_filepath.get(), entry_filename.get()), 
    text = 'Read 5 Rows', 
    font = 'arial 10', 
    bg='lime green', 
    fg='gray7'
    )

btn_read_columns = Button(root, 
    command = lambda: whole_column(entry_filepath.get(), entry_filename.get()), 
    text = 'Read Columns', 
    font = 'arial 10', 
    bg='lime green', 
    fg='gray7'
    )

# Place buttons on the tkinter window frame
btn_get_file.place(x=50, y=760)
btn_get_encoding.place(x=50, y=800)
btn_get_file_headers.place(x=50, y=840)
btn_clear_filepath.place(x=260, y=27)
btn_clear_filename.place(x=260, y=77)
btn_clear_output.place(x=150, y=117)
btn_clear_search.place(x=600, y=117)
btn_search.place(x=400, y=117)
btn_exit.place(x=725, y=850)
btn_print.place(x=650, y=795)
btn_clear_columns.place(x=600, y=52)
btn_read_file.place(x=220, y=760)
btn_read_5_rows.place(x=220, y=800)
btn_read_columns.place(x=220, y=840)

root.mainloop()
