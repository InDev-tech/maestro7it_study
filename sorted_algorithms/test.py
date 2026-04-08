def sqrt_search(target, eps=1e-6):
    left, right = 1, max(1, target)
    while right - left >= eps:
        mid = (left + right) / 2
        if mid * mid < target:
            left = mid
        else:
            right = mid
    return (left + right) / 2

print(sqrt_search(5))