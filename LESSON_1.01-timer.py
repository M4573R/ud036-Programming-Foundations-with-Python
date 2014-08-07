# *********************************
# TIMER 
# *********************************

import webbrowser # timer
import time # timer

print ("This program started on " + time.ctime())
def timer(n):
    i = 0
    while i < n:
        time.sleep(2)
        webbrowser.open("https://www.youtube.com/watch?v=S7J7XX0exDY")
        i += 1
timer(3)