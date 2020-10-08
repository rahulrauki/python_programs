fhand=open("words.txt")
def toString(lis):
    return ''.join(lis)
perms=[]
def permute(a,l,r):
    if l==r:
        perms.append(toString(a))
    else:
        for i in range(l,r+1):
            a[l],a[i] = a[i],a[l]
            permute(a,l+1,r)
            a[l],a[i] = a[i],a[l]
print()
string=input("Enter the word to be decoded ")
string=string.lower()
print()
print('-'*120)
#print()
n=len(string)
a=list(string)
permute(a,0,n-1)
c=0
finalList=[]
for word in fhand:
    word=word.strip()
    wor=word.lower()
    if word in perms:
        word=word.upper()
        if not word in finalList:
            finalList.append(word)
        c+=1
if c==0:
    print("No words found in the dictionary")
print("The possible words are: ")
for i in finalList:
    print(i, end=" ")
print()
