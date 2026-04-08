class Solution:
    def mySqrt(self, x):
        """        
        Задача: Sqrt(x) (LeetCode)
        Алгоритм: Бинарный поиск для нахождения целочисленного квадратного корня
        Сложность: O(log n) по времени, O(1) по памяти
        
        Идея решения:
        1. Используем бинарный поиск в диапазоне [0, x]
        2. Для каждого mid проверяем: mid² <= x
        3. Если mid² == x, возвращаем mid
        4. Если mid² < x, двигаемся вправо (start = mid + 1)
        5. Если mid² > x, двигаемся влево (end = mid - 1)
        6. Python автоматически работает с большими числами
        """
        
        # Базовые случаи
        if x == 0 or x == 1:
            return x
        
        start = 1
        end = x
        result = 0
        
        while start <= end:
            mid = start + (end - start) // 2
            square = mid * mid
            
            if square == x:
                return mid  # Точный квадратный корень
            elif square < x:
                start = mid + 1
                result = mid  # Сохраняем потенциальный результат
            else:
                end = mid - 1
        
        return result