import getpass, sys, os
from utils import check_jpg, get_input, if_data, write_enc_data, read_enc_data, rem_data, Picker
from rich.console import Console
# from rich.columns import Columns
from rich.table import Table
# from rich.panel import Panel

def clear_screen():
    if sys.platform=='win32' or os.name=='nt':
        os.system("cls")
    elif sys.platform=='linux' or os.name=='posix':
        os.system("clear")


def access_data(image):
    data_dict = {}
    c = Console()
    key = getpass.getpass('Enter your key: ') # read the password with echo off
    print('Reading the data from image')

    try:
        data_dict = read_enc_data(image, key) # read the data from image with the key
    except:
        pass

    if data_dict == -1: # Exit if the padding doesn't match
        print('Wrong key :(')
        return

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

            inp = input("Would you like to check the password to a particular service? (y/n): ")
            if inp.lower() == 'y':
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
            passw = getpass.getpass(f'Enter the password of {ser}: ')

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
                    conf = input("Are you sure you want to delete it (y/n): ")
                    if conf.lower() == 'y':
                        del data_dict[ser]
                        rem_data(image)
                        write_enc_data(image, data_dict, key)
                        chk = input("Would you like to check the updated data (y/n): ")
                        if chk.lower() == 'y':
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

def main():

    image = input('Enter the image path: ')
    data_dict = {}

    if check_jpg(image): # check if the input image has FFD9 in it

        if if_data(image):
            access_data(image)

        else: 

            key = input('Create a key (NEVER FORGET IT): ')
            ch1 = input('Would you like to add your data? (y/n): ')

            if ch1.lower() == 'y':

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