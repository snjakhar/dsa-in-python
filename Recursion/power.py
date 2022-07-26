from tkinter import N


def power(n,m):
    if(m==1):return n
    elif(m==0):
        return 1
    else:
        return n*power(n,m-1)
print(power(2,0))