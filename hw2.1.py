# Задание 1
class Cow():
    def make_sound(sound):
        return f"{sound}"
print (Cow.make_sound("Мууу!"))

# Задание 2
class Cars:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model = model
        self.year = year
        self.odometr = 0
        self.is_going = False

    def info_about_car (self):
        return f"{self.brand}, {self.model},{self.year}."
    
    def car_is_going(self,km):
        if self.is_going == False:
            self.is_going = True
            self.odometr += km
        return f"машина едет, {km} km"
    
    def car_not_going(self):
        if self.is_going == True:
            self.is_going = False
        return f"машина не едет" 

tesla = Cars("Tesla", "Model-3", 2018,)
print(tesla.info_about_car())
print(tesla.car_is_going(180))
print(tesla.car_not_going())

# Задание 3
class Airplane:
    def __init__(self,make, model, year, max_speed,):
        self.make = make
        self.model = model
        self.year = year
        self.max_speed = max_speed
        self.odometr = 0
        self.is_flying = False
        self.land = True

    def info(self):
        return f"{self.make}, {self.model}, {self.year}, {self.max_speed}."
    
    def take_off(self):
        if self.is_flying == False:
            self.is_flying = True
        elif self.land == True:
             self.land = False
        return f"Самолёт взлетает"
        
    def fly(self,km):
        if self.is_flying == True and self.land == False:
            self.odometr += km
            return f"Самолёт взлетел на рейс Ош-Бишкек  {km} km"
        
plane = Airplane("Airbus", "319", "2001", "890 км/ч")
print(plane.info())
print(plane.take_off())
print(plane.fly(300))


# Задание 4
class Math:
    
    def addition(a, b):
        result = a + b
        print(f"{a} + {b} = {result}")
    
    def multiplication(a, b):
        result = a * b
        print(f"{a} * {b} = {result}")
    
    def division(a, b):
        result = a / b
        print(f"{a} / {b} = {result}")
    
    def substraction(a, b):
        result = a - b
        print(f"{a} - {b} = {result}")
        
Math.addition(10, 5)
Math.multiplication(10, 5)
Math.division(10, 5)
Math.substraction(10, 5)

