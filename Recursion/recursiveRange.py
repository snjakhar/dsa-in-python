def recursiveRange(n):
    if(n==0):return n
    else:return n+recursiveRange(n-1)
  

print(recursiveRange(10))