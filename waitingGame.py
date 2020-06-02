# Record the time took between key hits
#Key things to learn: randomint(a,b) and time() method to save the time stamp
import random as rd
import time as t
def main():
    
   timeInSeconds = rd.randint(2,4)
   print("Your target time is "+ str(timeInSeconds) + " seconds \n Press enter to begin...")
   input("")
   
   startTime = t.time()
   
   print("Press enter again in " + str(timeInSeconds) + " seconds....")
   input("")
   
   endTime = t.time()
   
   timeElapsed = endTime - startTime
   
   if (timeElapsed < timeInSeconds):
      print("You pressed too EARLY ("  + str(timeElapsed) +  "!!!")
   
   elif (timeElapsed > timeInSeconds):
       print("You pressed too LATE (" + str(timeElapsed) + ")!!!")
   
   else:
       print("You WON!!!")
   

if __name__ == "__main__":
    main()
