#!/usr/bin/env python3
"""
╔═══════════════════════════════════════════════════════════════════════════════╗
║                         sorting_animation.py                                  ║
║                                                                               ║
║  A comprehensive sorting algorithm animation with visual feedback.            ║
║  Sorts a shelf of 10 blocks using multiple sorting algorithms.                ║
║                                                                               ║
║  Author: Dupley Maxim Igorevich - AGLA                                        ║
║  ORCID:  https://orcid.org/0009-0007-7605-539X                                ║
║  GitHub: https://github.com/QuadDarv1ne/                                      ║
║  Date:   19.04.2026                                                           ║
║                                                                               ║
║  Implemented algorithms:                                                      ║
║    • Bubble Sort      (b)    • Shell Sort      (h)                            ║
║    • Insertion Sort   (i)    • Cocktail Sort   (c)                            ║
║    • Selection Sort   (s)    • Merge Sort      (m)                            ║
║    • Quicksort        (q)                                                    ║
║                                                                               ║
║  Color indicators:                                                            ║
║    🟠 Orange  — element being examined/comparing                               ║
║    🟣 Purple  — element being moved/swapped                                    ║
║    ⚫ Black   — normal state                                                   ║
║                                                                               ║
║  Controls:                                                                    ║
║    SPACE — quit                     R — randomize array                       ║
║                                                                               ║
║  Shelfs are implemented using built-in lists.                                 ║
║  Blocks are turtles with shape "square", stretched to rectangles.             ║
║                                                                               ║
╚═══════════════════════════════════════════════════════════════════════════════╝
"""
from turtle import *
import random
import time


class Block(Turtle):
    """
    Визуальный блок для анимации сортировки.
    
    Каждый блок представляет собой прямоугольник, высота которого
    пропорциональна значению размера (size).
    """
    
    def __init__(self, size):
        self.size = size
        Turtle.__init__(self, shape="square", visible=False)
        self.pu()
        self.shapesize(size * 1.5, 1.5, 2)  # square → rectangle
        self.fillcolor("black")
        self.st()

    def glow_examining(self):
        """Подсветка оранжевым — элемент рассматривается/сравнивается"""
        self.fillcolor("orange")

    def glow_moving(self):
        """Подсветка фиолетовым — элемент перемещается/меняется"""
        self.fillcolor("purple")

    def unglow(self):
        """Возврат к нормальному цвету (чёрный)"""
        self.fillcolor("black")

    def __repr__(self):
        return f"Block(size={self.size})"


class Shelf(list):
    """
    Полка для хранения и визуализации блоков.
    
    Управляет позиционированием блоков по оси X и Y,
    а также анимацией их перемещения.
    """
    
    def __init__(self, y):
        """
        Создание полки.
        
        Args:
            y (int): Y-координата первого блока (нижняя граница)
        """
        self.y = y
        self.x = -150

    def push(self, d):
        """Добавление блока на полку с правильным позиционированием"""
        width, _, _ = d.shapesize()
        # align blocks by the bottom edge
        y_offset = width / 2 * 20
        d.sety(self.y + y_offset)
        d.setx(self.x + 34 * len(self))
        self.append(d)

    def _close_gap_from_i(self, i):
        """Сдвиг блоков влево для закрытия промежутка"""
        for b in self[i:]:
            xpos, _ = b.pos()
            b.setx(xpos - 34)

    def _open_gap_from_i(self, i):
        """Сдвиг блоков вправо для открытия промежутка"""
        for b in self[i:]:
            xpos, _ = b.pos()
            b.setx(xpos + 34)

    def pop(self, key):
        """Извлечение блока с анимацией подъёма и подсветкой"""
        b = list.pop(self, key)
        b.glow_moving()
        b.sety(200)
        self._close_gap_from_i(key)
        return b

    def insert(self, key, b):
        """Вставка блока с анимацией опускания"""
        self._open_gap_from_i(key)
        list.insert(self, key, b)
        b.setx(self.x + 34 * key)
        width, _, _ = b.shapesize()
        # align blocks by the bottom edge
        y_offset = width / 2 * 20
        b.sety(self.y + y_offset)
        b.unglow()

    def swap(self, i, j):
        """
        Обмен двух элементов местами с анимацией подъёма и опускания.
        
        Args:
            i (int): Индекс первого элемента
            j (int): Индекс второго элемента
        """
        if i == j:
            return
        
        # Подсвечиваем оба элемента фиолетовым
        self[i].glow_moving()
        self[j].glow_moving()
        
        # Анимация подъёма
        for _ in range(5):
            self[i].sety(self[i].ycor() + 4)
            self[j].sety(self[j].ycor() + 4)
            update()
            time.sleep(0.02)
        
        # Меняем позиции X
        xi = self[i].xcor()
        xj = self[j].xcor()
        self[i].setx(xj)
        self[j].setx(xi)
        
        # Меняем в списке
        self[i], self[j] = self[j], self[i]
        
        # Анимация опускания
        for _ in range(5):
            self[i].sety(self[i].ycor() - 4)
            self[j].sety(self[j].ycor() - 4)
            update()
            time.sleep(0.02)
        
        # Возвращаем цвет
        self[i].unglow()
        self[j].unglow()


