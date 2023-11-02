# function to print which key is being released and end Listener if ESC is pressed
def on_release(key):
    print('{0} released'.format(key))
    if key == Key.ESC:
        # Stop listener when ESC is pressed
        return False