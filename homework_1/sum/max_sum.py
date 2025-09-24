
def max_sum_div2(numbers: list):
    '''
    Поиск максимальной суммы элементов массива, которая делится на 2
    '''

    sum_all = sum(numbers)

    ### Если сумма четная, возвращаем ее
    if sum_all % 2 == 0:
        return sum_all
    
    ### Иначе вычитаем из суммы минимальное нечетное число
    odd_numbers = [i for i in numbers if i % 2 != 0]
    
    ### Если сумма нечетная и нет нечетных чисел, то возвращаем 0
    if not odd_numbers:
        return 0
    
    ### Иначе вычитаем из суммы минимальное нечетное число
    return sum_all - min(odd_numbers)


