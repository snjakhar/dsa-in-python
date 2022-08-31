def dtb(num):
    if(num==0):return
    dtb(int(num/2))
    print(num%2)
dtb(10)

def dToB(n):
    if(n==0):
        return 0
    else:
        return n%2+10*dToB(int(n/2))

print(dToB(12))