#Циклы  for & while





for i in range(100): 
    print("Hello world", i) 

# for n in  range(101):
#     print(n)
#     print(("Geeks"))

# for day in range(1,32):
#     print("Утро") 
#     print("Деня ", day)
#     print("Ночь")
#     print("========")


# number = int(input("Number : "))
# if number % 2 == 0 :
#     print(number , "четное")
# else : 
#     print(number , "нечетное")    


chet_numbers = []
for numbers in range(2, 101, 2):
    chet_numbers.append(numbers)
print(chet_numbers)

# numbers = [12, 2, 1002, 345, 3, 6, 454, 75, 87, 76, 6]
# chet = []
# for num in numbers : #Итерация списка numbers
#     if num % 2 == 0:
#         chet.append(num)
# print(chet)       


# letters = ["K", "D", "S", "P"]
# print(letters)
# for let in letters :
#     print(let) 



# num1 = 10
# num2 = 20
# while num1 < num2:
#     num1 += 1
#     print(num1)

# shet = 0
# while True:
#     shet += 1
#     print(shet) 

# n = 0 
# while True:
#     n += 12
#     print(n)
#     if n == 10004 :
#         print("Hacked!!")
#         break 

# import time 

# k = 0 
# while True :
#     k += 10
#     print("Hack", k, "%")
#     if k == 100:
#         print("Hack system")
#         break
#     time.sleep(5)





# import random 

# # print(random.randint(1, 10))
# random_number = random.randint(1, 10)
# attempts = 5
# while True : 
#     user_number  = int(input("Введите число от 1 до 10 :")) 
#     if user_number >= 1 and user_number <= 10: 
#         attempts -= 1
#         if user_number == random_number :
#             print("Win")
#     elif attempts == 0 :
#         print("Loose")     
#         break
#     else:
#         print("Wrong answer", attempts , "attempts") 


