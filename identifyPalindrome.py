# -*- coding: utf-8 -*-

#Check if the input string is palindrome or not
#Ignore white spaces
#Only cosider a-z in the given string
#palindrome chceker has to be cases insensitive

import re

class palindrome:
    
    def __init__(self,Str):
        self.InputString = Str
        self.NewString = ''
        
    def checkPalindrome(self):
       self.InputString = (self.InputString).lower()
          
       self.CleanedString = ''.join(re.findall(r'[a-z]+', self.InputString))
     
       revInputString = self.CleanedString[len(self.CleanedString)::-1]
                    
       return(revInputString == self.CleanedString)
           

def main():
    Str = input("Enter String:")
    pal = palindrome(Str)
    print(pal.checkPalindrome())
    
    
if __name__ == "__main__":
    main()
