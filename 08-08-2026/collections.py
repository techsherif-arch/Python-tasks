#List – Find Even Numbers
num=[10,15,22,31,40,55]
for i in num:
    if i % 2 == 0:
        print(i)
#Tuple – find largest number
num=(25,10,45,30,15)
largest = num[0]
for i in num:
    if i > largest:
        largest = i
print("largest is", largest)
#Set – Find Common Values
a={10,20,30,40}
b={30,40,50,60}
common = a & b
print("Common values:", common)
#Dictionary – Find Student Marks
stu={
    "Arun": 75,
    "Bala": 85,
    "Kumar": 65,
    "Rahul": 90
}
for name in stu:
    if stu[name] >= 80:
        print(name, stu[name])
