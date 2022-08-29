def dtb(num):
    if(num==0):return
    dtb(int(num/2))
    print(num%2)
dtb(10)