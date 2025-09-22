def num_prime_digits(n: int):

    nums = list(range(n+1))
    nums[1] = 0

    i = 2
    while i <= n:

        if nums[i] != 0:
            j = 2 * i
            while j <= n:
                nums[j] = 0
                j += i
        i += 1

    return len([i for i in nums if i != 0])