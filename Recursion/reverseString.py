def reverse(str):
    print(str)
    if(len(str)==0):return ''
    return str[-1]+reverse(str[0:-1])

print(reverse("srinivas"))

