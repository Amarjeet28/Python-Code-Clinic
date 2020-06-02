# INCOMPLETE -- How to input a multilevel list?
# Revisit this exercise again

class do_the_calculations:
    
    def __init__(self,multiLevelList):
        self.multiLevelList = multiLevelList
        
    def find_indexes(self):
        print((self.multiLevelList))
            
    


def main():
    
    input_list = list(input("Enter the list: "))
    print(input_list)
    #multiLevelList = str.split(input_list,",")
    #dtc = do_the_calculations(multiLevelList)
    #dtc.find_indexes()
    


if __name__== "__main__":
    main()
