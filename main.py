import time

def cd(t):

    while t:
        mins, secs = divmod(t, 60) # --> to calculate the number of minutes and secounds !!
        timer = '{:02d}:{:02d}'.format(mins, secs) # --> print the minutes and seconds on the screen using the variable timeformat.
        print(timer ,end="\r") # --> force the cursor to go back to the start of the screen (carriage return) so that the next line printed will overwrite the previous one
        time.sleep(1) # --> Code waits for one secound
        t -= 1 # --> Time decrease 

    print("Clock has run out!")


user_input = int(input('Enter the time in secounds: \n'))
cd(int(user_input))
