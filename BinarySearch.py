
list_of_items = [1,8999,7,456,703,5,2998,4885,4000,8400,2521,2,173,67,352,6500,1000,914]
list_of_items.sort()
print(list_of_items)

value = int(input("What is the value you are looking for? "))#

"""found = False

start=0
end=len(list_of_items)

while start <= end:
    middle = (start + end)//2
    item = list_of_items[middle]
    if value == item:
        print(value,"is in the position",middle)
        found = True
        break
    elif value > item:
        start = middle + 1
    else:
        end = middle - 1      

if found == False:
    print(value,"isn't the list")"""

#recursion
start=0
end=len(list_of_items)  

def binary(v, start, end):  
    if start <= end:
        pos = (start + end)//2
        item = list_of_items[pos]
        if v == item:
            return pos
        elif v > item:
            return binary(v, pos+1, end)
        else:
            return binary(v, start, pos-1)
    else:
        return -1
    
result = binary(value, start, end)    
if result == -1:
    print(value,"is not in the list.")
else:
    print(value,"is in the position",result)   
