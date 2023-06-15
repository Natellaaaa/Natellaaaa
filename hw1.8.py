#Задача 1
import random

def random_language(languages):
    random_language = random.choice(languages)
    with open("languages.txt", "w", encoding = 'utf-8') as text_file:
        text_file.write(random_language)
random_language(languages=["Python", "Java", "Kotlin", "JavaScript", "C#", "Ruby"])

#Задача 2
text = ("Lorem Ipsum is simply dummy text of the printing and typesetting industry.\n\
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,\n\
when an unknown printer took a galley of type and scrambled it to make a type specimen book.\n\
It has survived not only five centuries, but also the leap into electronic typesetting,\n\
remaining essentially unchanged. It was popularized in the 1960s with the release of \n\
Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing\n\
software like Aldus PageMaker including versions of Lorem Ipsum.")
with open("text.txt", "w") as file:
    file.write(text)

#Задача 3
text =("Lorem Ipsum is simply dummy text of the printing and typesetting industry.\n\
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,\n\
when an unknown printer took a galley of type and scrambled it to make a type specimen book.\n\
It has survived not only five centuries, but also the leap into electronic typesetting,\n\
remaining essentially unchanged. It was popularized in the 1960s with the release of \n\
Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing\n\
software like Aldus PageMaker including versions of Lorem Ipsum.")
file = open("text2.txt", "w")
file.write(text)
file.close()

#Дополнительное задание
with open("text2.txt", "r") as copy:
    text = copy.read()
with open("wikipedia.txt", "w") as paste:
    paste.write(text)