**Types of Inheritance in Python**



Inheritance is a feature of Object-Oriented Programming (OOP) where one class can use the properties and methods of another class.



**There are 5 main types of inheritance in Python:**



**1.Single Inheritance**



One child class inherits from one parent class.



class Parent:

&#x20;   def show(self):

&#x20;       print("Parent class")



class Child(Parent):

&#x20;   def display(self):

&#x20;       print("Child class")



obj = Child()

obj.show()

obj.display()



**---------------------------------------------------------------------------------------------------------------------------------------------------------**



**2. Multiple Inheritance**



One child class inherits from more than one parent class.



class Father:

&#x20;   def money(self):

&#x20;       print("Father's money")





class Mother:

&#x20;   def house(self):

&#x20;       print("Mother's house")





class Child(Father, Mother):

&#x20;   pass



obj = Child()

obj.money()

obj.house()





**!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!**



**3. Multilevel Inheritance**



A class inherits from another child class, forming a chain.



class Grandfather:

&#x20;   def property(self):

&#x20;       print("Grandfather's property")

class Father(Grandfather):

&#x20;   pass

class Child(Father):

&#x20;   pass

obj = Child()

obj.property()





**\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\***

**4. Hierarchical Inheritance**



Multiple child classes inherit from the same parent class.



class Parent:

&#x20;   def show(self):

&#x20;       print("Parent class")



class Child1(Parent):

&#x20;   pass



class Child2(Parent):

&#x20;   pass



obj1 = Child1()

obj2 = Child2()



obj1.show()

obj2.show()



**++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++**



**5. Hybrid Inheritance**



A combination of two or more types of inheritance.



class A:

&#x20;   def show(self):

&#x20;       print("Class A")



class B(A):

&#x20;   pass



class C(A):

&#x20;   pass



class D(B, C):

&#x20;   pass



obj = D()

obj.show()









