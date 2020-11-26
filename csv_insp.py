#! /usr/bin/env python3

import pandas as pd
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
    new_file = str('csv_results.txt')
     
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
    
    search_get = E3.get()
    search_term = search_get.upper()
    
    try:
        with open(filename, 'r', encoding=fencode, errors='ignore',
            newline='') as f:
            
            reader = csv.reader(f)
            
            included_cols = [0, 1, 2, 8, 11, 12, 15, 16, 17]
            
            for row in reader:
                if search_term in row:
                    content = list(row[i] for i in included_cols)
                    T1.insert(END, content)
                    T1.insert(END, '\n')
           
                
    except Exception as err:
        T1.insert(END, '\n' + str(err))
        T1.insert(END, '\nSearch Criteria Not Found ...')
    

def clear_output():
    T1.delete(1.0, END)
    

def clear_filep():
    E2.delete(0, 'end')


def clear_filen():
    E1.delete(0, 'end')


def clear_search():
    E3.delete(0, 'end')


def Exit():
    exit()


# Create tkinter Labels
L1 = Label(root, text = "Enter Filename: ", font = 'arial 13 bold', 
    bg='gray7', fg='lime green')
L1.place(x=50, y=55)

L2 = Label(root, text = "Output: ", font = 'arial 14 bold', 
    bg='gray7', fg='lime green')
L2.place(x=50, y=120)

L3 = Label(root, text = "Enter File Path: ", font = 'arial 13 bold', 
    bg='gray7', fg='lime green')
L3.place(x=50, y=5)

L4 = Label(root, text = "Search: Enter name, ZIP, County or City", 
    font = 'arial 13 bold', bg='gray7', fg='lime green')
L4.place(x=300, y=55)


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
E3.place(x=300, y=80)


# Create Buttons
B1 = Button(root, font = 'arial 10 bold', text = 'Get File', 
    command = get_file_name, bg='gray7', fg='lime green')
B1.place(x=50, y=760)

B2 = Button(root, font = 'arial 10 bold', text = 'Get File Encoding', 
    command = get_encoding, bg='gray7', fg='lime green')
B2.place(x=50, y=800)

B3 = Button(root, font = 'arial 10 bold', text = 'Get File Headers', 
    command = print_headers, bg='gray7', fg='lime green')
B3.place(x=50, y=840)

B4 = Button(root, font = 'arial 10 bold', text = 'Clear File Path', 
    command = clear_filep, bg='gray7', fg='lime green')
B4.place(x=250, y=760)

B9 = Button(root, font = 'arial 10 bold', text = 'Clear File Name', 
    command = clear_filen, bg='gray7', fg='lime green')
B9.place(x=250, y=800)

B10 = Button(root, font = 'arial 10 bold', text = 'Clear Output', 
    command = clear_output, bg='gray7', fg='lime green')
B10.place(x=250, y=840)

B11 = Button(root, font = 'arial 10 bold', text = 'Clear Search', 
    command = clear_search, bg='gray7', fg='lime green')
B11.place(x=500, y=110)

B5 = Button(root, font = 'arial 10 bold', text = 'SEARCH', 
    command = search_csv, bg='gray7', fg='lime green')
B5.place(x=300, y=110)

B7 = Button(root, font = 'arial 10 bold', text = 'EXIT', width=6, 
    command = Exit, bg = 'OrangeRed', padx=2, pady=1)
B7.place(x=725, y=850)

B8 = Button(root, font = 'arial 10 bold', text = 'Print', 
    command = text_print, bg='gray7', fg='lime green')
B8.place(x=625, y=850)

root.mainloop()
