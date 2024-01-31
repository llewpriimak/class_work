#  File: employee.py
#  Description:
#  Student Name:
#  Student UT EID:
#  Partner Name:
#  Partner UT EID:
#  Course Name: CS 313E
#  Unique Number:
#  Date Created:
#  Date Last Modified:

import sys

class Employee:

    def __init__(self, **kwargs):
        self.name = None
        self.id = None
        self.salary = None
        if kwargs.get('name'):
            self.name = str(kwargs['name'])
        if kwargs.get('id'):
            self.id = str(kwargs['id'])
        if kwargs.get('salary'):
            self.salary = str(kwargs['salary'])

    def __str__(self):
        return 'Employee\n'\
            '{0},{1},{2}'.format(self.name, self.id, self.salary)



############################################################
############################################################
############################################################

class Permanent_Employee(Employee):

    def __init__(self, **kwargs):
        Employee.__init__(self, **kwargs)
        self.benefits = None
        if kwargs.get('benefits'):
            self.benefits = str(kwargs['benefits'])


    def cal_salary(self):
        if self.benefits == ['health_insurance']:
            return self.salary * .9
        if self.benefits == ['retirement']:
            return self.salary * .8
        if self.benefits == ['retirement', 'health_insurance']:
            return self.salary * .7



    def __str__(self):
        return 'Permanent_Employee\n'\
            '{0},{1},{2},{3}'.format(self.name, self.id, self.salary, self.benefits)


############################################################
############################################################
############################################################

class Manager(Employee):

    def __init__(self, **kwargs):
        Employee.__init__(self,**kwargs)
        self.bonus = None
        if kwargs.get('bonus'):
            self.bonus = int(kwargs['bonus'])

    def cal_salary(self):
        return self.salary + self.bonus


    def __str__(self):
        return 'Manager\n'\
            '{0},{1},{2},{3}'.format(self.name, self.id, self.salary, self.bonus)




############################################################
############################################################
############################################################
class Temporary_Employee(Employee):

    def __init__(self, **kwargs):
        Employee.__init__(self, **kwargs)
        self.hours = None
        if kwargs.get('hours'):
            self.hours = str(kwargs['hours'])


    def cal_salary(self):
        return self.salary * self.hours


    def __str__(self):
        return 'Temporary_Employee\n'\
            '{0},{1},{2},{3}'.format(self.name, self.id, self.salary, self.hours)



############################################################
############################################################
############################################################


class Consultant(Temporary_Employee):

    def __init__(self, **kwargs):
        Temporary_Employee.__init__(self, **kwargs)
        self.travel = None
        if kwargs.get('travel'):
            self.travel = int(kwargs['travel'])

    def cal_salary(self):
        return Temporary_Employee.cal_salary()

    def __str__(self):
        return 'Consultant \n'\
            '{0},{1},{2},{3}'.format(self.name, self.id, self.salary, self.hours)

############################################################
############################################################
############################################################


class Consultant_Manager(Manager,Consultant):

    def __init__(self,  **kwargs):
        Manager.__init__(self, **kwargs)
        Consultant.__init__(self, **kwargs)

    def cal_salary(self):
        return self.salary * self.hours + self.travel * 1000 + self.bonus

    def __str__(self):
        return'Consultant_Manager\n'\
            # '{0},{1},{2},{3},{4},Consultant_Manager\n'.format(self.name, self.id, self.salary, self.hours,self.travel)
            # '{0},{1},{2},{3}'.format(self.name, self.id, self.salary, self.bonus)



############################################################
############################################################
############################################################



###### DO NOT CHANGE THE MAIN FUNCTION ########

def main():

    chris = Employee(name="Chris", id="UT1")
    print(chris, "\n")

    emma = Permanent_Employee(name="Emma", id="UT2", salary=100000, benefits=["health_insurance"])
    print(emma, "\n")

    sam = Temporary_Employee(name="Sam", id="UT3", salary=100,  hours=40)
    print(sam, "\n")

    john = Consultant(name="John", id="UT4", salary=100, hours=40, travel=10)
    print(john, "\n")

    charlotte = Manager(name="Charlotte", id="UT5", salary=1000000, bonus=100000)
    print(charlotte, "\n")

    matt = Consultant_Manager(name="Matt", id="UT6", salary=1000, hours=40, travel=4, bonus=10000)
    print(matt, "\n")

    ###################################
    print("Check Salaries")

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["health_insurance"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["retirement", "health_insurance"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")

    print("Sam's Salary is:", sam.cal_salary(), "\n")

    print("John's Salary is:", john.cal_salary(), "\n")

    print("Charlotte's Salary is:", charlotte.cal_salary(), "\n")

    print("Matt's Salary is:",  matt.cal_salary(), "\n")


if __name__ == "__main__":
    main()


