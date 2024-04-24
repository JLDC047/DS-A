
list = [1,8999,2521,4000,5659,2998,4885]
print(list)

def bubble(n):
    swapped = False
    for i in range(0, n-1):
        print(list) 
        if list[i] > list[i+1]:
            print("swap")
            temp = list[i]
            list[i] = list[i+1]
            list[i+1] = temp
            print(list)
            swapped = True
    if swapped == True:  
        print("recursive call")  
        bubble(n-1)


bubble(len(list))
print(list)
