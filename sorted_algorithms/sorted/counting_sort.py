def counting_sort(arr):
    """
    Сортировка подсчетом.
    
    Несравнивающий алгоритм сортировки. Подсчитывает количество вхождений 
    каждого уникального элемента, затем восстанавливает отсортированный массив.
    
    Подходит только для целых чисел (или приводимых к целым) в известном диапазоне.
    
    Сложность:
        - Время: O(n + k), где k - размер диапазона значений.
        - Память: O(k).
    
    Аргументы:
        arr (list): Список целых чисел.

    Возвращает:
        list: Новый отсортированный список.
    
    Исключения:
        ValueError: Если массив пуст.
    """
    if not arr:
        return []
        
    max_val = max(arr)
    min_val = min(arr)
    range_of_values = max_val - min_val + 1
    
    # Массив для подсчета
    count = [0] * range_of_values
    
    # Подсчет элементов
    for num in arr:
        count[num - min_val] += 1
        
    # Восстановление отсортированного массива
    sorted_arr = []
    for i in range(range_of_values):
        sorted_arr.extend([i + min_val] * count[i])
        
    return sorted_arr


# Пример использования и проверки
if __name__ == "__main__":
    test_array = [64, 34, 25, 12, 22, 11, 90]
    
    print(f"Исходный массив: {test_array}")
    print(f"Подсчетом:        {counting_sort(test_array.copy())}")