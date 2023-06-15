#Args, kwargs. Lambda функции
# def students(name1 , name2 , name3):
#     print("Hi", name1)
#     print("hi",name2)
#     print("hi", name3)
# students("Nurislam", "Nurbolot", "Robert") 

# def args_students(*args):
#     # print(args)
#     for name in args:
#         print("Hi", name)
# # args_students("Natella", "Amora", "Rimma")

# def students_points(name:str, *points:int) -> str:
#     print(name, sum(points) / len(points))
# # students_points("Natella", 4, 4, 5, 5, 3, 4, 2, 3)


# def translate(**words):
#     print(words)
# # translate(USA="США",  Apple="Яблоко", Bus = "автобус") 





# def agg(num1:int=1,num2:int=1) ->int:
#     print(num1 +num2)

# def sub(num1:int=1, num2:int= 2)-> int:
#     print(num1-num2)

# def mult(num1:int=1, num2:int=1)->int:
#     print(num1*num2)

# def div(num1:int=1, num2:int=1) ->float:
#     try:
#         print(num1 / num2)
#     except ZeroDivisionError:
#         print("на ноль делить нельзя")

# def main(number1:int = 1, number2:int=2,operator:str = "+") -> int:
#     if operator == "+":
#         add(number1,number2)
#     elif  operator =="-":
#         sub(number1, number2) 
#     elif operator == "*":
#         mult(number1,number2) 
#     elif operator =="/":
#         div(number1, number2)
#     else:
#         print("Такого оператора нету , пожайлуста используйте +, -, *, / ")    
# # main(234, 56 , "-")            
# # main(3 , 0 ,"/")

# #Limbda  - функция
# def hello(word):
#     print(word)
# hello("Geeks")

# lambda_hello = lambda word: word
# print(lambda_hello("geeks"))

# print((lambda word: word)("geeks"))


# #ex 2
# def add(num1:int=1, num2:int=1):
#     print(num1 + num2)
# add(91432 , 7834)  


# lambda_add = lambda num1 , num2: num1 + num2
# print(lambda_add(108, 3984))

# print((lambda num1 , num2:num1 +num2)(208, 84))

# #ex 3
# f = lambda: True #limbda функция без аргументов 
# print(f())


# #ex 4
# numbers = [1, 2, 3, 4, 5]
# new_numbers = []
# def mult_two(nums:list)->list:
#     for n in nums:
#         new_numbers.append(n*2)
#     print(new_numbers)
# mult_two(numbers)        

# numbers = [1, 2, 3, 4, 5, 6]
# lambda_new_numbers = list(map(lambda nums:nums*2,numbers))
# print(lambda_new_numbers)

# numbers = [1, 2, 3, 4, 5, 6]
# # print(list(map(lambda nums:nums*2,numbers))) 

# # print(list(map(lambda nums:nums*2,[1, 2, 3, 4, 5, 6])))


# #ex5

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
# chet = []
# def numbers_chet(nums:list)->list:
#     for n in nums:
#         if n % 2 == 0:
#             chet.append(n)
#         print(chet)
# # numbers_chet(numbers)            

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]

# lambda_numbers_chet=list(filter(lambda nums:nums % 2 == 0, numbers))
# # print(lambda_numbers_chet)



# # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]

# print(list(filter(lambda nums:nums % 2 == 0, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))


from lesson8 import reverse_word
reverse_word("Natella")

