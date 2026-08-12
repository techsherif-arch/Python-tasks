n=input("enter ur name")
p=input("enter ur password")

login= lambda n,p: n=="sherif" and p=="555"
if login(n,p):
    print ("valid")
else:
    print ("invalid")
