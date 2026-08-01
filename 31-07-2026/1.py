sum=0
while (True):
    n= int (input("Enter the number"))
    if n==0:
        break
    elif not (0<=n <=6):
        continue
    else:
        sum=sum+n
print (sum)
    
