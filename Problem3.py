my_list=[]
l=[]
n=int(input("Enter the no of values")) 
for i in range(n):
    a=input("Enter the values")
    my_list.append(a)
j=int(input("Eter the value to serch"))    
count=0
for i in my_list:
    print(i)
    if int(i) == int(j):
        l.append(count)
    count+=1    
print(l)        
