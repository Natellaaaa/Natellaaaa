class Washer:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        self.powder = 0
        self.iswork = False

    def __str__(self):
        return f"Бренд: {self.brand}, Цвет: {self.color}"

    def start(self):
        if self.powder < 20:
            return "Не хватает порошка"
        self.iswork = True
        self.powder -= 20
        return f"Началась стирка"
    
    def refuel(self):
        if self.powder >= 100:
            return "В стиралку можно положить только 100 грамм порошка"
        self.powder += 100
        return f"Стиральная машинка заправлена"

    def finish(self):
        self.iswork = False
        return "Стиральная машинка отключена"

    def main(self):
        while True:
            commands = input("1 - Информация, 2 - Начало стирки, 3 - Заправка порошка, 4 - Финиш :")
            if commands == "1":
                print(indesit)
            elif commands == "2":
                print(indesit.start())
            elif commands == "3":
                print(indesit.refuel())
            elif commands == "4":
                print(indesit.finish())
                break
        return f"До свидания!"
               


indesit = Washer("Indesit", "Белая")
print(indesit.main())
