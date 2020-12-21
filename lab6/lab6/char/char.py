#Name:Tarini Srikanth
#Instructor: Clark Turner
#Project: Lab 6

def is_lower_01(inputChar):
    #checks if the input character is lowercase
    valueOfInput = ord(inputChar)
    if valueOfInput >= 97:
        #97 is the max of the lowercase values
        return True
    else:
        return False

def char_rot_13(inputChar):
    #converts the char into the rot_13 char
    o = ord(inputChar)
    if o>=ord('a')and o<=ord('z'):
        #checks if it is a letter
        if o>ord('m'):
            #based on the value, either add of subtract 13
            o=o-13
        else:
            o=o+13
    elif o>=ord('A')and o<=ord('Z'):
        if o>ord('M'):
            o=o-13
        else:
            o=o+13
    resultChar = chr(o)
    return resultChar
        
        
        
