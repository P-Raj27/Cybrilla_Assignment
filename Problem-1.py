#PROBLEM 1
n,k=[int(x) for x in input().split()]
lst=[int(x) for x in input().split()]
s_lst=sorted(lst)

count=0
summ=0
prev=0
for i in range(len(s_lst)-1,-1,-1):
    if(s_lst[i]!=prev):       #CHecks FOR THE PREVIOUS ELEMENT SAME OR NOT.
        count=count+1
    if(count>k):
        break 
    summ=summ+s_lst[i]       
    prev=s_lst[i]              #Updates the Previous Element
print(summ)
