class Solution:
    def numSteps(self, s):
        steps = 0
        carry = 0
        # Проходим справа налево, начиная с предпоследнего бита
        for i in range(len(s) - 1, 0, -1):
            current_bit = int(s[i]) + carry
            if current_bit == 0:
                # Бит 0: просто делим на 2
                steps += 1
            elif current_bit == 1:
                # Бит 1: добавляем 1, затем делим
                steps += 2
                carry = 1
            else:  # current_bit == 2
                # После переноса имеем 0 с новым переносом
                steps += 1
                carry = 1
        # Обрабатываем старший бит с учётом переноса
        return steps + carry

result = Solution()
print(result.numSteps('1101'))