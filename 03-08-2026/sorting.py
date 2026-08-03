#write a code to implement sorting in ascending using list datatype

#ascending
a=[55,44,33,22,11,99,77,66,88,12,34,56,98,78,96,32,14,54,10,20,1,100]
for i in range(len(a)):
    for j in range (i+1,len(a)):
        if a[i]>a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print (a)
print()

#decending
a=[55,44,33,22,11,99,77,66,88,12,34,56,98,78,96,32,14,54,10,20,1,100]
for i in range(len(a)):
    for j in range (i+1,len(a)):
        if a[i]<a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print (a)
    
