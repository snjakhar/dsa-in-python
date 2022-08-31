from logging import captureWarnings


def capitalizeWords(words):
    if len(words)==0:return ''
    return words[0].upper()+capitalizeWords(words[1:])





words = ['i', 'am', 'learning', 'recursion']
result=capitalizeWords(words) # ['I', 'AM', 'LEARNING', 'RECURSION']
print(result)