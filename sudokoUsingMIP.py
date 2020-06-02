"""Need to work on this further"""
"""Write a program to solve sudoku"""
"""Input will be a nested list with two dimensions:
    
  [[5 3 0  0 2 4  7 0 0 
    0 0 2  0 0 0  8 0 0 
    1 0 0  7 0 3  9 0 2 
 
    0 0 8  0 7 2  0 4 9 
    0 2 0  9 8 0  0 7 0 
    7 9 0  0 0 0  0 8 0 
 
    0 0 0  0 3 0  5 0 6 
    9 6 0  0 1 0  3 0 0 
    0 5 0  6 9 0  0 1 0]]
  
  
  Output:
[[
5 3 9  8 2 4  7 6 1  
6 7 2  1 5 9  8 3 4  
1 8 4  7 6 3  9 5 2  

3 1 8  5 7 2  6 4 9  
4 2 5  9 8 6  1 7 3  
7 9 6  3 4 1  2 8 5  

8 4 1  2 3 7  5 9 6  
9 6 7  4 1 5  3 2 8  
2 5 3  6 9 8  4 1 7 ]]"""
  
from pulp import *
import math
import pandas as pd

class SudokuMIPSolver():

   def __init__(self, model):
       self.model = model
       self.values = [x for x in range(1,10)] #Every cell can take values as 1-9
       self.rows = [x for x in range(1,10)] #Range of rows 1-9
       self.columns = [x for x in range(1,10)] #Range of columns 1-9
       
       
   def initializeDecisionVaribales(self):
       self.choices = LpVariable.dicts("Choice", (self.values,self.rows,
                                                  self.columns), cat='Binary')
    
       #print(self.choices[1][1].values())
      
   def generateObjectiveFunction(self):
       print("Generate OF")   
       """this does something"""
   
   def generateConstraints(self):
       """Each Row Should Contain a Particular Value Only Once"""
       for v in self.values:
           for r in self.rows:
               self.model+=lpSum(self.choices[v][r][c] for c in self.columns) ==1
       
       """Each Column Should Contain a Particular Value Only Once"""
       for v in self.values:
           for c in self.columns:
               self.model+=lpSum(self.choices[v][r][c] for r in self.rows) ==1
       
       #Each 3x3 Box Should Contain a Particular Value Only Once
       boxNo = list()
   
       for r in self.rows:
           for c in self.columns:
               if ((math.ceil(r/3)-1)*3 + math.ceil(c/3)) == 1:
                   self.model+=lpSum(self.choices[v][r][c] for v in self.values)==1
        #print(boxNo)
       # for iterator in range(len(boxNo)):
       #     b = boxNo[iterator][0]
       #     r = boxNo[iterator][1]
       #     c = boxNo[iterator][2]
       #     boxNoDict[b] = {r,c}
      
       # print(boxNoDict)
             
       
        
       self.model.writeLP("./../Output Files/temp.csv")
           #print("Generate Constrts")
       

def main():
    
    #Create an instance of Optimization Problem
    SudokuProblem = LpProblem("SudokuProblem", LpMinimize)
    
    #Instantiate my class for constructing the optimization problem
    sms = SudokuMIPSolver(SudokuProblem)
    sms.initializeDecisionVaribales()
    #sms.generateObjectiveFunction()
    sms.generateConstraints()

if __name__ == "__main__":
    main()

          
          
    
    
    