# ═══════════════════════════════════════════════════════════════════════════════
#                          ALGORITHM IMPLEMENTATIONS
# ═══════════════════════════════════════════════════════════════════════════════

def bubble_sort(shelf):
    """
    Пузырьковая сортировка.
    
    Сложность: O(n²) в худшем и среднем случае, O(n) в лучшем.
    Память: O(1).
    """
    length = len(shelf)
    for i in range(length):
        swapped = False
        for j in range(0, length - i - 1):
            # Подсветка сравниваемых элементов
            shelf[j].glow_examining()
            shelf[j + 1].glow_examining()
            update()
            time.sleep(0.1)
            
            if shelf[j].size > shelf[j + 1].size:
                shelf.swap(j, j + 1)
                swapped = True
            
            shelf[j].unglow()
            shelf[j + 1].unglow()
        
        if not swapped:
            break


def insertion_sort(shelf):
    """
    Сортировка вставками.
    
    Сложность: O(n²) в худшем и среднем случае, O(n) в лучшем.
    Память: O(1).
    """
    length = len(shelf)
    for i in range(1, length):
        hole = i
        
        # Подсветка текущего элемента
        shelf[i].glow_examining()
        update()
        time.sleep(0.1)
        
        while hole > 0 and shelf[i].size < shelf[hole - 1].size:
            shelf[hole - 1].glow_examining()
            update()
            time.sleep(0.1)
            shelf[hole - 1].unglow()
            hole = hole - 1
        
        shelf[i].unglow()
        shelf.insert(hole, shelf.pop(i))


def selection_sort(shelf):
    """
    Сортировка выбором.
    
    Сложность: O(n²) во всех случаях.
    Память: O(1).
    """
    length = len(shelf)
    for j in range(0, length - 1):
        imin = j
        shelf[j].glow_examining()
        
        for i in range(j + 1, length):
            shelf[i].glow_examining()
            update()
            time.sleep(0.05)
            
            if shelf[i].size < shelf[imin].size:
                if imin != j:
                    shelf[imin].unglow()
                imin = i
            else:
                shelf[i].unglow()
        
        if imin != j:
            shelf[imin].glow_moving()
            shelf.insert(j, shelf.pop(imin))
        
        shelf[j].unglow()
        if imin != j:
            shelf[imin].unglow()


def partition(shelf, left, right, pivot_index):
    """
    Разделение для быстрой сортировки (схема Ломуто).
    
    Returns:
        int: Новый индекс опорного элемента
    """
    pivot = shelf[pivot_index]
    pivot.glow_examining()
    update()
    time.sleep(0.1)
    
    shelf.insert(right, shelf.pop(pivot_index))
    store_index = left
    
    for i in range(left, right):
        shelf[i].glow_examining()
        update()
        time.sleep(0.05)
        
        if shelf[i].size < pivot.size:
            shelf.insert(store_index, shelf.pop(i))
            store_index = store_index + 1
        
        shelf[i].unglow()
    
    shelf.insert(store_index, shelf.pop(right))
    shelf[store_index].unglow()
    return store_index


def quick_sort(shelf, left, right):
    """
    Быстрая сортировка (рекурсивная).
    
    Сложность: O(n log n) в среднем, O(n²) в худшем.
    Память: O(log n) для стека вызовов.
    """
    if left < right:
        pivot_index = left
        pivot_new_index = partition(shelf, left, right, pivot_index)
        quick_sort(shelf, left, pivot_new_index - 1)
        quick_sort(shelf, pivot_new_index + 1, right)


