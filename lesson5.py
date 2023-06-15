#Множества (set, frozenset)
# a = [1, 2, 3, 4, 5]
# b = [3, 4, 5, 6, 7]
# print(set(a + b))

# st = {'Geeks','Bishkek', 'Osh','IT','Osh' }
# print(st)

# st.add('Asus')
# print(st)
# st.remove('IT')
# print(st)
# st.pop()
# print(st)
# st.clear()
# print(st)

# emails = {'geeks@gmail.com'}
# print(emails)
# emails.add('dvalishvilinatella@gmail.com')
# print(emails)
# emails.add('Geeks@gmail.com')
# print(emails)
# emails.add(1)
# emails.add("1")
# print(emails)


# frzn = frozenset({1,1,2,2,3,4})
# print(frzn)

#Словари
# student = {'name':'Askat',
#   'age': 19,
#   'phone_number': 9965525356
#   }
# print(student)
# print(student['name'])
# print(student['phone_number'])
# student.setdefault('language','Python')
# print(student)
# student.pop('phone_number')
# print(student)

# student['age'] = 20
# print(student)

# print(student.keys())
# print(student.values())

# contacs = {"MCHS": 112}
# while True:
#     comands = input("1-просмотреть, 2 - добавить,3 - удалить , 4 -обнавить:" )
#     if comands == "1":
#         print(contacs)
#     elif comands == "2":
#         add_name = input("введите имя которое нужно добавить :")
#         if add_name in contacs:
#             print("Такой контакт уже существует")
#         add_number = input("ВВедите номер который нужно добавить:")
#         contacs.setdefault(add_name,add_number)
#         print(f"Контакт {add_name} успешно дабавлен")
#     elif comands == "3":
#         delete_name = input("введите имя которе хотите удалить:")
#         if delete_name in contacs:
#             contacs.pop(delete_name)
#         print(f"Контакт{delete_name} успешно удален")
#       но обнавить?")

#             new_number = input("введите новый номер:")
#             contacs[updates_number] = new_number
#             print(f"Контакт {update_number} успешно обнавлен ")
#         else:
#             print("Такого контакта нет")
            




