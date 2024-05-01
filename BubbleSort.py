
"""list = [1,8999,2521,4000,5659,2998,4885]
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
print(list)"""

class Sort:
    def __init__(self, values):
        self.values = values

    def bubble(self, n):
        swapped = False
        for i in range(0, n-1):
            #print(self.values) 
            if self.values[i] > self.values[i+1]:
                #print("swap")
                temp = self.values[i]
                self.values[i] = self.values[i+1]
                self.values[i+1] = temp
                #print(self.values)
                swapped = True
        if swapped == True:  
            #print("recursive call")  
            self.bubble(n-1)

list1 = Sort([1,8999,2521,4000,5659,2998,4885]) 
print(list1.values)
list1.bubble(len(list1.values)) 
print(list1.values)  

list2 = Sort([8999,96,49,1,2521,4000,5659,2998,4885]) 
print(list2.values)
list2.bubble(len(list1.values)) 
print(list2.values) 

