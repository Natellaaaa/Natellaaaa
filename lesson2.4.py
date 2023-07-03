# # Магические методы
# class Student:
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.books = []
#         self.knowledge = 0
    
#     def __str__(self):
#         return f"{self.name}, {self.surname}, {self.books}, {self.knowledge}"

#     def read_book(self, name_book):
#         self.books.append(name_book)
#         self.knowledge += 100
#         return f"Ученик прочитал книгу {name_book} и получил 100 баллов"

#     def __eq__(self, other) -> bool:
#         return other.knowledge == self.knowledge
    
#     def __gt__(self,other):
#         return self.knowledge > other.knowledge
        
#     def __lt__(self, other):
#         return self.knowledge < other.knowledge
    
# rob = Student ("Роберт", "Азимов", 18)
# print(rob)
# print(rob.read_book("Python для чайников"))
# print(rob)
# print("=========================")
# Nutella = Student("Natella", "Pepsi-Cola", 16)
# print(Nutella)
# print(Nutella.read_book("Грокаем Алгоритмы"))
# print(Nutella.read_book("Чистый код"))
# print(Nutella)
# print("=====================")
# print(rob == Nutella)
# print(rob > Nutella)
# print(rob < Nutella)

import sqlite3

connection = sqlite3.connect("bank.db")
cursor = connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS clients (
    name VARCHAR(100),
    surname VARCHAR(100),
    age INTER,
    wallet_id VARCHAR(50),
    email VARCHAR(255)
);
""")

class Bank:
    def __init__(self):
        self.name = None 
        self.surname = None 
        self.age = None 
        self.balance = None 
        self.wallet_id = None 
        self.email = None 

    def register(self, name, surname, age, email):
        cursor = connection.cursor()
        cursor.execute(f"""INSERT INTO clients (name, surname, age, balance, wallet_id, email) 
                       VALUES ('{name}', '{surname}', {age}, 0, 'qwerty', '{email}');""")
        cursor.connection.commit()
        print(f"Уважаемый {name} {surname} вы успешно создали счет в нашем банке")

    def authorization(self, name, email):
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM clients WHERE name = '{name}' AND email = '{email}';")
        result = cursor.fetchall()
        self.name = result[0][0]
        self.surname = result[0][1]
        self.age = result[0][2]
        self.balance = result[0][3]
        self.wallet_id = result[0][4] 
        self.email = result[0][5]
        print(f"{self.name} {self.surname} вы успешно авторизовались") 

    def main(self):
        while True:
            command = input("1 - регистрация, 2 - авторизация, 3 - информация, 4 - пополнить, 5 - вывести: ")
            if command == "1":
                name = input("Имя: ")
                surname = input("Фамилия: ")
                age = int(input("Возраст: "))
                email = input("Почта: ")
                self.register(name, surname, age, email)
            elif command == "2":
                name = input("Имя: ")
                email = input("Почта: ")
                self.authorization(name, email)

optima = Bank()
optima.main()
