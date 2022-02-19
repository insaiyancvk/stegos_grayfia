This is a sort of _TODO_ kind of thing. And this is my notes.

1. Debug the wrong key thing ✅
2. Implement the dialog box to select the image ✅
    - Implement the same in pymusicdl to choose the download path
3. Ask if the user wants to check the services for deleting a service. 
4. Implement password field from PyInquirer. ✅
5. Improve the prompt messages UI using Rich and PyInquirer. ✅
7. Store the key in same directory as the code with a bunch of encryptions ❌
8. Add an option for the user to send the key and image to their E-mail ❌
9. use expand.py to show the image path 
10. use list.py to select inputs
11. Implement back button ❌
12. Try to get the summary of what happened in the entire session ❌
13. Use `jobs.py` or `live_progress.py` or `status.py` while decryption, encryption, updation, finding something ✅
14. Use `dynamic_progress.py` to install dependencies 
15. Use `screen.py` to print the message related to image input at the beginning of the program ✅
16. Use `table_movie.py` to print all services, handles and passwords ❌
17. 


Create a setup program that sets up everything while using rich to style the terminal and installation process

Prompt flow

_print a logo sort of thing with pyfiglet_

Enter to select the image
_print the image path_
print(checking if any data exists) # include sleep with rich
if data exists then
    print(Data found!)
    Ask for key
    print(decrypting the data) # include sleep with rich
    if decrypted
        print(data decrypted successfully)
        use boxes to show the inputs and pyinquirer to select the input
        after taking the input
        if the input is view the data
            print(reading the data) # include sleep with rich
            if they want to check the password to a specific thing
                use `input.py` (pyinquirer) to check if the entered input exists in the service list
        else if the input is to update data
            ask for 
                the service 
                    check if the service already exists. print (checking if it already exists)
                    if it exists then print it exists with a table
                    then ask for new handle and pass depending on it's existance in the DB
                or check existing services
                    print existing services in alphabetical order with rich
                    then ask for them to input the service name, handle, pass

                        IF THE SERVICE IS NEW
                            print (checking if it already exists)
                            print(new stuff)
                            and input the serv name, handle and pass
                            
                    

    if not decrypted
        print(wrong key, enter key again) # implement 3 attempts then exit the code

if data doesn't exist then
    print(data not found)
    ask to create a key
