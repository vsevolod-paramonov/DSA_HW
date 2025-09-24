
def num_prime_digits(n: int):
    '''
    Поиска числа простых чисел от 0 до n включительно
    '''

    ### Решето Эратосфена

    if n <= 0:
        return 0

    nums = list(range(n+1))
    nums[1] = 0

    ### Стартуем с 2
    i = 2
    while i <= n:

        ### Если не зануляли текущее число, то зануляем все его кратные
        if nums[i] != 0:
            j = 2 * i
            while j <= n:
                nums[j] = 0
                j += i
        i += 1

    ### Считаем число не зануленных элементов
    return len([i for i in nums if i != 0])