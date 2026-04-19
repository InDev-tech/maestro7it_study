def merge_sort(arr):
    """
    Сортировка слиянием.
    
    Рекурсивный алгоритм, работающий по принципу "разделяй и властвуй".
    Массив рекурсивно делится пополам, пока размер части не станет равен 1,
    затем отсортированные части сливаются воедино.
    
    Сложность:
        - Время: O(n log n) во всех случаях (гарантированно).
        - Память: O(n) (требуется дополнительная память для слияния).
    
    Аргументы:
        arr (list): Список элементов, поддерживающих сравнение.

    Возвращает:
        list: Новый отсортированный список (исходный список не изменяется).
    """
    if len(arr) <= 1:
        return arr

    # Разделение
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Слияние
    return _merge(left_half, right_half)

def _merge(left, right):
    """Вспомогательная функция для слияния двух отсортированных списков."""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    # Добавляем оставшиеся элементы
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Пример использования и проверки
if __name__ == "__main__":
    test_array = [64, 34, 25, 12, 22, 11, 90]
    
    print(f"Исходный массив: {test_array}")
    print(f"Слиянием:         {merge_sort(test_array.copy())}")