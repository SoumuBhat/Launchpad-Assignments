my_list=[]
lst=[]
n=int(input("Enter the no of values")) 
for i in range(n):
    a=input("Enter the values")
    my_list.append(a)
for i in my_list:
   if int(i)<5:
       lst.append(i)
print(lst)
