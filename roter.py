alfabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
        "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
        "U", "V", "W", "X", "Y", "Z"]

def RoterOne(word):    
    roter = alfabet.copy()
    result = ""
    for i in word:        
        index = alfabet.index(i)
        result += roter[index]
        roter.append(roter.pop(0))
    return result

print(RoterOne("H"))
