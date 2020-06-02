"""Read a text file and group the words and show most commonly occuring words"""
"""Key Learnings:
                How to use the Counter object from Collections class
                It is a special type of dictionary - hashtable of iterables"""

import re
from collections import Counter

class ReadFileAndGenerateSummary():
    
    def __init__(self,path):
        self.path = path
    
    def readFile(self):
        WordsAndCountInFile = Counter()
        file = open(self.path, "r", encoding ="utf8")
        #PunctuationString = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
        FileText = file.read()
        FileTextContents = re.findall(r"[\w']+|[!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~]", FileText.lower())
        
        
        for word in FileTextContents:
            if word in WordsAndCountInFile:
                WordsAndCountInFile[word] +=1
            else:
                WordsAndCountInFile[word]=1
                
        print("Unique Number Of Words: ", len(FileTextContents))
        
        
        for words in WordsAndCountInFile.most_common(20):
            print(words[0], " : ", words[1])

def main():
    RFGS = ReadFileAndGenerateSummary("./../Input Files/CompleteWorkOfShakespeare.txt")
    RFGS.readFile()
    
    
    
if __name__ == "__main__":
    main()
