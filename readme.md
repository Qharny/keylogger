## Keylogger using Pynput Module
 This Python script uses the pynput module to create a keylogger.

## Description
  A keylogger is a computer program that records every keystroke made by a computer user, especially in order to gain fraudulent access to passwords and other confidential information. This script records all the keystrokes and writes them into a file named *log.txt.*

## How it works
 The script first imports the necessary modules and initializes an empty list to store the keystrokes.

 ++ It defines three functions:

    on_press(key): This function is triggered whenever a key is pressed. It appends the key to the list and calls the write_file(keys) function.
    write_file(keys): This function writes all the keys in the list to the log.txt file.
    on_release(key): This function is triggered whenever a key is released. It prints which key was released and stops the listener if the ‘esc’ key is pressed.
    The script then starts a listener that listens for key press and release events. When such an event occurs, it calls the corresponding function.

## Usage
 To use this script, simply run it in your Python environment. Make sure you have the pynput module installed.

*Note*: This script is for educational purposes only. Misuse of this script can lead to violation of privacy rights, and legal action could be taken against you by individuals, or companies.

- Dependencies
- Python
- Pynput module
- License
- This project is licensed under the MIT License.

*Please remember that this code should be used responsibly and ethically.*