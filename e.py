def countdown(t):
    import time
    print('This window will remain open for 3 more seconds...')
    while t >= 0:
        print(t, end='...')
        time.sleep(1)
        t -= 1
    print('Goodbye!')

t=3
