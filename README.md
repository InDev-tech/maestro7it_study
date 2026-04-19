# Объектно-Ориентированное Программирование (ООП)

## Основные понятия ООП

### Что такое ООП?

`ООП (Объектно-Ориентированное Программирование)` — это парадигма программирования, в которой программа представляется как набор взаимодействующих объектов, каждый из которых является экземпляром определенного класса.

Можно представить это как создание виртуальных "предметов" со своими свойствами и возможностями, которые взаимодействуют друг с другом.

## Основные принципы ООП

### 1. Инкапсуляция

**Определение:** Скрытие внутренней реализации объекта и предоставление контролируемого доступа к данным.

**Преимущества:**

- Защита данных от несанкционированного доступа
- Упрощение использования объектов
- Повышение безопасности кода

**Пример:**

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Приватный атрибут
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def get_balance(self):
        return self.__balance
```

### 2. Наследование

**Определение:** Механизм создания нового класса на основе существующего, при котором новый класс перенимает свойства и методы родительского класса.

**Преимущества:**

- Переиспользование кода
- Создание иерархий классов
- Полиморфизм

**Пример:**

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"
```

### 3. Полиморфизм

**Определение:** Возможность объектов разных классов использовать одинаковый интерфейс, но иметь разную реализацию.

**Типы полиморфизма:**

- **Ad-hoc полиморфизм** (перегрузка функций)
- **Параметрический полиморфизм** (дженерики)
- **Подтипизация** (наследование)

**Пример:**

```python
def make_sound(animal):
    print(animal.speak())

dog = Dog("Buddy")
cat = Cat("Whiskers")

make_sound(dog)  # Buddy says Woof
make_sound(cat)  # Whiskers says Meow
```

### 4. Абстракция

**Определение:** Выделение существенных характеристик объекта и игнорирование несущественных деталей.

**Преимущества:**

- Упрощение сложных систем
- Сокрытие деталей реализации
- Повышение читаемости кода

## Классы и Объекты

### Класс

`Класс` — это шаблон или чертеж для создания объектов.

**Он определяет:**

- Атрибуты (свойства)
- Методы (поведение)
- Конструкторы

### Объект

Объект — это экземпляр класса, созданный по шаблону класса.

**Пример:**

```python
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_running = False
    
    def start_engine(self):
        self.is_running = True
        print(f"{self.brand} {self.model} engine started")
    
    def stop_engine(self):
        self.is_running = False
        print(f"{self.brand} {self.model} engine stopped")

# Создание объектов
my_car = Car("Toyota", "Camry", 2023)
your_car = Car("Honda", "Civic", 2022)
```

## Модификаторы доступа

### В Python:

- **Публичные** (`public`): Доступны из любого места
- **Защищенные** (`protected`): Обозначаются префиксом `_` *(соглашение)*
- **Приватные** (`private`): Обозначаются префиксом `__` *(name mangling)*

### В других языках (Java, C++, C#):

- `public` — доступен всем
- `protected` — доступен в классе и подклассах
- `private` — доступен только внутри класса
- `internal` — доступен в пределах сборки (C#)

## Композиция vs Наследование

### Наследование ("is-a" отношение)

```python
class Vehicle:
    def move(self):
        pass

class Car(Vehicle):  # Car является Vehicle
    pass
```

### Композиция ("has-a" отношение)

```python
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()  # Car имеет Engine
    
    def start(self):
        self.engine.start()
```

## SOLID принципы

### 1. Single Responsibility Principle (SRP)

Класс должен иметь только одну причину для изменения.

### 2. Open/Closed Principle (OCP)

Классы должны быть открыты для расширения, но закрыты для модификации.

### 3. Liskov Substitution Principle (LSP)

Объекты в программе должны быть заменяемыми на экземпляры их подтипов без изменения правильности выполнения программы.

### 4. Interface Segregation Principle (ISP)

Клиенты не должны зависеть от интерфейсов, которые они не используют.

### 5. Dependency Inversion Principle (DIP)

Зависимости должны строиться относительно абстракций, а не деталей.

## Практические примеры

### Пример №1: Система управления библиотекой

```python
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        self.books.append(book)
    
    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn and not book.is_borrowed:
                book.is_borrowed = True
                return f"Book '{book.title}' borrowed successfully"
        return "Book not available"
```

### Пример №2: Система платежей

```python
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing credit card payment of ${amount}"

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount):
        return f"Processing PayPal payment of ${amount}"
```

## Преимущества ООП

1. **Модульность** — код организован в отдельные, независимые блоки
2. **Повторное использование** — наследование и композиция
3. **Расширяемость** — легкость добавления новых функций
4. **Поддерживаемость** — чистая структура и четкие интерфейсы
5. **Безопасность** — инкапсуляция защищает данные

## Недостатки ООП

1. **Сложность** — может быть избыточной для простых задач
2. **Производительность** — накладные расходы на создание объектов
3. **Кривая обучения** — требуется время для освоения концепций
4. **Чрезмерное использование** — не все задачи требуют `ООП` подхода

## Когда использовать ООП?

✅ **Использовать, когда:**

- Моделируете реальные объекты и сущности
- Нужна повторная используемость кода
- Работаете с большими, сложными системами
- Требуется четкая структура и архитектура

❌ **Не использовать, когда:**

- Решаете простые алгоритмические задачи
- Пишете скрипты для одноразового использования
- Работаете с функциональной логикой
- Производительность критична

## Заключение

`ООП` — мощная парадигма программирования, которая помогает создавать гибкие, расширяемые и поддерживаемые приложения.

Понимание основных принципов ООП необходимо для любого разработчика, стремящегося писать качественный код.

**Ключевые моменты для запоминания:**

- Инкапсуляция, наследование, полиморфизм, абстракция
- `SOLID` принципы
- Правильный выбор между наследованием и композицией
- Баланс между простотой и сложностью

---

### 🏫 О школе

[![Website](https://img.shields.io/badge/Maestro7IT-school--maestro7it.ru-darkgreen?style=for-the-badge)](https://school-maestro7it.ru/)

> Инновационная школа программирования, специализирующаяся на подготовке специалистов в области современных технологий и языков программирования.

---

💼 **Преподаватель:** Дуплей Максим Игоревич

📲 **Telegram №1:** [@quadd4rv1n7](https://t.me/quadd4rv1n7)

📲 **Telegram №2:** [@dupley_maxim_1999](https://t.me/dupley_maxim_1999)

📅 **Дата:** 07.02.2026


Пузырьковая сортировка
Сортировка вставками
