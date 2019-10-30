s=str(input("Enter the sentence"))
s=s.split(" ")
s=s[-1::-1]
s=' '.join(s)
print(s)