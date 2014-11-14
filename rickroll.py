import webbrowser
import time

#This will "rick roll" someone every 2 hours 3 times
breaks = 0
print ("The program started on "+time.ctime())
while (breaks < 3):
    time.sleep(7200)
    webbrowser.open("http://bringvictory.com/")
    breaks = breaks + 1
    print breaks
