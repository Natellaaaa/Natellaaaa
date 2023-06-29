# # Принципы ООП. Наследование Полиморфизм Инкапсуояция и Абстракция

# hello = ""
# lst = []
# def hello_word ():
#     pass
# hello_word()

# class Hello:
#     pass
# hello = Hello

# class Person: #Родительский класс 
#     def __init__(self, name, surname, age): # Конструктор
#         self.name = name #Атрибут
#         self.surname = surname
#         self.age = age
    
#     def get_info(self):# метод
#         return f"{self.name} {self.surname} {self.age}"
    
# rob = Person("Роберт", "Азимов", 23)
# print(rob.get_info())

# class Bank(Person):
#     def __init__(self, name, surname, age):
#         super().__init__(name, surname, age)
#         self.balance = 0

#     def get_balane(self):
#         return f"{self.name}, баланс {self.balance} KGS"

#     def top_up_balance(self, amount):
#         self.balance += amount
#         return f"{self.name}, Ваш баланс пополнен на {amount} KGS"
    
#     def take_money(self, amount):
#         self.balance -= amount
#         return f"{self.name}, Вы сняли со своего счёта {amount} KGS"    
    
# rob_bank = Bank("Роберт", "Азимов", 23)
# print(rob_bank.get_info())
# print(rob_bank.get_balane())
# print(rob_bank.top_up_balance(1000))
# print(rob_bank.get_balane())
# print(rob_bank.take_money(1000))
# print(rob_bank.get_balance())


# class Work(Bank):
#     def __init__(self , name , surname , age , work):
#         super().__init__(name , surname, age)
#         self.work = work


# driver_askhat  = Work('Askhat', 'Abjalov', 17 , "Driver")
# print(driver_askhat.get.balance())

#Множественное наследование 
class A:
    def class_a(self):
        return f"Class A"
class B:
    def class_b(self):
        return f"Class B"
class C (A,B):
        pass


class Car:
    def __init__(self , make , model , year):
        self.make = make
        self.model = model 
        self.year = year
        self.odometer = 0
        self.fuel = 70


    def add_distance(self , km):
        self.odometr += km

    def drive(self, km):
        if (self.fuel * 10) <= km:
            self.add_distance(km)
            return f"Вы проехали {km} у вас осталось {self.fuel} литров"
        else:
            return"У вас недостаточно топлива для поездки"

camry = Car ('Tayota', 'Camry 55', 2016)
print(camry.drive(350))
print(camry.fuel)