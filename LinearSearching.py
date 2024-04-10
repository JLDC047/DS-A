
list_of_items = [1,8999,7,456,703,5,2998,4885,4000,8400,2521,2,173,67,352]

value = int(input("What is the value you are looking for? "))

found = False

for i in range(0,len(list_of_items)):
    if list_of_items[i] == value:
        found = True
        print(value,"is at the position",i)
        break
    else:
        print("Not this value")    
if found == False:
    print(value,"was not in the list")        
