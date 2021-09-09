def reverse(x: int) -> int:
        
    reversed = 0
    sign = 1

    if x < 0:
        sign = -1
        x = x * -1
    
    while x > 0:
        remainder = x % 10
        reversed = reversed * 10 + remainder
        x = x // 10
    
    result = reversed * sign

    limit = 2**31
    if not -1 * limit < result < limit:
        return 0
    
    return result
        
print(reverse(123))  # 321
print(reverse(-123)) # -321
print(reverse(120))  # 21
print(reverse(0))    # 0
