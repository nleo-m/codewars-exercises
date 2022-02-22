#Task: Return an ordered array with the indexes of each capital letter in a given string

def capitals(word):
    lst_capital = []
    index = 0
    for l in word:
        if l.isupper():
            lst_capital.append(index)
        index+=1
    return lst_capital

#Example:
#capitals('CodEWaRs')