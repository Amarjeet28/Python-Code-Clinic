"""Simulate the roll  of "k" dices each with "n" sides and find out the probability 
of the occurence of each outcome using Monte Carlo Simulation"""

#Key Learnings: How to provide dynamic number of arguements to a function
#             : Using Monte Carlo Simulation - repeating the experiment a 
#               huge number of times to generate the probabilties

import random

def generateProbabilties(*dice, numberOfSimulations = 1000000):
    
    outcomes = {}
    #Initialize the dictionary with all possible outcomes
    for possibleOutcomes in range(len(dice),sum(dice)+1):
        outcomes[possibleOutcomes] = 0
        
    #Repeatedly simulate the rolling of die
    for iterations in range(1,numberOfSimulations):
     outcome = 0
     for d in dice:
      outcome = outcome + random.randint(1,d) 
      
     outcomes[outcome] +=1
    
    for possibleOutcomes in range(len(dice),sum(dice)+1):
        print(possibleOutcomes,":", '{:0.2f}%'.format(outcomes[possibleOutcomes]/numberOfSimulations*100))
     
def main():
  #This function can take any number of arguements
  generateProbabilties(4,6,6)

if __name__ == "__main__":
    main()
    