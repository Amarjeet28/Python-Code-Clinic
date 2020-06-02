"""Use the Diceware list to generate a password in terms of a paraphrase"""
"""Key Learnings:
    1. Use int() and str() methods for type conversion
    2. randint(1,n) method to generate random number between 1 to n. Import random"""
    
import random


class PasswordGenerator():
    
    def __init__(self):
        self.diceWareWordMapping = {}
        
    def readDiceWareDictionary(self):
        file = open("./../Input Files/DicewareWordList.txt","r")
        for line in file.readlines():
            self.diceWareWordMapping[line.split()[0]]=line.split()[1]
          
    
    def generateParaphrase(self, lengthOfPassword):
        password = ""
        
        #Simulate dice rolls lengthOfPassword*5 times
        for rollDice in range(1,lengthOfPassword+1):
            keyNumber = ""
          
            for iterator in range(1,6):
                digit = random.randint(1,6)
                keyNumber = keyNumber + str(digit)
            if password =="":
               password = self.diceWareWordMapping[keyNumber]
            else:
                password = password + " " + self.diceWareWordMapping[keyNumber]
        print(password)
        

def main():
    pg = PasswordGenerator()
    pg.readDiceWareDictionary()
    pg.generateParaphrase(3)
    

if __name__ == "__main__":
    main()
    