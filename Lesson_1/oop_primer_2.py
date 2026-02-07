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

    def stop(self):
        """Выводит сообщение об остановке транспортного средства."""
        print(f"{self.brand} {self.model} остановился.")


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
        self.current_charge = 0  # Текущий заряд батареи в %

    def charge(self, percentage):
        """
        Заряжает батарею на заданный процент.

        Аргументы:
            percentage (int): Процент зарядки.
        """
        if self.current_charge + percentage > 100:
            self.current_charge = 100
        else:
            self.current_charge += percentage
        print(f"{self.brand} {self.model} заряжен на {self.current_charge}%.")

    def range(self):
        """Выводит предполагаемый запас хода на текущем заряде."""
        estimated_range = self.battery_capacity * (self.current_charge / 100) * 5  # 5 км на 1 кВт/ч
        print(f"{self.brand} {self.model} может проехать примерно {estimated_range:.2f} км на текущем заряде.")


class HybridCar(Vehicle):
    """
    Класс, представляющий гибридный автомобиль (наследует Vehicle).

    Атрибуты:
        brand (str): Марка автомобиля.
        model (str): Модель автомобиля.
        fuel_capacity (int): Ёмкость топливного бака в литрах.
        battery_capacity (int): Ёмкость батареи в кВт/ч.
    """

    def __init__(self, brand, model, fuel_capacity, battery_capacity):
        """
        Инициализация объекта класса HybridCar.

        Аргументы:
            brand (str): Марка автомобиля.
            model (str): Модель автомобиля.
            fuel_capacity (int): Ёмкость топливного бака в литрах.
            battery_capacity (int): Ёмкость батареи в кВт/ч.
        """
        super().__init__(brand, model)
        self.fuel_capacity = fuel_capacity
        self.battery_capacity = battery_capacity
        self.current_fuel = 0  # Текущий уровень топлива в литрах
        self.current_charge = 0  # Текущий заряд батареи в %

    def refuel(self, liters):
        """
        Заправляет автомобиль на заданное количество литров.

        Аргументы:
            liters (int): Количество литров для заправки.
        """
        if self.current_fuel + liters > self.fuel_capacity:
            self.current_fuel = self.fuel_capacity
        else:
            self.current_fuel += liters
        print(f"{self.brand} {self.model} заправлен на {self.current_fuel} литров.")

    def charge(self, percentage):
        """
        Заряжает батарею на заданный процент.

        Аргументы:
            percentage (int): Процент зарядки.
        """
        if self.current_charge + percentage > 100:
            self.current_charge = 100
        else:
            self.current_charge += percentage
        print(f"{self.brand} {self.model} заряжен на {self.current_charge}%.")

    def range(self):
        """Выводит предполагаемый запас хода на текущем заряде и уровне топлива."""
        electric_range = self.battery_capacity * (self.current_charge / 100) * 5  # 5 км на 1 кВт/ч
        fuel_range = self.current_fuel * 15  # 15 км на 1 литр топлива
        total_range = electric_range + fuel_range
        print(f"{self.brand} {self.model} может проехать примерно {total_range:.2f} км на текущем заряде и топливе.")


# Тестирование классов
if __name__ == "__main__":
    # Электромобиль
    my_electric_car = ElectricCar("Tesla", "Model S", 100)
    my_electric_car.drive()
    my_electric_car.charge(50)
    my_electric_car.range()

    print("\n")

    # Гибридный автомобиль
    my_hybrid_car = HybridCar("Toyota", "Prius", 40, 20)
    my_hybrid_car.drive()
    my_hybrid_car.refuel(20)
    my_hybrid_car.charge(80)
    my_hybrid_car.range()