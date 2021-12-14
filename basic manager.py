import base64, getpass
from os import write
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random

def encrypt(key, source, encode=True):
    key = key.encode('utf-8')
    source = source.encode('utf-8')
    key = SHA256.new(key).digest()
    IV = Random.new().read(AES.block_size)
    encryptor = AES.new(key, AES.MODE_CBC, IV)
    padding = AES.block_size - len(source) % AES.block_size
    source += bytes([padding]) * padding
    data = IV + encryptor.encrypt(source)
    return base64.b64encode(data).decode("latin-1") if encode else data

def decrypt(key, source, decode=True):
    key = key.encode('utf-8')
    if decode:
        source = base64.b64decode(source.encode("latin-1"))
    key = SHA256.new(key).digest()
    IV = source[:AES.block_size]
    decryptor = AES.new(key, AES.MODE_CBC, IV)
    data = decryptor.decrypt(source[AES.block_size:])
    padding = data[-1]
    if data[-padding:] != bytes([padding]) * padding:
        print('Wrong key :(')
        return -1
    return data[:-padding].decode('utf-8') 

def write_enc_data(img_path, data, key):
    
    str_data = str(data)
    enc_data = encrypt(key, str_data)
    
    with open(img_path,'ab') as f:
        print('writing the encrypted data to image')
        f.write(enc_data.encode('utf-8'))

def read_enc_data(img_path, key):

    get_data = ''
    with open(img_path,'rb') as f:
        content = f.read()
        offset = content.index(bytes.fromhex('FFD9'))
        f.seek(offset+2)
        get_data = f.read().decode('utf-8')
    dec_data = eval(decrypt(key, get_data))
    if dec_data == -1:
        return -1
    return dec_data

def check_jpg(name):

    with open(name,'rb') as f:
        content = f.read()
    if bytes.fromhex('FFD9') in content:
        return True
    else:
        return False

def get_input():

    data_dict = {}
    
    print('\n\tJust hit enter when done with all the inputs\n\tAlso, don\'t worry about the password, it\'s hidden:)\n')
    print('Give your inputs ')

    while True:

        service = ''
        handle = ''
        passw = ''
        
        service = input('Enter name of the service (eg: Gmail, Facebook, etc): ')
        if service=='':
            break
        
        handle = input(f'Enter the username/handle of your {service}: ')
        if handle=='':
            break
        
        passw = getpass.getpass(f'Enter the password of your {service}: ')
        if passw=='':
            break
        
        print()
        data_dict[service] = [handle, passw]
    
    return data_dict

def rem_data(img):

    with open(img,'rb') as f:
        content = f.read()
        position = content.index(bytes.fromhex('FFD9'))+2
        
    with open(img, 'r+') as f:
        f.seek(position)
        f.truncate()

if __name__ == '__main__':

    image = input('Enter the image path: ')
    data_dict = {}
    if check_jpg(image):

        ch = input('First time here? (y/n): ')
        ch = ch.lower()
        if ch == 'y':
            key = input('Create a key (NEVER FORGET IT): ')
            ch1 = input('Would you like to add your data? (y/n): ')
            if ch1.lower() == 'y':
                data_dict = get_input()
                write_enc_data(image, data_dict, key)
                print(f"The encrypted data is written to {image} :)")
        else:
            key = getpass.getpass('Enter your key: ')
            print('Reading the data from image')
            data_dict = read_enc_data(image, key)
            if data_dict == -1:
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
    #TODO: Take dictionary inputs and write/read to/from image