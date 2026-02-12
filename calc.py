import tkinter as tk
'''Imports Tkinter module tk is an alias for easy access'''

# Button click handler
def press(v):
    entry.insert(tk.END, v)
    '''called when a number or operator button is clicked 
    Inserts the pressed value at the end of the entry widget'''

def clear():
    entry.delete(0, tk.END)  # it deletes the data from o to end of the expression
    '''called when the clear button is clicked'''

def backspace():
    current_text = entry.get()  # retrieves the current text from the entry widget
    entry.delete(0, tk.END)  # clears the entry widget
    entry.insert(0, current_text[:-1])  # reinserts the text minus the last character
    '''called when backspace button is clicked removes last character from the entry widget'''

#Calculation function
def calc():
    try:
        result = eval(entry.get()) # entry.get() retrives  e.g (2+6) Eval() evalutes the string as a python expression
        entry.delete(0, tk.END) # clears the old expression
        entry.insert(0, result) # Displays exception instread of crashing

    except :
        entry.delete(0, tk.END)
        entry.insert(0, "inavalid input")
    ''' handles inavalid inputs dosplays exception instread of crashing'''

# Create main window
root = tk.Tk()  # creates the main application window

root.title("Calculator")  # sets the title of the window

root.configure(bg="#6E3915") # sets the background color of the window

root.resizable(False, False) # Disables resizing of the window

# Entry widget (display screen)
entry = tk.Entry(
    root,
    font=("times new roman", 24), 
    bg="#413508",
    fg="white",
    bd=5,
    justify="right"
)
'''Text input field acts as calculator display right-aligned for better calculator look'''
entry.grid(row=0, column=0, columnspan=4,padx=12, pady=12,ipady=10)

# Button Labels
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]
''' represents the labels of the buttons in a list'''
#Dyanamic button creation
row_val = 1
col_val = 0
''' Rows and column counter for grid layout'''
for b in buttons:
    cmd=calc if b=="=" else lambda x=b: press(x)
    '''if button is "=" , call cal() else, call press() with button value lambda x=b prevents late binding issues'''
    tk.Button(
        root,
        text=b,
        command=cmd, # these three lines creates a buttomn widget with the specified text and command
        font=("calibri", 21),
        width=6,
        height=2,
        bg="#948246" if b in "+-*/" else "#A38600",
        fg="white",
        bd=5).grid(row=row_val, column=col_val, padx=6, pady=6)
    col_val += 1
    ''' places the button in the grid at the current row and column'''
    if col_val == 4:
        row_val += 1
        col_val = 0
        ''' moves to the next row after every 4 buttons'''
    
    

#clear Button
tk.Button(
    root,
    text='clear',
    command=clear,
    font=("calibri", 21),
    width=22,
    height=2,
    bg="#8B4040",
    fg="white",
    bd=3).grid(row=row_val, column=0, columnspan=3, padx=6, pady=6)
'''clears the calculator display screen spans across all 4 columns '''
#Backspace Button
tk.Button(
    root,
    text='⌫',
    command=backspace,
    font=("calibri", 21),
    width=5,
    height=2,
    bg="#8B4040",
    fg="white",
    bd=3).grid(row=row_val, column=3, columnspan=1, padx=6, pady=6)
'''removes the last character from the calculator display screen spans across all 4 columns '''


#Event loop
root.mainloop()  # keeps the window running Listens for user interactions
'''keeps the application running and responsive to user input'''