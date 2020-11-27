#! /usr/bin/env python3

import csv
import time
from tkinter import *

root = Tk()

root.geometry('800x900')
root.configure(bg='gray7')
root.resizable(1,1)
root.title("CSV File Inspector")

global filename

# filename = 'EntireStateVoters.csv'

def get_file_name():

    try:

        if E1.get() == "":
            T1.insert(END, "\nPlease Enter a File Name ...")
            
        else:
            global filename
        
            getfn = E1.get()
            getfp = E2.get()
            gfile = getfp + getfn
            T1.insert(END, '\n' + gfile + '\n')
            
            filename = gfile
        
    except Exception:
        T1.insert(END, '\nPlease Enter A Valid File Path and Name ...')
        
        
   
def get_encoding():

    global filename
    global fencode
    
    try:    
        with open(filename, 'r', errors='ignore') as file:
            fencode = file.encoding
            T1.insert(END, fencode + '\n')
    
    except Exception:
        T1.insert(END, '\nPlease Enter A Valid File Path and Name ...')
        
        
def print_headers():

    global filename
    global fencode
    
    try:
        with open(filename, 'r', encoding=fencode, errors='ignore', 
            newline='') as f:
            
            reader = csv.reader(f)
            header_row = next(reader)
            
            header_file=open(filename + '_headers.txt', 'w')
            
            count = 0
            
            for row in header_row:
                
                header_file.write(row)
                header_file.write('\n')
                
                header_string = ("Header Index " + str(count) + " " + 
                    row + '\n')
                T1.insert(END, header_string)
                
                count += 1
                
    except Exception:
        T1.insert(END, '\nPlease Enter A Valid File Path and Name ...')   
                

def text_print():

    
    fp = E5.get()
    fn = E6.get()
    new_file = (fp + fn + '.txt')
     
    date = time.strftime('%B %d, %Y')
    clock_time = time.strftime('%I:%M %p')
     
    phrase1 = ("                   'CSV File Inspector' \n" + 
        "                    Author: promontorycoder \n" + 
        "                    Author Email: promontorycoder@tutanota.com \n" +
        "                    GitHub: https://github.com/promontorycoder \n" +
        "\nCSV File Results Produced On ")
    phrase2 = " at "
    
    doc_write = (phrase1 + date + phrase2 + clock_time + '\n' + 
        T1.get(1.0, END))
    
    with open(new_file, 'w') as file_object:
        file_object.write(doc_write)

def search_csv():
    
    global filename
    global fencode
    global included_cols
    
    search_get = E3.get()
    search_term = search_get.upper()
    
    try:
        with open(filename, 'r', encoding=fencode, errors='ignore',
            newline='') as f:
            
            reader = csv.reader(f)
            
            included_cols = []
            
            columns = [int(x) for x in E4.get().split()]
            for column in columns:
                included_cols.append(column)
            
            for row in reader:
                if search_term in row:
                    content = list(row[i] for i in included_cols)
                    T1.insert(END, content)
                    T1.insert(END, '\n')
           
                
    except Exception as err:
        T1.insert(END, '\n' + str(err))
        T1.insert(END, '\nSearch Criteria Not Found ...')


def whole_column():
    
    global filename
    global fencode
    global included_cols
    
    try:
        with open(filename, 'r', encoding=fencode, errors='ignore',
            newline='') as f:
            
            reader = csv.reader(f)
            
            included_cols = []
            
            columns = [int(x) for x in E4.get().split()]
            for column in columns:
                included_cols.append(column)
            
            for row in reader:
                content = list(row[i] for i in included_cols)
                T1.insert(END, content)
                T1.insert(END, '\n')
           
                
    except Exception as err:
        T1.insert(END, '\n' + str(err))
        T1.insert(END, '\nSearch Criteria Not Found ...')
        T1.insert(END, '\nPlease enter column to be returned.')
    

def read_file():
    
    global filename
    global fencode
    
    fields = []
    rows = []
    
    try:
        with open(filename, 'r', encoding=fencode, errors='ignore', 
            newline='') as f:
        
            reader = csv.reader(f)
            
            fields = next(reader)
            for row in reader:
                rows.append(row)
            
            rows_num = ("\nTotal No. of rows: %d"%(reader.line_num))    
            T1.insert(END, rows_num)
            T1.insert(END, '\n')
        
        op_fields = ("Field names are: " + ', '.join(field for field in fields))
        T1.insert(END, op_fields)
        T1.insert(END, '\n')
        
        for row in rows:
            for col in row:
                op_print = ("%10s"%col)
                # T1.insert(END, '\n'
                T1.insert(END, op_print)
            T1.insert(END, '\n')
                
    except Exception as err:
        T1.insert(END, '\n' + str(err))
        T1.insert(END, '\nUnable to process file ...')


def read_part():
    
    global filename
    global fencode
    
    fields = []
    rows = []
    
    try:
        with open(filename, 'r', encoding=fencode, errors='ignore', 
            newline='') as f:
        
            reader = csv.reader(f)
            
            fields = next(reader)
            for row in reader:
                rows.append(row)
            
            rows_num = ("\nTotal No. of rows: %d"%(reader.line_num))    
            T1.insert(END, rows_num)
            T1.insert(END, '\n')
        
        op_fields = ("Field names are: " + ', '.join(field for field in fields))
        T1.insert(END, op_fields)
        T1.insert(END, '\n')
        T1.insert(END, 'First 5 rows are:\n')
        
        for row in rows[:5]:
            for col in row:
                op_print = ("%10s"%col)
                # T1.insert(END, '\n'
                T1.insert(END, op_print)
            T1.insert(END, '\n')
                
    except Exception as err:
        T1.insert(END, '\n' + str(err))
        T1.insert(END, '\nUnable to process file ...')


