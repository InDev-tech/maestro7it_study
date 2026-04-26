class Solution:
    def fairCandySwap(self, aliceSizes, bobSizes):
        """
        Находит размеры коробок для обмена, чтобы у Алисы и Боба стало поровну конфет.

        Алгоритм:
        - Вычисляем общую сумму конфет у Алисы и Боба.
        - Находим разницу diff = (sumA - sumB) // 2.
        - Для каждой коробки Алисы a вычисляем необходимую коробку Боба b = a - diff.
        - Если b есть у Боба (хранится в множестве), возвращаем [a, b].

        Параметры:
        aliceSizes (list[int]) – список коробок Алисы.
        bobSizes   (list[int]) – список коробок Боба.

        Возвращает:
        list[int] – два числа [коробка_Алисы, коробка_Боба].
        """
        sumA = sum(aliceSizes)
        sumB = sum(bobSizes)
        diff = (sumA - sumB) // 2
        setB = set(bobSizes)
        for a in aliceSizes:
            need = a - diff
            if need in setB:
                return [a, need]