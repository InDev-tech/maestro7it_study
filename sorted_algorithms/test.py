def binary_search(lst, target):
    left, right = 0, len(lst)-1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left += 1
        else:
            right -= 1
    return -1

sorted_list = [2, 5, 8, 12, 16, 23, 38, 56]
print(binary_search(sorted_list, 23)) # Вывод: 5
print(binary_search(sorted_list, 1))  # Вывод: -1