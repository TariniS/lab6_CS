#Name:Tarini Srikanth
#Instructor: Clark Turner
#Project- Lab6, Strings


def str_rot_13(inputString):
    #takes a string and converts it based on rot13
    resultString =''
    for c in inputString:
        o=ord(c)
        if o>=ord('a')and o<=ord('z'):
            #checks if it is a letter
            if o>ord('m'):
                #either adds or subtracts based on value
                o=o-13
            else:
                o=o+13
        elif o>=ord('A')and o<=ord('Z'):
            if o>ord('M'):
                o=o-13
            else:
                o=o+13
        resultString = resultString+chr(o)
        #adds to the resulting string
    return resultString

def str_translate_101(string, old, new):
    #replaces the old words with the new words in the string
    #using list comprehension
    stringList = list(string)
    [new for i in stringList if stringList[i]==old]
    return str(stringList)
    
    
        
        
        
        
    


