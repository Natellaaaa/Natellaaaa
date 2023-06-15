
# задание 1
for num in range(5):
    print(0, num) 

# Задание  2
list = []
for numbers in range(1,101):
    list.append(numbers)
print(list)

#задание 3
list = []
for chet_numbers in range(1,498):
    if chet_numbers %2 == 0:
        list.append(chet_numbers)
print(list)

# Задание 4
list = []
for i in range(1,1001):
    list.append(i)
print("Наименьшее число :" , min(list))
print("Наибольшее число:" , max(list))
print("Общая сумма:", sum(list))

#Задание 5
list = []
for i in range(1,101):
    null = 0
    if i >= 1 and i <= 100:
        list.append(null)
print(list)

# Задание 6
it_company = ("Google", "Amazon", "Microsoft")
it_list = list(it_company)
it_list.append ("Tesla")
print (it_list)
it_kort = it_company + ("Tesla", )
print(it_kort)

# Задание 7
it_company = ("Google", "Amazon", "Microsoft")
print(it_company[1])

# Задание 8
it_company = ("Google", "Amazon", "Microsoft")
it_list = list(it_company)
it_list [0] = "Apple"
print (it_list)

# Задание 9
it_company = ("Google", "Amazon", "Microsoft")
it_list = list(it_company)
it_list [0] = "Apple"
print (it_list [0:2])

#задание 10
text_tuple = ('Experienced', 'programmers', 'in', 'any', 'other', 'language',
'can', 'pick', 'up', 'Python', 'very', 'quickly,', 'and', 'beginners', 'find', 'the', 'clean', 'syntax', 'and',
'indentation', 'structure', 'easy', 'to', 'learn.', 'Whet', 'your', 'appetite', 'with', 'our', 'Python', '3',
'overview')
count = text_tuple.count ('Python')
print ("Количество повторений слова Python: ", count)

# задание 11
num1 = 10
num2 = 20
print("Значение num1 = 10 а значение num2 = 20")
question = int(input("Чему равно num1?:" ))
if question == num1:
    print("Значение num1 = 20 а значение num2 = 10")
    question = int(input("Чему равно num1?:" ))
    if question == num2:
        print("Значение num1 = 10 а значение num2 = 20")
        question = int(input("Чему равно num1?:" ))
    else:
        print("Ошибка")
else:
    print("Ошибка")

#задание 12
while True:
    age = int(input("Введите свой возраст:" ))
    if age < 18:
        print("Иди отсюда если тебе нет 18")
    elif age >=18:
        print("Теперь можно")
        break      
    