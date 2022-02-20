from PyInquirer.prompt import prompt
import tkinter as tk
from tkinter import filedialog
from rich.console import Console
from rich.table import Table
from rich import box
from picker import Picker
from rich.align import Align

import sys


def yn_prompt(message, name):

    resp = prompt(
            {
                'type': 'confirm',
                'message': message,
                'name': name,
                'default': True,
            }
        )
    return resp

def pass_inp(message, name):
    
    return prompt(
        {
        'type': 'password',
        'message': message,
        'name': name
        }
    )

def get_image_popup():

    root = tk.Tk() # create a tkinter object
    root.attributes('-topmost',1)
    root.withdraw() # close the pop up created by tkinter

    file_path = filedialog.askopenfilename(
        title = 'Select an image',
        multiple=False, 
        filetypes= [
            ('Image Files', ('*.jpg', '*.png'))
            ]) # select images in jpg and png format
    
    return file_path

def get_csv_popup():

    root = tk.Tk() # create a tkinter object
    root.attributes('-topmost',1)
    root.withdraw() # close the pop up created by tkinter

    file_path = filedialog.askopenfilename(
        title = 'Select the CSV file',
        multiple=False, 
        filetypes= [
            ('CSV', ('*.csv'))
            ]) # select images in jpg and png format
    
    return file_path

def get_path_popup():

    root = tk.Tk() # create a tkinter object
    root.attributes('-topmost',1)
    root.withdraw() # close the pop up created by tkinter

    file_path = filedialog.askdirectory(
        title = 'Select the directory') # select a directory
    
    return file_path

def print_table(headings, rows):

    table = Table(header_style='bold cyan')
    
    for i in headings:
        table.add_column(i)
    
    for i in rows:
        table.add_row(*i)
    
    table.box = box.MINIMAL
    table = Align.left(table)
    
    Console().print(table)

def pick(options):

    picker1 = Picker(
        options, 
        "Select your choice using arrow keys or press q to quit", 
        indicator=" => "
        )
    picker1.register_custom_handler(ord('q'), lambda picker1: exit())
    picker1.register_custom_handler(ord('Q'), lambda picker1: exit())
    _,sers = picker1.start()

    return sers