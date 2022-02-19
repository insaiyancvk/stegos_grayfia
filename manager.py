import csv
import pyminizip
import os, sys, pdb, msvcrt
import time
from utils import check_jpg, get_input, if_data, png_to_jpg, write_enc_data, read_enc_data, rem_data, clear_screen, Picker
from ui_utils import get_image_popup, pass_inp, yn_prompt, print_table, pick, get_path_popup, get_csv_popup
from rich.align import Align
from rich.console import Console
from rich.panel import Panel
from halo import Halo

## install all deez packages automatically using subprocess.call

def access_data(image):

    data_dict = {}
    outp = pass_inp('Enter your key: ', 'key')
    key = outp['key']

    with Halo(text = 'Reading the data from image', text_color='cyan', color='green', spinner='dots') as spinner:
        # print('\nReading the data from image')
        spinner.start()
        time.sleep(2)
        
        data_dict = read_enc_data(image, key) # read the data from image with the key
        
        spinner.text = 'Decrypting the data'
        spinner.color = 'magenta'
        spinner.text_color = 'green'
        time.sleep(2)
        
        if data_dict == -1: # Exit if the padding doesn't match
            spinner.stop_and_persist(text='Wrong key :(')
            sys.exit()
        
        spinner.stop_and_persist(text='Successfully decrypted data from image')
        time.sleep(0.5)
    
    # pdb.set_trace()

    options = ['Check the existing data','Update data','Delete data', 'Export data', 'Import data']
    
    op = pick(options)

    if op == 0:
        
        rows = []

        for k, value in data_dict.items():
            rows.append(['\n'+k, '\n'+value[0], '\n****'+value[1][-2:]])

        # pdb.set_trace()
        print_table(['Service','Handle','Password'],rows)
        del rows
        
        inp =  yn_prompt("Would you like to check the password to a particular service ? ",'inp')
        if inp['inp']:
            ser = input('Enter the service name: ')
            for k, value in data_dict.items():
                if k.lower() == ser.lower():
                    print_table(
                        ['Service','Handle','Password'],
                        [['\n'+k, '\n'+value[0], '\n'+value[1]]]
                    )
                    break

        input('\n\n\tPress enter to exit')
        # _ = msvcrt.getch()
        clear_screen()

        return
    
    elif op == 1:
        
        sers = pick(['Add new entries']+list(data_dict.keys()))
        # pdb.set_trace()
        
        if sers == 0:
            rows = []
            new_entries = get_input()
            data_dict.update(new_entries)
            
            for k, value in data_dict.items():
                rows.append(['\n'+k, '\n'+value[0], '\n****'+value[1][-2:]])
            clear_screen()
            print('Here\'s the updated data\n')
            
            print_table(
                ['Service','Handle','Password'],
                rows)

        else:
        
            ser = list(data_dict.keys())[sers-1]

            handle = input(f"Enter the handle of {ser}: ")
            outp = pass_inp(f'Enter the password of your {ser}: ', 'passw')
            passw = outp['passw']
            # passw = outp['passw']
            data_dict[ser] = [handle, passw]
            
            clear_screen()
            
            print('Here\'s the updated data\n')
            print_table(
                ['Service','Handle','Password'], 
                [['\n'+ser, '\n'+handle, '\n****'+passw[-2:]]]
            )

        with Halo(text='Removing the existing data from image', text_color = 'red', color = 'cyan', spinner = 'dots') as spinner:
            
            spinner.start()
            
            rem_data(image)
            time.sleep(2)
            spinner.text_color = 'green'
            spinner.text = 'Existing data removed from the image'
            time.sleep(0.5)

            spinner.text_color = 'red'
            spinner.text = 'Writing the updated data to image'
            write_enc_data(image, data_dict, key)
            time.sleep(2)

            spinner.text_color = 'green'
            spinner.text = 'Updated data written successfully'
            spinner.stop_and_persist()

        input('\n\n\t Press enter to exit')
        # _ = msvcrt.getch()
        clear_screen()
        
        return

    elif op == 2:

        sers = pick(list(data_dict.keys()))

        ser = list(data_dict.keys())[sers]

        for k, value in data_dict.items():
            if k.lower() == ser:
                print("The following is going to be deleted\n")

                print_table(
                    ['Service','Handle','Password'],
                    [['\n'+k, '\n'+value[0], '\n****'+value[1][-2:]]]
                )

                conf = yn_prompt("Are you sure you want to delete it ? ",'conf')
                if conf['conf']:
                    del data_dict[ser]

                    with Halo(text='Removing the existing data from image', text_color = 'red', color = 'cyan', spinner = 'dots') as spinner:
            
                        spinner.start()
                        
                        rem_data(image)
                        time.sleep(2)
                        spinner.text_color = 'green'
                        spinner.text = 'Existing data removed from the image'
                        time.sleep(0.5)

                        spinner.text_color = 'red'
                        spinner.text = 'Writing the updated data to image'
                        write_enc_data(image, data_dict, key)
                        time.sleep(2)

                        spinner.text_color = 'green'
                        spinner.text = 'Updated data written successfully'
                        spinner.stop_and_persist()
                    
                    chk = yn_prompt('Would you like to check the updated data ?','chk')
                    if chk['chk']:

                        rows = []

                        for k, value in data_dict.items():
                            rows.append(['\n'+k, '\n'+value[0], '\n****'+value[1][-2:]])
                        
                        print_table(['Service','Handle','Password'],rows)
                        del rows
                
                input('Press enter to exit')
                clear_screen()
                return
        print(f'No such service found\nexiting')
        return
    
    # OP 3 to export data in key protected csv as a zip file (https://www.geeksforgeeks.org/create-password-protected-zip-of-a-file-using-python/)
    elif op == 3:  # export data as csv and put it in password protected zip file
        pdb.set_trace()

        export = []
        csv_path = 'temp.csv'
        sel_path = get_path_popup()
        zip_path = sel_path +'/'+'passwords.zip'

        with Halo(text='Exporting the image data', text_color = 'red', color = 'cyan', spinner = 'dots') as spinner:

            spinner.start()
            time.sleep(1.5)

            export.append(['Service','Handle','Password'])
            for serv, value in data_dict.items():
                export.append([serv, *value])
            spinner.text_color = 'green'
            spinner.text = 'Data exported'
            
            time.sleep(1.5)

            spinner.text_color = 'red'
            spinner.text = 'Exporting a temporary CSV file'
            
            with open(csv_path, 'w', newline='') as f:
                writer = csv.writer(f, delimiter=',')
                writer.writerows(export)

            time.sleep(1.5)

            spinner.text = 'Creating a password protected zip file'
            
            pyminizip.compress(csv_path, None, zip_path, key, 5)

            spinner.text_color = 'green'
            spinner.text = 'Password protected zip file exported successfully'
            spinner.stop_and_persist()

            os.remove(csv_path)

            print(f'\n\nThe zip file is protected with the same password as you used for the image')
            print(f'The zip file is located at: {sel_path}')
            
            ans = yn_prompt('Would you like to see the key ', 'key')

            if ans['key']:
                print(f'Key to the password protected zip is: {key}')

    
    elif op == 4: # import csv 
        
        Console().rule(
            "\n[bold]Note that the CSV file must be an exported password file from a browser [bold]", 
            style="black", 
            align="center")
        
        pass_csv = get_csv_popup()
        
        new_data = []

        with Halo(text='Reading the passwords CSV file', text_color = 'red', color = 'cyan', spinner = 'dots') as spinner:
            spinner.start()

            with open(pass_csv, 'r') as f:
                csvreader = csv.reader(f)
                next(csvreader)
                new_data = [[i[0],i[2],i[3]] for i in csvreader]
            
            spinner.text_color = 'green'
            spinner.text = 'Password data from the CSV file is imported'

            spinner.text_color = 'red'
            spinner.text = 'Updating the new data with existing data'

            new_dict = {}
            for i in new_data:
                new_dict[i[0]] = [i[1],i[2]]
            data_dict.update(new_dict)

            spinner.text_color = 'green'
            spinner.text = 'New data added along with existing data'
            
            pdb.set_trace()

            spinner.text_color = 'red'
            spinner.text = 'Removing the existing data from image'

            rem_data(image)
            time.sleep(2)
            spinner.text_color = 'green'
            spinner.text = 'Existing data removed from the image'
            time.sleep(0.5)

            spinner.text_color = 'red'
            spinner.text = 'Writing the updated data to image'
            write_enc_data(image, data_dict, key)
            time.sleep(2)

            spinner.text_color = 'green'
            spinner.text = 'Updated data written successfully'

            spinner.stop_and_persist()






def main():
    clear_screen()
    image = ''
    
    with Console().screen(style='bold white on black') as screen:
        text = Align.center('Press any key to select the image', vertical='middle')
        screen.update(Panel(text))
        _ = msvcrt.getch()

    image = get_image_popup()

    if os.path.splitext(image)[1].lower() == '.png':
            
            image = png_to_jpg(image)
    
    if image == '':
        print('No image was selected. Exiting.')
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
                
                with Halo(text = 'Embedding the data to image', text_color='cyan', color='green', spinner='dots') as spinner:
                    spinner.start()
                
                    write_enc_data(image, data_dict, key) # pass the dictionary, key to the function
                    time.sleep(2)
                
                    spinner.text = f"The encrypted data is written to {image} :)"
                    spinner.text_color = 'magenta'
                    spinner.stop_and_persist()
            
            else:
                print("\nSee you later!")

    elif not check_jpg(image):
        print("The image not in JPG format :(")
    

    #TODO: Complete dictionary part and fill some sample encrypted data and test the decryption ✅
    #TODO: Take a "proper" dictionary input. ✅
    #TODO: Take dictionary inputs and write/read to/from image ✅
    #TODO: Implement Create, Read, Update, Delete feature ✅

main()