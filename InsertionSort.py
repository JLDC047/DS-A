
SCPs = [1,8999,2521,4000,5659,2998,4885]

for i in range(0,len(SCPs)):
    key = SCPs[i]
    point = i - 1
    while point >= 0 and key < SCPs[point]:
        SCPs[point + 1] = SCPs[point]
        point -= 1
    SCPs[point + 1] = key    
    print(SCPs)







