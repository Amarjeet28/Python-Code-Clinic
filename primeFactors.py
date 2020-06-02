# Prints all unique prime factors of the input number

import math 

class performCalculations:
    
    def __init__(self, num):
        self.InputNumber = num
              
    def isPrime(self, factor):
        for x in range(2,factor):
            if (factor % x == 0):
                return False
        return True    

    def findPrimeFactors(self):
        ###
        Factors = []
        ###
        
        for x in range(2,math.ceil(self.InputNumber/2)+1):
            if ((self.InputNumber % x) == 0 and self.isPrime(x)):
                   Factors.append(x)
        if len(Factors) == 0:
            print(self.InputNumber)
        else:
            print(Factors)
  
    
def main():

    num = int(input("Enter your value: ")) 
    pc = performCalculations(num)
    pc.findPrimeFactors()

if __name__ == "__main__":
    main()