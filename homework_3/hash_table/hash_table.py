class HashMap:
    def __init__(self, capacity = 8, 
                       limit = 0.9):
        self.size_max = capacity
        self.limit = limit
        self.size = 0

        ### Задаем такие "ячейки", чтобы в случае коллизий в них можно было хранить несколько ключей и значений
        self.k_list = [[] for _ in range(capacity)]
        self.v_list = [[] for _ in range(capacity)]

    def _get_index(self, key):
        '''
        Определяем хэш-функцию для ключей
        '''
        return hash(key) % self.size_max

    def _grow(self):
        '''
        Увеличиваем размер таблицы в 2 раза и переносим всё
        '''
        old_k = self.k_list
        old_v = self.v_list

        ### Увеличиваем размер в 2 раза и создаем новые массивы побольше
        self.size_max *= 2
        self.k_list = [[] for _ in range(self.size_max)]
        self.v_list = [[] for _ in range(self.size_max)]
        self.size = 0

        for ks, vs in zip(old_k, old_v):
            for k, v in zip(ks, vs):
                self.put(k, v)

    def put(self, key, value):
        '''
        Добавление нового элемента или обновление старого
        '''
        idx = self._get_index(key)

        ### Проверяем, есть ли ключ в ячейке 
        ### Решаем проблему с коллизиями
        if key in self.k_list[idx]:
            pos = self.k_list[idx].index(key)
            self.v_list[idx][pos] = value
        else:
            self.k_list[idx].append(key)
            self.v_list[idx].append(value)
            self.size += 1

        ### Если на грани переполнения, то x2 увеличиваем размер
        if self.size / self.size_max > self.limit:
            self._grow()

    def get(self, key):
        '''
        Получить значение по ключу
        '''
        idx = self._get_index(key)

        if key in self.k_list[idx]:
            pos = self.k_list[idx].index(key)
            return self.v_list[idx][pos]
        return None

    def delete(self, key):
        '''
        Удаление элемента по ключу
        '''
        idx = self._get_index(key)

        if key in self.k_list[idx]:
            pos = self.k_list[idx].index(key)
            del self.k_list[idx][pos]
            del self.v_list[idx][pos]
            self.size -= 1
            return True
        return False

    def __len__(self):
        '''
        Возвращение размера хэш-таблицы
        '''
        return self.size
