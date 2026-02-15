'''
https://leetcode.com/problems/container-with-most-water/description/
'''

class Solution:
    def maxArea(self, height):
        """
        Находит максимальную площадь контейнера для воды.

        Даны n вертикальных линий с высотами height[i]. 
        Нужно выбрать две линии так, чтобы они вместе с осью X образовали контейнер, 
        который вмещает максимальное количество воды.

        Алгоритм:
        - Используется два указателя: left в начале, right в конце массива.
        - На каждом шаге вычисляется площадь: 
            area = (right - left) * min(height[left], height[right]).
        - Указатель с меньшей высотой двигается внутрь, 
          так как именно он ограничивает возможную площадь.
        - Работает за O(n), требует O(1) памяти.

        :param height: список высот вертикальных линий
        :return: максимальная площадь контейнера
        """
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area