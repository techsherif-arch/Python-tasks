'''write teh code to print the following series

1 2 30 4 5 60 7 8 90'''
count =1
while count<=9:
    if count%3==0:
        print(count*10,end=' ')
    else :
        print(count,end=" ")
    count+=1
