# def hello_student(*names):
#     for name in names:
#         print("Hi" , names)



# def avg(object:list)->int:
#     "Вычесляет среднее арифмеьтческое значенте из списка и кортежей"        
#     print(sum(object) / len(object)


# def reverse_word(word:str)->str:
#     "Переворачивает строку"
#     print(word[::-1])

# it = "Geeks"

#Работа с файлами

# f = open('geeks.txt ', "w")
# f.write("Hello Geeks Backend 09!")
# f.close()
# r = open('geeks.txt', 'r')
# print(r.read())
# r.close()

# py = open('Hello.py', 'w')
# py.write("print('hello world')")
# py.close()


# read_py = open('lesson2.py' , 'r', encording = 'utf-8')
# print(read_py.read())
# read_py.close() 

# import os 
# # os.remove()
# # os.mkdir("C:/Users/user/Desktop/gggggg")

# n = 0
# while True:
#     n+= 1
#     os.mkdir(f"C:/Users/user/Desktop/test/hello{n}")
#     if n == 10:
#         break



# with open('hello.txt', 'w' , encording = 'utf-8') as hello:
#     hello.write("Hello world")


# with open('hello.txt', 'r') as read_file:
#     print(read_file.read())


# with open('rus.txt', 'w' ) as rus:
#     rus.write("Привет мир и гикс!")



with open('students.txt', 'w' , encording ='utf-8') as students:
    students.write("Islam\n")
    students.write("Robert\n")
    
with open('students.txt', 'w' , encording='utf-8') as nem_students:    
    new_student.write("Natella\n") 
   
