# from __future__ import print_function
# import sys
from PyInquirer import prompt
import tkinter as tk
from tkinter import filedialog

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
    root.withdraw() # close the pop up created by tkinter

    file_path = filedialog.askopenfilename(multiple=False, filetypes= [('Image Files', ('*.jpg', '*.png'))]) # select images in jpg and png format
    
    return file_path



#########  INPUT FROM ONLY BOTTOM OF THE TERMINAL  ##################

# from time import sleep

# if sys.version_info > (3,):
#     # Get the (current) number of lines in the terminal
#     import shutil
#     height = shutil.get_terminal_size().lines - 1

#     stdout_write_bytes = sys.stdout.buffer.write
# else:
#     height = 40
#     input = raw_input
#     stdout_write_bytes = sys.stdout.write


# # Some ANSI/VT100 Terminal Control Escape Sequences
# CSI = b'\x1b['
# CLEAR = CSI + b'2J'
# CLEAR_LINE = CSI + b'2K'
# SAVE_CURSOR = CSI + b's'
# UNSAVE_CURSOR = CSI + b'u'

# GOTO_INPUT = CSI + b'%d;0H' % (height + 1)

# def emit(*args):
#     stdout_write_bytes(b''.join(args))

# def set_scroll(n):
#     return CSI + b'0;%dr' % n

# emit(CLEAR, set_scroll(height))

# try:
#     while True:
#         #Get input
#         emit(SAVE_CURSOR, GOTO_INPUT, CLEAR_LINE)
#         try:
#             n = int(input('Number: '))
#         except ValueError:
#             continue
#         finally:
#             emit(UNSAVE_CURSOR)

#         #Display some output
#         for i in range(n):
#             print(i)
#             sleep(0.1)

# except KeyboardInterrupt:
#     #Disable scrolling, but leave cursor below the input row
#     emit(set_scroll(0), GOTO_INPUT, b'\n')