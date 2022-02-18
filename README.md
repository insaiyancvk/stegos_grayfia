# Image Steganography for passwords
Like the name of the repository suggests it's a password manager but it is not as simple as it sounds.

What makes this password manager _not-so-simple_
- The passwords are encrypted and stored in an **image** :)
- So all you need to have is the image and the decoding script to check your passwords :)

## ⚠️PROJECT UNDER CONSTRUCTION⚠️

Setup:

1. Clone the repository

    ```
    git clone https://github.com/insaiyancvk/password-manager
    ```

2. Change the directory

    ```
    cd password-manager
    ```

3. Create a virtual env to keep your main python env clean and activate it (optional) (the following was tested on windows)

    ```
    python -m venv env
    env\Scripts\activate
    ```

3. Install the dependencies

    ```
    pip install -r requirements.txt
    ```

4. Run the code

    ```
    python manager.py
    ```

5. To deactivate the env

    ```
    env\Scripts\deactivate.bat
    ```

6. To update code locally

    - Change the directory to password-manager
    - `git pull`