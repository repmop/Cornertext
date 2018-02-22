import copy
def memeify(input):
    def printer(L):
        temp2=""
        for i in range(len(L)):
            for j in range(len(L[i])):
                temp2= temp2+L[i][j][0] if L[i][j][0]!='0' else temp2+" "
            temp2+="\n"
        return temp2
    te,s="",""
    for c in input:
        if c!=" ":te+=c
    for c in te:
        s+=c+" "
    s=s[:-1]
    if len(s)<3: return "String must be at least 3 characters long"
    if s[0]!=s[-1]: return "Error: Different first and last characters"
    if len(te)%2==0: return "Error: Even number of characters" 
    l=len(s)
    middle=(l+1)//2
    longdim=middle+l-1
    heightdim=middle+middle//2
    temp=[copy.deepcopy([copy.deepcopy('0') for i in range(longdim+4)]) for i in range(heightdim+4)]
    alternate=True
    for i in [0,middle//2,heightdim-middle//2-1,heightdim-1]:
        for strind in range(len(s)):
            temp[i][strind+alternate*(middle-1)+4]=s[strind]
        alternate=not alternate
    for strind in range(len(te)):
        for j in [0,l-1,middle-1,longdim-1]:
            temp[strind+alternate*(middle//2)][j+4]=te[strind]
            if j==l-1 or j==longdim-1: alternate=not alternate
    for loop in range(middle//2-1):
        temp[middle//2-1-loop][(loop+1)*2+4]='/'
        temp[middle//2+l//2-1-loop][(loop+1)*2+4]='/'
        temp[middle//2+l//2-1-loop][(loop+1)*2+3+l]='/'
        temp[middle//2-1-loop][(loop+1)*2+3+l]='/'
    finished= (printer(temp))
    return finished
#str="A L O L U L A"
#print(memeify(str))

