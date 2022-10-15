import string


def change(v,b):
    language = dict()
    l = list()
    alphabet = list(string.ascii_uppercase)
    num = 10
    for i in alphabet:
        language[num] = i
        num+=1
    text = ''
    while True:
        newval = v//b
        ost = v%b
        l.append(ost)
        if v//b==0:
            break
        v = newval
    for i in range(len(l)):
        if l[i]>9:
            l[i] = language.get(l[i])
    l.reverse()
    number = ''.join(map(str, l))
    return number
    
val, base = map(int,input().split(" "))
print(change(val, base))
    


