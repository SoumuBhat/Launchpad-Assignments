my_dict =dict()
for i in range(3): 
    key = input("Enter the name ")
    value = input("Enter the USN")
    my_dict[key] = value
for i,k in my_dict.items():
    print(i+":"+k)