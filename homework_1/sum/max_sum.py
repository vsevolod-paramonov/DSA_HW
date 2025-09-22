

def max_sum_div2(numbers: list):

    sum_all = sum(numbers)

    if sum_all % 2 == 0:
        return sum_all
    
    odd_numbers = [i for i in numbers if i % 2 != 0]
    
    if not odd_numbers:
        return 0
    
    return sum_all - min(odd_numbers)