def clear_output():
    T1.delete(1.0, END)
    

def clear_filep():
    E2.delete(0, 'end')


def clear_filen():
    E1.delete(0, 'end')


def clear_search():
    E3.delete(0, 'end')


def clear_columns():
    E4.delete(0, 'end')


def Exit():
    exit()


# Create tkinter Labels
L1 = Label(root, text = "Enter Filename: ", font = 'arial 10', 
    bg='gray7', fg='lime green')
L1.place(x=50, y=55)

L2 = Label(root, text = "Output: ", font = 'arial 14 bold', 
    bg='gray7', fg='lime green')
L2.place(x=50, y=120)

L3 = Label(root, text = "Enter File Path: ", font = 'arial 10', 
    bg='gray7', fg='lime green')
L3.place(x=50, y=5)

L4 = Label(root, text = "Enter Search Criteria:", 
    font = 'arial 12', bg='gray7', fg='lime green')
L4.place(x=400, y=55)

L5 = Label(root, text = "Enter columns to be RETURNED, separated by spaces: ", 
    font = 'arial 10', bg='gray7', fg='lime green')
L5.place(x=400, y=5)

L6 = Label(root, text = "Enter file path for printing output:", 
    font = 'arial 10', bg='gray7', fg='lime green')
L6.place(x=350, y=760)

L7 = Label(root, text = "Enter file name for printing output:", 
    font = 'arial 10', bg='gray7', fg='lime green')
L7.place(x=350, y=800)


# Create tkinter text output widget
T1 = Text(root, height=35, width=85, borderwidth=1, relief='ridge', bg='gray7', 
    fg='lime green')
T1.place(x=50, y=150)

# Create Scrollbar for text widget
S1 = Scrollbar(root)
S1.place(x=750, y=400)


# Configure commands for scrollbar and tie to text widget
T1.config(yscrollcommand=S1.set)
S1.config(command=T1.yview, bg='gray7', activebackground='lime green', 
    highlightcolor='lime green', width=15)

# Create Entry Boxes
# Entry box for filename 
E1 = Entry(root, font = 'arial 10', width=25, bg='gray7', fg='lime green')
E1.place(x=50, y=80)
# Entry box for file path
E2 = Entry(root, font = 'arial 10', width=25, bg='gray7', fg='lime green')
E2.place(x=50, y=30)
# Entry box for search criteria
E3 = Entry(root, font = 'arial 10', width=50, bg='gray7', fg='lime green')
E3.place(x=400, y=80)
# Entry box for columns to be searched
E4 = Entry(root, font = 'arial 10', width=50, bg='gray7', fg='lime green')
E4.place(x=400, y=30)
# Entry box for output file path
E5 = Entry(root, font = 'arial 10', width=40, bg='gray7', fg='lime green')
E5.place(x=350, y=780)
# Entry box for output file name
E6 = Entry(root, font = 'arial 10', width=40, bg='gray7', fg='lime green')
E6.place(x=350, y=820)


# Create Buttons
B1 = Button(root, font = 'arial 10', text = 'Get File', 
    command = get_file_name, bg='gray7', fg='lime green')
B1.place(x=50, y=760)

B2 = Button(root, font = 'arial 10', text = 'Get File Encoding', 
    command = get_encoding, bg='gray7', fg='lime green')
B2.place(x=50, y=800)

B3 = Button(root, font = 'arial 10', text = 'Get File Headers', 
    command = print_headers, bg='gray7', fg='lime green')
B3.place(x=50, y=840)

B4 = Button(root, font = 'arial 8', text = 'Clear File Path', 
    command = clear_filep, bg='gray7', fg='lime green')
B4.place(x=260, y=27)

B9 = Button(root, font = 'arial 8', text = 'Clear File Name', 
    command = clear_filen, bg='gray7', fg='lime green')
B9.place(x=260, y=77)

B10 = Button(root, font = 'arial 8', text = 'Clear Output', 
    command = clear_output, bg='gray7', fg='lime green')
B10.place(x=150, y=117)

B11 = Button(root, font = 'arial 8', text = 'Clear Search', 
    command = clear_search, bg='gray7', fg='lime green')
B11.place(x=600, y=117)

B5 = Button(root, font = 'arial 10', text = 'SEARCH', 
    command = search_csv, bg='lime green', fg='gray7')
B5.place(x=400, y=117)

B7 = Button(root, font = 'arial 10 bold', text = 'EXIT', width=6, 
    command = Exit, bg = 'OrangeRed', padx=2, pady=1)
B7.place(x=725, y=850)

B8 = Button(root, font = 'arial 10', text = 'Print', 
    command = text_print, bg='royal blue', fg='lime green')
B8.place(x=650, y=795)

B12 = Button(root, font = 'arial 8', text = 'Clear Columns', 
    command = clear_columns, bg='gray7', fg='lime green')
B12.place(x=600, y=52)

B13 = Button(root, font = 'arial 10', text = 'Read File', 
    command = read_file, bg='lime green', fg='gray7')
B13.place(x=220, y=760)

B14 = Button(root, font = 'arial 10', text = 'Read 5 Rows', 
    command = read_part, bg='lime green', fg='gray7')
B14.place(x=220, y=800)

B15 = Button(root, font = 'arial 10', text = 'Read Columns', 
    command = whole_column, bg='lime green', fg='gray7')
B15.place(x=220, y=840)

root.mainloop()
