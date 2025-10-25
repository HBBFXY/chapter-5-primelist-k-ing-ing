import math

def PrimeList(N):
    """
    返回小于 N 的所有质数，以空格分隔    
    参数:    N - 正整数    
    返回:    str - 包含所有小于 N 的质数的字符串，空格分隔
    """
    primes = []
    if N <= 2:
        return ''
    for num in range(2, N):
        is_prime = True
        # 优化：只检查到平方根，且步长为2（排除偶数）
        sqrt_num = int(math.sqrt(num)) + 1
        # 先判断是否为偶数（除2外）
        if num > 2 and num % 2 == 0:
            is_prime = False
        else:
            # 只检查奇数
            for i in range(3, sqrt_num, 2):
                if num % i == 0:
                    is_prime = False
                    break
        if is_prime:
            primes.append(str(num))
    return ' '.join(primes)
