# Image Steganography for passwords

The word Steganography is derived from two Greek words- ‘stegos’ meaning ‘to cover’ and ‘grayfia’, meaning ‘writing’, thus translating to ‘covered writing’, or ‘hidden writing’.

Pretty sure y'all have seen some fancy password managers. 
Now get ready for another one of the fanciest one on the internet, _Stegos Grayfia_ (ik it sounds like a harry potter spell lol).


Features:
* Import passwords that are exported from browser.
* Export passwords to a protected zip file.
* Create/Read/Edit/Delete passwords from an image.
* Hella fancy installer 🚫🧢

### Installer

https://user-images.githubusercontent.com/53230977/154854140-8e8034b9-db16-474f-93e0-8e8c1d5ffdad.mp4

### Export data

https://user-images.githubusercontent.com/53230977/154854150-ace49990-04bc-41de-b3c8-5bdefa2e3a08.mp4

### Import data

https://user-images.githubusercontent.com/53230977/154854152-ca50b8c3-6c8e-46ff-9928-d90dc67c0427.mp4

### Check data

https://user-images.githubusercontent.com/53230977/154854166-ad2b2221-8de4-4a53-beab-349c021ebbb2.mp4


Setup (tested on windows only):

* Open cmd and nativate to desktop (recommended)
    ```
    cd Desktop
    ```
* Download the installer file and run it

    <details>

    <summary><b>Note</b></summary>

    **Read the instructions carefully**
    * Make sure Python is added to your Path.
        * You can check it by typing `py --version` in cmd.
        * Consider running this piece of code (in cmd) for installing python (if you don't have python installed): 
        ```
        curl -o python.exe https://www.python.org/ftp/python/3.9.5/python-3.9.5-amd64.exe && python.exe
        ```
        **make sure to check "add to PATH"**
    * Make sure PIP is added to your Path.
        * You can check it by typing `pip --version` or `py -m pip --version` in cmd.
        * Consider running this piece of code (in cmd) for installing pip (if you don't have PIP installed): 
        ```
        curl -o get-pip.py https://bootstrap.pypa.io/get-pip.py && py get-pip.py
        ```
    </details>

    ```
    curl -o installer.py https://raw.githubusercontent.com/insaiyancvk/stegos_grayfia/main/installer.py && py installer.py && del installer.py
    ```

* Once the installation is completed, change the directory to `Stegos Grayfia` and run the main file
    ```
    cd Stegos Grayfia
    py manager.py
    ```
