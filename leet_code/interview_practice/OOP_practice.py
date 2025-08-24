# class Shape:
#     def __init__(self):
#         pass
#     # def areaa():
#     #     return 
    
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    


s = [Rectangle(3,2), Circle(4)]

for i in s:
    print(i.area())

        







"""
class BankAccount:
    def __init__(self, owner, staring_balance = 0):
        self.owner = owner
        self.balance = staring_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Not valid")
        self.balance +=  amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Not sufficient fund to withdraw")
        self.balance -= amount
        return self.balance
        
    def get_balance(self):
        return self.balance
    
customer = BankAccount("Richie", 100)
print(customer.deposit(5000))
print(customer.withdraw(50))
"""










# class Extract:
#     def __init__(self, date_time, file_path):
#         self.a = date_time
#         self.b = file_path
#         print("init menthod executed")

#     def add_info(self, age, sex):
#         self.age = age
#         self.sex = sex
        
#         # print(self.a, self.b)
#         # print(date_time,file_path)

#     def hello_etl(self):
#         print(f"hello user. Today's extraction process starts at {self.a} and reads {self.b}")
#         print(f"age of pt is {self.age} and sex of pt is {self.sex}")




# if __name__ == "__main__":
#     ob1 = Extract('07/21', 'vish/leetcode.txt')
#     ob1.add_info('28', 'Female')

#     ob1.hello_etl()
#     #object.method
#     # ob1.custom_print('07/22', 'wiewj')





