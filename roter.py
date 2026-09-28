alfabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
        "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
        "U", "V", "W", "X", "Y", "Z"]


roter = alfabet.copy()

def RoterOne(word):    
    result = ""
    for i in word:        
        
        index = alfabet.index(i)
        result += roter[index]
        roter.append(roter.pop(0))        
    return result

