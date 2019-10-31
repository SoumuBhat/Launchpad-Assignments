lst=[]
n=int(input("Enter the no of values")) 
for i in range(n):
    a=input("Enter the values")
    lst.append(a)
tmp=[]
for i in lst:
    if i not in tmp:
        tmp.append(i)
print(tmp)

