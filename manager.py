import os, sys, pdb
from utils import check_jpg, get_input, if_data, png_to_jpg, write_enc_data, read_enc_data, rem_data, clear_screen, Picker
from ui_utils import get_image_popup, pass_inp, yn_prompt
from rich.console import Console
# from rich.columns import Columns
from rich.table import Table
# from rich.panel import Panel

# add delay where required

def access_data(image):
    data_dict = {}
    c = Console()
    outp = pass_inp('Enter your key: ', 'key')
    key = outp['key']

    print('Reading the data from image')

    data_dict = read_enc_data(image, key) # read the data from image with the key

    # pdb.set_trace()

    if data_dict == -1: # Exit if the padding doesn't match
        print('Wrong key :(')
        sys.exit()

    else:
        print('\nData decrypted successfully.')

        options = ['Check the existing data','Update data','Delete data']
        picker = Picker(options, "Select your choice using the arrow keys or press q to quit", indicator= " => ")
        picker.register_custom_handler(ord('q'), lambda picker: exit())
        picker.register_custom_handler(ord('Q'), lambda picker: exit())
        _, op = picker.start()

        if op == 0:

            table = Table(header_style='bold cyan')
            table.add_column('Service')
            table.add_column('Handle')
            table.add_column('Password')
            for k, value in data_dict.items():
                table.add_row('\n'+k, '\n'+value[0], '\n****'+value[1][-2:])
            c.print(table)
            
            inp =  yn_prompt("Would you like to check the password to a particular service ? ",'inp')
            if inp['inp']:
                ser = input('Enter the service name: ')
                for k, value in data_dict.items():
                    if k.lower() == ser.lower():
                        table = Table(header_style='bold green')
                        table.add_column('Service')
                        table.add_column('Handle')
                        table.add_column('Password')
                        table.add_row('\n'+k, '\n'+value[0], '\n'+value[1])
                        c.print(table)
                        break

            input('\n\n\tPress Enter to exit')
            clear_screen()
            
            return
        
        elif op == 1:
            
            ser = input("Enter the service that you want to update: ")
            ser = ser.lower()

            handle = input(f"Enter the handle of {ser}: ")
            # passw = getpass.getpass(f'Enter the password of {ser}: ')
            outp = pass_inp(f'Enter the password of your {ser}: ', 'passw')
            passw = outp['passw']
            passw = outp['passw']

            rem_data(image)
            data_dict[ser] = [handle, passw]
            write_enc_data(image, data_dict, key)

            print('Here\'s the updated data\n')
            table = Table(header_style='bold green')
            table.add_column('Service')
            table.add_column('Handle')
            table.add_column('Password')
            table.add_row('\n'+ser, '\n'+handle, '\n****'+passw[-2:])
            c.print(table)

            input('\n\n\t Press enter to exit')
            clear_screen()
            
            return

        elif op == 2:

            ser = input("Enter the service that you want to delete: ")
            ser = ser.lower()

            for k, value in data_dict.items():
                if k.lower() == ser:
                    print("The following is going to be deleted\n")
                    
                    table = Table(header_style='bold green')
                    table.add_column('Service')
                    table.add_column('Handle')
                    table.add_column('Password')
                    table.add_row('\n'+k, '\n'+value[0], '\n****'+value[1][-2:])
                    c.print(table)

                    conf = yn_prompt("Are you sure you want to delete it ? ",'conf')
                    if conf['conf']:
                        del data_dict[ser]
                        rem_data(image)
                        write_enc_data(image, data_dict, key)
                        
                        chk = yn_prompt('Would you like to check the updated data ?','chk')
                        if chk['chk']:
                            table1 = Table(header_style='bold green')
                            table1.add_column('Service')
                            table1.add_column('Handle')
                            table1.add_column('Password')

                            for k, value in data_dict.items():
                                table1.add_row('\n'+k, '\n'+value[0], '\n****'+value[1][-2:])
                            c.print(table1)
                    clear_screen()
                    return
            print(f'No such service found\nexiting')
            return
        # OP 3 to export data in key protected csv as a zip file (https://www.geeksforgeeks.org/create-password-protected-zip-of-a-file-using-python/)

def main():

    image = ''
    input('press enter to select the image')
    image = get_image_popup()

    if os.path.splitext(image)[1].lower() == '.png':
        print('Converting the image from PNG to JPEG')
        image = png_to_jpg(image)
    
    if image == '':
        exit() 

    data_dict = {}

    if check_jpg(image): # check if the input image has FFD9 in it

        if if_data(image):
            access_data(image)

        else: 

            key = input('Create a key (NEVER FORGET IT): ')
            ch1 = yn_prompt('Would you like to add your data ? ','ch1')

            if ch1['ch1']:

                data_dict = get_input() # get the service, handle, password dictionary
                write_enc_data(image, data_dict, key) # pass the dictionary, key to the function
                print(f"The encrypted data is written to {image} :)")
            
            else:
                print("\nSee you later!")

    elif not check_jpg(image):
        print("The image not in JPG format :(")
    

    #TODO: Complete dictionary part and fill some sample encrypted data and test the decryption ✅
    #TODO: Take a "proper" dictionary input. ✅
    #TODO: Take dictionary inputs and write/read to/from image ✅
    #TODO: Implement Create, Read, Update, Delete feature

main()