def shell_sort(shelf):
    """
    Сортировка Шелла (улучшенная сортировка вставками).
    
    Сложность: зависит от выбора промежутков, обычно O(n log² n) или O(n^(3/2)).
    Память: O(1).
    """
    length = len(shelf)
    gap = length // 2
    
    while gap > 0:
        for i in range(gap, length):
            temp = shelf[i]
            temp.glow_examining()
            update()
            time.sleep(0.05)
            
            j = i
            while j >= gap:
                shelf[j - gap].glow_examining()
                update()
                time.sleep(0.05)
                
                if shelf[j - gap].size > temp.size:
                    shelf[j - gap].glow_moving()
                    shelf[j] = shelf[j - gap]
                    shelf[j].unglow()
                    shelf[j - gap].unglow()
                    j -= gap
                else:
                    shelf[j - gap].unglow()
                    break
            
            shelf[j] = temp
            temp.unglow()
        
        gap //= 2


def cocktail_sort(shelf):
    """
    Шейкерная сортировка (двунаправленная пузырьковая).
    
    Сложность: O(n²) в худшем случае, O(n) в лучшем.
    Память: O(1).
    """
    length = len(shelf)
    swapped = True
    start = 0
    end = length - 1
    
    while swapped:
        swapped = False
        
        # Проход слева направо
        for i in range(start, end):
            shelf[i].glow_examining()
            shelf[i + 1].glow_examining()
            update()
            time.sleep(0.05)
            
            if shelf[i].size > shelf[i + 1].size:
                shelf.swap(i, i + 1)
                swapped = True
            
            shelf[i].unglow()
            shelf[i + 1].unglow()
        
        if not swapped:
            break
        
        swapped = False
        end -= 1
        
        # Проход справа налево
        for i in range(end - 1, start - 1, -1):
            shelf[i].glow_examining()
            shelf[i + 1].glow_examining()
            update()
            time.sleep(0.05)
            
            if shelf[i].size > shelf[i + 1].size:
                shelf.swap(i, i + 1)
                swapped = True
            
            shelf[i].unglow()
            shelf[i + 1].unglow()
        
        start += 1


def merge(shelf, left, mid, right):
    """
    Слияние двух отсортированных подмассивов для merge sort.
    
    Args:
        left (int): Левая граница
        mid (int): Середина
        right (int): Правая граница
    """
    # Создаем временные подмассивы
    left_part = []
    right_part = []
    
    # Копируем элементы и поднимаем их для анимации
    for i in range(left, mid + 1):
        left_part.append(shelf[i])
        shelf[i].glow_moving()
        shelf[i].sety(100)
    
    for i in range(mid + 1, right + 1):
        right_part.append(shelf[i])
        shelf[i].glow_moving()
        shelf[i].sety(100)
    
    update()
    time.sleep(0.3)
    
    i = j = 0
    k = left
    
    # Слияние с анимацией
    while i < len(left_part) and j < len(right_part):
        left_part[i].glow_examining()
        right_part[j].glow_examining()
        update()
        time.sleep(0.1)
        
        if left_part[i].size <= right_part[j].size:
            shelf[k] = left_part[i]
            left_part[i].unglow()
            i += 1
        else:
            shelf[k] = right_part[j]
            right_part[j].unglow()
            j += 1
        
        shelf[k].sety(s.y)
        shelf[k].unglow()
        k += 1
    
    # Добавляем оставшиеся элементы
    while i < len(left_part):
        shelf[k] = left_part[i]
        shelf[k].sety(s.y)
        shelf[k].unglow()
        i += 1
        k += 1
    
    while j < len(right_part):
        shelf[k] = right_part[j]
        shelf[k].sety(s.y)
        shelf[k].unglow()
        j += 1
        k += 1
    
    # Выравниваем позиции X
    for idx in range(left, right + 1):
        shelf[idx].setx(s.x + 34 * idx)


def merge_sort_helper(shelf, left, right):
    """Рекурсивный помощник для сортировки слиянием"""
    if left < right:
        mid = (left + right) // 2
        merge_sort_helper(shelf, left, mid)
        merge_sort_helper(shelf, mid + 1, right)
        merge(shelf, left, mid, right)


def merge_sort(shelf):
    """
    Сортировка слиянием.
    
    Сложность: O(n log n) во всех случаях.
    Память: O(n).
    """
    merge_sort_helper(shelf, 0, len(shelf) - 1)


# ═══════════════════════════════════════════════════════════════════════════════
#                           INTERFACE FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════════

