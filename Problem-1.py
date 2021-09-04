#PROBLEM 1
n,k=[int(x) for x in input().split()]
lst=[int(x) for x in input().split()]
s_lst=sorted(lst)

count=0
summ=0
prev=0
for i in range(len(s_lst)-1,-1,-1):
    if(s_lst[i]!=prev):
        count=count+1
    if(count>k):
        break
    
    if(s_lst[i]!=prev ):
        summ=summ+s_lst[i]
        #count=count+1
        prev=s_lst[i]
    else:
        summ=summ+s_lst[i]
    #print(count)
    
    
    
        
        
        
print(summ)
