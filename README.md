![Hellcode Logo](https://i.imgur.com/zm4ORbl.png)

## Features  
-  **Dynamic Payload Retrieval:** The script fetches a payload from a specified encoded URL during runtime.
- **Persistence Mechanisms:** It employs techniques to achieve persistence on the target system by copying itself to the AppData directory and adding a registry entry. 
-  **Stealth Techniques:** The script disguises itself by using randomized filenames and operates with a delay before execution. 

## Usage
**THIS IS MADE FOR WINDOWS**
```bash 
git clone https://github.com/Jumpy22/Hellcode 
cd Hellcode 
.\setup.bat (or install dependencies manually)
python loader.py
```

![Running Example (Uses the shellcode in this repository)](https://i.imgur.com/yuifhGW.gif)

## Execution Path
1. Checks %TEMP% for file with set beginning and end regex (beginRegex & endRegex be default)
2. If one is not found the following will happen
3. Find 10 random programs installed on the PC and choose 1
4. Make a file in %TEMP% with the following format "beginRegex(base64 encoded program name)endRegex"
5. Copy the program to %APPDATA% into a folder matching the name of the impersonated program
6. Write to the program path to ```Computer\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce```
7. Once the previous code completes OR a encoded file is found the following will happen
8. Sleep for 20-30 seconds
9. Decode the payload URL by converting the ORD to CHR
10. Fetch the payload from the supplied URL
11. Write the payload to memory and run it

## Improvements
 - Encode all function names
 - Add junk code
 - Anti-vm
 - Improved persistence/startup methods
 - Improve delay handling (before anything is executed)

### Encode
Simply used to easily convert a string to a list of ORD. Just swap line 1.

    python encode.py