def randomize():
    """Перемешивание массива случайным образом"""
    disable_keys()
    clear()
    target = list(range(10))
    random.shuffle(target)
    for i, t in enumerate(target):
        for j in range(i, len(s)):
            if s[j].size == t + 1:
                s.insert(i, s.pop(j))
    show_text(instructions1)
    show_text(instructions2, line=1)
    show_text(instructions3, line=2)
    enable_keys()


def show_text(text, line=0):
    """Отображение текста инструкций"""
    line = 20 * line
    goto(0, -250 - line)
    write(text, align="center", font=("Courier", 14, "bold"))


# ═══════════════════════════════════════════════════════════════════════════════
#                            SORT TRIGGER FUNCTIONS
# ═══════════════════════════════════════════════════════════════════════════════

def start_bubble():
    disable_keys()
    clear()
    show_text("Bubble Sort")
    bubble_sort(s)
    clear()
    show_text(instructions1)
    show_text(instructions2, line=1)
    show_text(instructions3, line=2)
    enable_keys()


def start_insertion():
    disable_keys()
    clear()
    show_text("Insertion Sort")
    insertion_sort(s)
    clear()
    show_text(instructions1)
    show_text(instructions2, line=1)
    show_text(instructions3, line=2)
    enable_keys()


def start_selection():
    disable_keys()
    clear()
    show_text("Selection Sort")
    selection_sort(s)
    clear()
    show_text(instructions1)
    show_text(instructions2, line=1)
    show_text(instructions3, line=2)
    enable_keys()


def start_quick():
    disable_keys()
    clear()
    show_text("Quicksort")
    quick_sort(s, 0, len(s) - 1)
    clear()
    show_text(instructions1)
    show_text(instructions2, line=1)
    show_text(instructions3, line=2)
    enable_keys()


def start_shell():
    disable_keys()
    clear()
    show_text("Shell Sort")
    shell_sort(s)
    clear()
    show_text(instructions1)
    show_text(instructions2, line=1)
    show_text(instructions3, line=2)
    enable_keys()


def start_cocktail():
    disable_keys()
    clear()
    show_text("Cocktail Sort")
    cocktail_sort(s)
    clear()
    show_text(instructions1)
    show_text(instructions2, line=1)
    show_text(instructions3, line=2)
    enable_keys()


def start_merge():
    disable_keys()
    clear()
    show_text("Merge Sort")
    merge_sort(s)
    clear()
    show_text(instructions1)
    show_text(instructions2, line=1)
    show_text(instructions3, line=2)
    enable_keys()


# ═══════════════════════════════════════════════════════════════════════════════
#                            INITIALIZATION
# ═══════════════════════════════════════════════════════════════════════════════

def init_shelf():
    """Инициализация полки с блоками"""
    global s
    s = Shelf(-200)
    vals = (4, 2, 8, 9, 1, 5, 10, 3, 7, 6)
    for i in vals:
        s.push(Block(i))


def disable_keys():
    """Временное отключение управления во время анимации"""
    onkey(None, "i")
    onkey(None, "s")
    onkey(None, "q")
    onkey(None, "b")
    onkey(None, "h")
    onkey(None, "c")
    onkey(None, "m")
    onkey(None, "r")


def enable_keys():
    """Включение управления"""
    onkey(start_insertion, "i")
    onkey(start_selection, "s")
    onkey(start_quick, "q")
    onkey(start_bubble, "b")
    onkey(start_shell, "h")
    onkey(start_cocktail, "c")
    onkey(start_merge, "m")
    onkey(randomize, "r")
    onkey(bye, "space")


def main():
    """Главная функция запуска"""
    getscreen().clearscreen()
    tracer(False)  # Отключаем автоматическое обновление для плавной анимации
    ht()
    penup()
    init_shelf()
    show_text(instructions1)
    show_text(instructions2, line=1)
    show_text(instructions3, line=2)
    enable_keys()
    listen()
    tracer(True)
    return "EVENTLOOP"


# ═══════════════════════════════════════════════════════════════════════════════
#                            GLOBAL STRINGS
# ═══════════════════════════════════════════════════════════════════════════════

instructions1 = "press i:insertion  s:selection  q:quicksort  b:bubble"
instructions2 = "press h:shell  c:cocktail  m:merge  r:randomize"
instructions3 = "spacebar:quit  (orange=comparing, purple=moving)"


if __name__ == "__main__":
    msg = main()
    mainloop()