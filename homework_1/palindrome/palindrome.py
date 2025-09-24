
def max_divisor(number: int):
    '''
    Поиск максимального порядка числа
    '''
    
    div = 1
    while number // div >= 10:
        div *= 10

    return div


def is_palindrome(number: int):
    '''
    Проверка числа на палиндром
    '''

    ### Если число отрицательное, оно не может быть палиндромом
    if number < 0:
        return False
 
    ### Заводим "левые и правые" указатели на начало и конец числа
    l, r = max_divisor(number), 10

    ### Проверяем левые и правые цифры на равенство
    while number > 0:
        if number // l != number % r:
            return False

        ### Через арифметические операции сдвигаем указатели к центру числа
        number = (number % l) // r
        l //= 100

    return True
