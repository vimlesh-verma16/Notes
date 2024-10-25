
class PlayerCharacter:
    
    membership = True # This is Class object attribute
    def __init__(self,name='anonymous',age=18): #Constructor with default argument 
        if (PlayerCharacter.membership):
            self.__name = name  #attribute
            self.__age = age  #make a private member variable  #Abstraction  (Private and public)with __

        if age < 18:
            print(f'{self.__name} below 18 year of age cant play') 
    
    @property  # without this we cannot access name from outside
    def name(self): 
        return self.__name 

    def run(self):
        print(f'The {self.__name} is running')

    def shout(self):
        print("player is shouting")
    
    @classmethod 
    def adding_things(cls,num1,num2): #cls stands for class it is class method
        return cls("teddy",num1 + num2) #This can be used for instainting a object


player1 = PlayerCharacter('tom',19)
player2 = PlayerCharacter('cindy',1)
player3 = PlayerCharacter()  # No argument given

print(f'player name is: {player1.name}')
#print(help(player1))
player1.shout()
player2.attack = 5 

player4 = PlayerCharacter.adding_things(118,2)
print("player name is:",player4.name)



 





#----------------------------------------------------------
# Code with harry 

''' Object Oriented programming '''
# class Employee:
#     company='Google'
#     salary=100

# harry=Employee()
# rajni=Employee()
# Employee.company='youtube'
# print(harry.company)
# print(rajni.company)
# # creating instance attribute for both the objects
# harry.salary=300
# rajni.salary=400
# print(harry.salary)
# print(rajni.salary)

# --------------------------------------------------------------------
# class Employee:
#     company='youtube'
#     def getsalary(self,signature):
#         print(f'Salary for employee working in {self.company} is {self.salary}\n{signature}')

#     @staticmethod
#     def greet():
#         print("Goodmorning, Sir")

# harry=Employee()
# harry.salary=1000
# harry.getsalary('thanks')  #it is same as Employee.getsalary(harry)
# harry.greet()  # we want Employee.getsalary()
# ----------------------------------------------------------------------
''' special method or init function(Constructor)'''
# class Employee:
#     company='youtube'

#     def __init__(self,name,salary,subunit):
#         self.name=name
#         self.salary=salary
#         self.subunit=subunit
#         print("Employee constructor is initilised: ")

#     def getDetails(self):
#         print(f'employee name is {self.name} and his salary is {self.salary} and his unit is {self.subunit}')

#     def getsalary(self,signature):
#         print(f'Salary for employee working in {self.company} is {self.salary}\n{signature}')

#     @staticmethod
#     def greet():
#         print("Goodmorning, Sir")

# harry=Employee('harry',100,'Gmail')
# harry.getDetails()
# harry.greet()

''' inheritance in Oops  '''
#single level inheritance

# class Employee:
#     company='Google'
#     def showDetail(self):
#         print("this is an employee")
# class Programmer(Employee):
#     language='python'
#     def showDetail(self):
#         print("this is programmer")

# e=Employee()
# p=Programmer()
# e.showDetail()
# p.showDetail()
# print(p.company)

''' multiple inheritance '''
# class Employee:
#     company='Google'

# class Freelancer:
#     level=1
#     company='youtube'
#     def upgrade(self):
#         self.level=self.level+1

# class Programmer(Employee,Freelancer):
#     language='python'

# p=Programmer()
# p.upgrade()
# print(p.level)

'''multilevel inheritance with super function'''


# class Person:
#     country = 'india'

#     def __init__(self):
#         print("initialising person....")

#     def takebreath(self):
#         print("i am person and i em breating ")


# class Employee(Person):
#     company = 'honda'

#     def __init__(self):
#         super().__init__()
#         print("initialising Employee....")

#     def takebreath(self):
#         # super().takebreath()
#         print("i am employee and i am heavily breathing ")


# class Programmer(Employee):
#     company = "fiverr"

#     def __init__(self):
#         # super().__init__()
#         print("initialising Programmer....")

#     def takebreath(self):
#         # super().takebreath()
#         print("it is Programmer class ")

# p=Person()
# p.takebreath()

# e=Employee()
# e.takebreath()


# pr = Programmer()
# pr.takebreath()

'''Class Method or changing the attribute of class'''
# class Employee:
#     company="Google"
#     salary=100
# def changesalary(self,sal):
#     self.__class__.salary=sal  #__class__ is called dunder method or class
#     print(self.salary)

#     @classmethod
#     def changesalary(cls,sal):
#         cls.salary=sal
#         print(cls.salary)

# e=Employee()
# print(e.salary)
# e.changesalary(300)
# print(e.salary)

'''class decorator or getters or setters '''


# class Employee:
#     salary = 5700
#     bonous = 300
#     # totalsalary=6000

#     @property  # it is a getter function
#     def totalsalary(self):
#         return self.salary+self.bonous

#     @totalsalary.setter  # it is setting some value
#     def totalsalary(self, val):
#         self.bonous = val-self.salary


# e = Employee()
# print(e.totalsalary)
# e.totalsalary =65000
# print(e.bonous)
# print(e.salary)

'''operator overloading '''


# class Number:
#     def __init__(self, num):
#         self.num = num

#     def __add__(self, num2):
#         print('lets add')
#         return self.num+num2.num

#     def __mul__(self, num2):
#         print('lets multiply')
#         return self.num*num2.num

#     def __str__(self):
#         return f'this is decimal number {self.num}'

#     def __len__(self):
#         return 1

# n1 = Number(4)
# n2 = Number(6)
# sum = n1+n2
# sum = n1*n2
# print(sum)


# n=Number(9)
# print(n)
# print(len(n))


# -----------------------------------------------------------------------