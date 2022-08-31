import string


def capitalFirst(strings):
    result=[]
    if(len(strings)==0):return result
    strings[0]=strings[0][0].upper()+strings[0][1:]
    result.append(strings[0])
    return result+capitalFirst(strings[1:])



print(capitalFirst(['car', 'taco', 'banana']))

print([1,2]+[3])