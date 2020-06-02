"""Merge "n"" csv files into one, they may have different number and order of columns"""
""" Key Learnings:
    1. If For loop and some assignment is needed then think of:
           self.dataSet = [pd.read_csv(eachPath) for eachPath in path]
    2. Concat function in pandas library requires first element as List of Dataframes
       so it has to be given as [df1,df2,df3] or as in this case directly a list"""

import pandas as pd

class MergeCSV():
    
    def __init__(self):
        pass
    
    def generateOutput(self, *path, outputFilePath = "./../Input Files/Student Marks Final.csv"):
        self.dataSet = [pd.read_csv(eachPath) for eachPath in path]
        self.outputDataSet = pd.concat(self.dataSet,ignore_index = True, sort=False) 
        print(self.outputDataSet)

def main():
    mc = MergeCSV()
    mc.generateOutput("./../Input Files/Student Marks 1.csv","./../Input Files/Student Marks 2.csv","./../Input Files/Student Marks 3.csv")
    

if __name__ == "__main__":
    main()
    