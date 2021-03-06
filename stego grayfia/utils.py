import base64, sys, os, time
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
from ui_utils import pass_inp
from PIL import Image
from halo import Halo

def png_to_jpg(image):  

    with Image.open(image) as im:

        with Halo(text = 'Converting the image from PNG to JPEG', text_color = 'cyan', color='green', spinner='dots') as spinner:
            spinner.start()
            # import pdb; pdb.set_trace()
            base,_ = os.path.split(image)
            img_name, _ = os.path.splitext(os.path.basename(image))
            im.save(f'{base}/{img_name}.jpg',"JPEG")
            
            time.sleep(2)
            spinner.stop_and_persist(text = f'"{image}" saved as "{img_name}.jpg"!')
        
    print('The data will now be stored in the JPG image.')

    return f'{base}/{img_name}.jpg'

def encrypt(key, source, encode=True): # Encrypt the str(dictionary) with a key and return utf-8 decoded string
    key = key.encode('utf-8') # encode the key to utf-8 (as bytes)
    source = source.encode('utf-8') # encode the string to utf-8 (as bytes)
    
    # STACKOVERFLOW STUFF
    key = SHA256.new(key).digest()
    IV = Random.new().read(AES.block_size)
    encryptor = AES.new(key, AES.MODE_CBC, IV)
    padding = AES.block_size - len(source) % AES.block_size
    source += bytes([padding]) * padding
    data = IV + encryptor.encrypt(source)
    return base64.b64encode(data).decode("latin-1") if encode else data

def decrypt(key, source, decode=True): # Decrypt the encrypted string data and return utf-8 decoded string
    key = key.encode('utf-8') # encode the key to utf-8 (as bytes)

    # STACKOVERFLOW STUFF
    if decode:
        source = base64.b64decode(source.encode("latin-1"))
    key = SHA256.new(key).digest()
    IV = source[:AES.block_size]
    decryptor = AES.new(key, AES.MODE_CBC, IV)
    data = decryptor.decrypt(source[AES.block_size:])
    padding = data[-1]
    if data[-padding:] != bytes([padding]) * padding: # Check for the padding (idk what it is)
        return -1
    return data[:-padding].decode('utf-8') 

def write_enc_data(img_path, data, key):
    
    str_data = str(data) # Convert the dictionary to a string
    enc_data = encrypt(key, str_data) # encrypt str(dictionary)
    
    with open(img_path,'ab') as f: # open the file as append binary mode
        # print('writing the encrypted data to image')
        f.write(enc_data.encode('utf-8')) # append the encrypted data

def read_enc_data(img_path, key):

    get_data = ''
    with open(img_path,'rb') as f: # open the file as read binary mode
        content = f.read()
        offset = content.index(bytes.fromhex('FFD9')) # get the index of FFD9
        f.seek(offset+2) # seek till the offset
        get_data = f.read().decode('utf-8') # read the data after the offset position and decode
        
    dec_data = decrypt(key, get_data) # decrypt the data and convert str(dictionary) to dictionary
    if dec_data == -1: # Check if the key is correct
        return -1
    return eval(dec_data)

def check_jpg(name):

    with open(name,'rb') as f: # open the file as read binary mode
        content = f.read()
    if bytes.fromhex('FFD9') in content: # Check if FFD9 exists in the file
        return True
    else:
        return False

def if_data(image):
    data = ''
    with open(image, 'rb') as f:
        content = f.read()
        offset = content.index(bytes.fromhex('FFD9'))
        f.seek(offset+2)
        data = f.read().decode('utf-8')
        
    if data == '':
        return False
    return True

def get_input():

    data_dict = {}
    clear_screen()
    
    print('\n\tJust hit enter when done with all the inputs\n\tAlso, don\'t worry about the password, it\'s hidden:)\n')
    print('Give your inputs ')

    while True:

        service = ''
        handle = ''
        passw = ''
        
        service = input('Enter name of the service (eg: Gmail, Facebook, instagram, etc): ')
        service = service.lower()
        if service=='':
            break
        
        handle = input(f'Enter the username/handle of your {service}: ')
        if handle=='':
            break
        
        # passw = getpass.getpass()
        outp = pass_inp(f'Enter the password of your {service}: ', 'passw')
        passw = outp['passw']
        if passw=='':
            break
        
        print()
        data_dict[service] = [handle, passw]
    
    return data_dict

def rem_data(img):

    with open(img,'rb') as f: # open the file as read binary mode
        content = f.read() 
        position = content.index(bytes.fromhex('FFD9'))+2 # Get the position of FFD9
        
    with open(img, 'r+') as f: # open the file as read update mode
        f.seek(position) # seek to FFD9 position
        f.truncate() # clear the data after FFD9

def clear_screen():
    if sys.platform=='win32' or os.name=='nt':
        os.system("cls")
    elif sys.platform=='linux' or os.name=='posix':
        os.system("clear")

