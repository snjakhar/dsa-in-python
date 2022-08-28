from multiprocessing.dummy import Array
from array import *
arr1=array('i',[1,2,3,4])
print(arr1)
arr1.insert(0,0)
print(arr1)
def traverse(arr1):
    for item in arr1:
        print(item)
traverse(arr1)

def search(array,value):
    for e in array:
        if e==value:
            return print(array.index(value))
search([1,2,3,4,4],4)


