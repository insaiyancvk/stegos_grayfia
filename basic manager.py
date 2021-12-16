import getpass
from utils import check_jpg, get_input, write_enc_data, read_enc_data

if __name__ == '__main__':

    image = input('Enter the image path: ')
    data_dict = {}

    if check_jpg(image): # check if the input image has FFD9 in it

        ch = input('First time here? (y/n): ')
        ch = ch.lower()
        if ch == 'y':
            key = input('Create a key (NEVER FORGET IT): ')
            ch1 = input('Would you like to add your data? (y/n): ')
            if ch1.lower() == 'y':
                data_dict = get_input() # get the service, handle, password dictionary
                write_enc_data(image, data_dict, key) # pass the dictionary, key to the function
                print(f"The encrypted data is written to {image} :)")
        else:
            key = getpass.getpass('Enter your key: ') # read the password with echo off
            print('Reading the data from image')
            data_dict = read_enc_data(image, key) # read the data from image with the key
            if data_dict == -1: # Exit if the padding doesn't match
                print('Wrong key :(')
                exit()
            else:
                print('Data decrypted successfully :)')
                for key, value in data_dict.items():
                    print(key, value)

    elif not check_jpg(image):
        print("The image not in JPG format :(")
    

    #TODO: Complete dictionary part and fill some sample encrypted data and test the decryption ✅
    #TODO: Take a "proper" dictionary input. ✅
    #TODO: Take dictionary inputs and write/read to/from image ✅
    #TODO: Implement Create, Read, Update, Delete feature