n = int(input())
while (n>0):
    flag = "NO"
    n-=1
    ls = list(map(int, input().strip().split()))
    full_sum=0
    for j in ls:
        full_sum+=j
    for i in range(1,1<<len(ls)):
        sum=0
        for j in range (0,len(ls)):
            if(i & (1<<j) !=0):
                sum+=ls[j]
               # print (ls[j] , end= ' ')
        if sum*2 == full_sum:
            flag = "YES"
            break
    print(flag)        
