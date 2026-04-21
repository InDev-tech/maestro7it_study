def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for array in range(n-i-1):
            swapped = False
            if nums[array] > nums[array+1]:
                nums[array], nums[array+1] = nums[array+1], nums[array]
                swapped = True
        if not swapped:
            break
    return nums

if __name__ == "__main__":
    test_array = [-13, 64, 34, 25, 12, -15, 22, 90, 11]
    
    print(f"Исходный массив: {test_array}")
    print(f"Пузырьковая:     {bubble_sort(test_array.copy())}")