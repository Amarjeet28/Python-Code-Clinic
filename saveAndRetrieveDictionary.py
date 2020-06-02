#Assignment Question: Write to methods to save a dictionary to a file and retrieve it
#-----------------------------------------------
# Key Learnings:
 # How to read/write a file using native Python methods
 # How to iterate through dictionaries
 # Read line also brings in \n so rstrip
#-----------------------------------------------
# Instructor has used pickle to store the data by converting the dictionary to
# bytes. That allows to store images as well.
    #import pickle
    # with open(path,"w") as file:
    #     pickle.dump(newDict, file)
    
    # with open(path,"r") as file:
    #     pickle.load(file)

#----------------------------------------------


def saveDictionary(newDict,path):
    file = open(path,"w")
            
    for key in newDict:
        file.write(str(key) + "->" + str(newDict[key])+"\n")
        
    file.close()
    
    
def loadDictionary(path):
    file = open(path,"r")
    newDict = {}
    
    for line in file:
        line = line.rstrip("\n")
        [keyText,valueText] = str.split(line,sep="->")
        newDict[keyText] = valueText
        
    print(newDict)
    

def main():
    newDict = {"brand": "Ford", "model": "Mustang", "year": 1964}
    userChoice = int(input("Input Your Choice: \n1) Save Dictionary \n2) Load Dictionary\n"))
    
    if userChoice == 1:
       path = input("Enter File Path: ")
       saveDictionary(newDict,path)   
       print("Dictionary saved successfully")
    else:
       path = input("Enter File Path: ")
       loadDictionary(path)
       print("Dictionary loaded successfully")

    
    
if __name__ == "__main__":
    main()
