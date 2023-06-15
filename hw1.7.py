# Задание 1
def hello(x):
    print(x * x - 10)
hello()

print(list(map(lambda x: x * x - 10, [None])))

# Задание 2
name = ["Kuma", "Nurtilek", "Zina", "Edzen", "Kuma", "Aitenur", "Zina"]
print(list(map(lambda names: names, set(name))))

# Задание 3
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(lambda x: x % 2 == 0, numbers)))

# Задание 4
names = ["azat", "zina", "kuma", "anna", "sas"]
print(list(filter(lambda name: name == name[::-1], names)))

# Дополнительное задание
time1 = input("Введите первую отметку времени (в формате ЧЧ:ММ:СС): ")
time2 = input("Введите вторую отметку времени (в формате ЧЧ:ММ:СС): ")
time1 = time1.split(":")
time2 = time2.split(":")
time1 = int(time1[0]) * 3600 + int(time1[1]) * 60 + int(time1[2])
time2 = int(time2[0]) * 3600 + int(time2[1]) * 60 + int(time2[2])
print(time2 - time1)


list = [ 1, 2, 3, 4]
print(list)