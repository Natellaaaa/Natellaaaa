class Student:

    def __init__(self, name):
        self.name = name
        self.books = []
        self.knowledge = 0
        self.is_ready_to_work = False
        self.languages = {}


    def info(self):
        return f"Имя: {self.name}, Очки: {self.knowledge}, Языки программирования: {self.languages}, Готовность к работе: {self.is_ready_to_work}"


    def read_book(self, book):
        self.books.append(book)
        self.__add_points(100)
        return f"Книга '{book}' добавлена в список, 100 очков"


    def do_homework(self):
        self.__add_points(10)
        return f"Добавлено 10 очков"


    def do_project(self):
        self.__add_points(50)
        return f"Добавлено 50 очков"


    def __add_points(self, points):
        self.knowledge += points
        if self.knowledge >= 1000:
            self.is_ready_to_work = True
            return f"Cтудент готов к работе"


    def learn_new_language(self, language, points):
        if points < 1 and points >100:
            return f"Знание должно быть в диапазоне от 1 до 100"
        self.languages[language] = points
        return f"Изучен язык '{language}' на {points}%"


Natella = Student("Натэлла")
print(Natella.info())
print(Natella.read_book("Python"))
print(Natella.do_homework())
print(Natella.do_project())
print(Natella.learn_new_language("Java",72 ))
print(Natella.learn_new_language("Kotlin", 25))
print(Natella.info())
print(Natella.read_book("Python"))
print(Natella.read_book("Python"))
print(Natella.read_book("Python"))
print(Natella.read_book("Python" ))
print(Natella.read_book("Python"))
print(Natella.read_book("Python"))
print(Natella.read_book("Python"))
print(Natella.read_book("Python"))
print(Natella.read_book("Python"))
print(Natella.read_book("Python"))
print(Natella.info())