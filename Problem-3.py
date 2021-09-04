# Cybrilla_Assignment
This Repo contains the code for the Cybrilla Assignment
string=input()
f=0
for i in range(len(string)-1):
    if(string[i]!=string[-(i+1)]):         #checking for two elements
        f=1
if(f==1):
    print("Not Palindrome")
else:
    print("palindrome")
