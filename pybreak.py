"""
    Program to initiate timely breaks when browsing/hacking
    Program can be modified to auto launch on boot by editing init file
"""
import webbrowser
import time

print "\nIts time to take some break!\n"

#Idle time in hours before break
time_breaks = raw_input("After how many hours would you like to take breaks?\n")
break_frequency = raw_input("How many breaks do you require?\n")

#Converting string to interger
tb = int(time_breaks)
bf = int(break_frequency)

choose_song = raw_input("Select Prefered Song:\nEnter trey for Trey Songs Body to Body Collabo or\n"
"Enter yemi for Yemi Alade and Nyashinski Mungu Pekee\n")

#convert choice to lower case
cs = choose_song.lower()

#define static part of Youtube URL
youtube = "https://www.youtube.com/watch?v="

#check and assign selected song.
if(choose_song == "yemi"):
    song = youtube + "lFJW2od5q84"

elif(choose_song == "trey"):
    song = youtube + "snDUXl_Wjto"
else:
    print "Poor choice!"

#defining break function to count break frequency
def breaking():
    breaks = 0

    while(breaks < bf):
        #Allow wait time chosen before opening video. Hours converted to seconds
        time.sleep(tb)

        #Open favorite music video: Mungu Pekee (Cover) by Yemi Alade. Original by Nyasinski
        webbrowser.open(song)
        breaks = breaks + 1
breaking()
