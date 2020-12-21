#Name:Tarini Srikanth
#Instructor: Clark Turner
#Project- Lab6

def sum(inputList):
    #finds the sum of all the numbers
    totalSum =0
    for num in inputList:
        totalSum = totalSum+num
    return totalSum

def index_of_smallest(inputList):
    #finds the index of the smallest value
    min_value = inputList[0]
    min_index=0
    #compares it to the min_index
    for i in range(len(inputList)):
        if(inputList[i]<min_value):
            min_value =inputList[i]
            min_index=i
    return min_index

            
    
