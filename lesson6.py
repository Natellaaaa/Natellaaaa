# def welcome():
#     name = input("Name:")



# def calculator():
#     num1 = int(input("Number1 :"))
#     operator = input("+ , - , *, /:") 
#     num2 = int(input("Number2 :"))
#     if operator == "+":
#         print(f"Result {num1 + num2}")
#     elif operator == "-":   
#         print(f"Result {num1 - num2}") 
#     elif operator == "*":
#         print(f"Result {num1 * num2}")
#     elif operator == "/":   
#         print(f"Result {num1 / num2}") 
#     else:
#         print("Error operator")    
# calculator()




# def add(num1 , num2):    #num1 , num2  являются параметрами функции add
#     print(num1 + num2)
# add(10,56)      #значения 10 и 56 являются аргументами

# def mult(num1 : int , num2 : int):
#     print(num1 * num2)
# mult("geeks ", 7)    

# def sub(num1:int, num2:int)  -> int:
#     print(num1 - num2) 
# sub(20,89)

# def div(num1 :int=1, num2:int=1)-> float:
#     "Данная функция принемет два числа и делит их"
#     print(num1 / num2)
# div()


# import random


# def generator_password(len_password:int=8)-> str:
#     letters = "qwertyuiopasdfghjklzxcvbnm1234567890"
#     result = ""
#     for n in range(len_password):
#         random_letters = random.choice(letters)
#         result += random_letters
#     print(result)
# generator_password(1)    


# #исключения try , except
# try:
#     print(10 / 0)
# except ZeroDivisionError:
#     print("На ноль делить нельзя")    


# try :
#     print("10"+ 3)
# except TypeError:
#     print("Ошибка типов данных")



# raise ValueError("Hello Geeks")




