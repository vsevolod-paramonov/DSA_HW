from collections import defaultdict

def anagrams(words):
    '''
    Только для английских слов. Иначе подход с ключом в виде кортежа из 26 чисел не сработает.
    Если знаем, что вход состоит из английских слов, то можем гарантировать работу за O(N * K) по скорости.

    Если нет такого условия на язык слов, то можно использовать сортировку слова в качестве ключа, но скорость работы
    алгоритма будет O(N * K log K)
    '''
    output = defaultdict(list)

    for word in words:
        count = [0] * 26

        for c in word:
            count[ord(c) - ord('a')] += 1

        output[tuple(count)].append(word)

    return list(output.values())