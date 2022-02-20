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

https://raw.githubusercontent.com/insaiyancvk/stegos_grayfia/main/assets/installer.mp4

### Export data

https://raw.githubusercontent.com/insaiyancvk/stegos_grayfia/main/assets/export%20data.mp4

### Import data

https://raw.githubusercontent.com/insaiyancvk/stegos_grayfia/main/assets/import%20data.mp4

### Check data

https://raw.githubusercontent.com/insaiyancvk/stegos_grayfia/main/assets/check%20data.mp4

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