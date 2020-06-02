#Assignment: Program to play the sound file and display the message on a given input time
#A method with 3 arguments: time, sound file, message

# Key Learnings:
  # How to use a sound file
  # 

import time as t
import playsound as ps

def setAlarm(inputTime,soundFile,message):
    t.sleep(inputTime-t.time())
    print(message)
    ps.playsound("./../Input Files/sound.wav")
    

def main():
    time = t.time() + 1
    soundFile = "alarm.wav"
    message = "Time to get up you lazy bum!"
    
    
    setAlarm(time,soundFile,message)
    

if __name__ == "__main__":
    main()
