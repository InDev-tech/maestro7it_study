class Car:
    """
    Класс, представляющий обычный автомобиль.

    Атрибуты:
        brand (str): Марка автомобиля.
        model (str): Модель автомобиля.
        year (int): Год выпуска автомобиля.
    """

    def __init__(self, brand, model, year):
        """
        Инициализация объекта класса Car.

        Аргументы:
            brand (str): Марка автомобиля.
            model (str): Модель автомобиля.
            year (int): Год выпуска автомобиля.
        """
        self.brand = brand
        self.model = model
        self.year = year

    def drive(self):
        """Выводит сообщение о движении автомобиля."""
        print(f"{self.brand} {self.model} едет.")


class Vehicle:
    """
    Класс, представляющий транспортное средство.

    Атрибуты:
        brand (str): Марка транспортного средства.
        model (str): Модель транспортного средства.
    """

    def __init__(self, brand, model):
        """
        Инициализация объекта класса Vehicle.

        Аргументы:
            brand (str): Марка транспортного средства.
            model (str): Модель транспортного средства.
        """
        self.brand = brand
        self.model = model

    def drive(self):
        """Выводит сообщение о движении транспортного средства."""
        print(f"{self.brand} {self.model} едет.")


class ElectricCar(Vehicle):
    """
    Класс, представляющий электрический автомобиль (наследует Vehicle).

    Атрибуты:
        brand (str): Марка автомобиля.
        model (str): Модель автомобиля.
        battery_capacity (int): Ёмкость батареи в кВт/ч.
    """

    def __init__(self, brand, model, battery_capacity):
        """
        Инициализация объекта класса ElectricCar.

        Аргументы:
            brand (str): Марка автомобиля.
            model (str): Модель автомобиля.
            battery_capacity (int): Ёмкость батареи в кВт/ч.
        """
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    def charge(self):
        """Выводит сообщение о начале зарядки автомобиля."""
        print(f"{self.brand} {self.model} заряжается на {self.battery_capacity} кВт/ч.")

    def calculate_charge_time(self, charge_percentage, charge_rate):
        """
        Рассчитывает время зарядки автомобиля до указанного процента.

        Аргументы:
            charge_percentage (int): Процент зарядки (от 0 до 100).
            charge_rate (int): Скорость зарядки в кВт/ч.

        Возвращает:
            float: Время зарядки в часах.
        """
        if charge_rate <= 0:
            raise ValueError("Скорость зарядки должна быть больше нуля.")

        energy_needed = (self.battery_capacity * charge_percentage) / 100
        charge_time = energy_needed / charge_rate
        return charge_time


# Создание объекта класса ElectricCar
my_electric_car = ElectricCar("Tesla", "Model S", 100)

# Демонстрация функциональности
my_electric_car.drive()  # Tesla Model S едет
my_electric_car.charge()  # Tesla Model S заряжается на 100 кВт/ч

# Расчёт времени зарядки
charge_percentage = 50  # Процент зарядки
charge_rate = 22  # Скорость зарядки в кВт/ч

charge_time = my_electric_car.calculate_charge_time(charge_percentage, charge_rate)
print(f"Для зарядки {charge_percentage}% батареи потребуется {charge_time:.2f} часов при скорости {charge_rate} кВт/ч.")