# -*- coding: utf-8 -*-
'''Chained Dictionary with doubling and halving


Implement a dictionary using chaining.
You may assume every key has a hash() method, e.g.:
>>> hash(1)
1
>>> hash('hello world')
-2324238377118044897

Author: Larsen Close
Version: Completed through extra credit with several extra methods implemented
with tests
Outline and initial tests provided in class by Professor Dr. Beaty at MSU Denver


Todo:
    * Make runnable from file
    * Also also use ``sphinx.ext.todo`` extension
'''


class Dictionary:
    """dictionary class with doubling and halfing"""
    def __init__(self, init=None):
        self.__limit = 10
        self.__items = [[] for _ in range(self.__limit)]
        self.__count = 0

        if init:
            for i in init:
                self.__setitem__(i[0], i[1])

    def __len__(self):
        self.__count = 0
        for i in self.__iter__():
            self.__count += 1
        return self.__count

    def flattened(self):
        return [item for inner in self.__items for item in inner]

    def __iter__(self):
        return iter(self.flattened())

    def __str__(self):
        return str(self.flattened())

    def __setitem__(self, key, value):
        list_number = hash(key) % self.__limit
        for slot in self.__items[list_number]:
            if slot[0] == key:
                slot[1] = value
                return
        self.__items[list_number].append([key, value])

        loadfactor = (len(self) / self.__limit)
        if loadfactor >= 0.75:
            self.__doublehash__()

    def __getitem__(self, key):
        list_number = hash(key) % self.__limit
        for slot in self.__items[list_number]:
            if slot[0] == key:
                return slot[1]
        raise RuntimeError("Key not present")

    def __contains__(self, key):
        list_number = hash(key) % self.__limit
        for slot in self.__items[list_number]:
            if slot[0] == key:
                return True
        return False

    def __doublehash__(self):
        data = iter(self)
        self.__limit *= 2
        self.__items = [[] for _ in range(self.__limit)]
        for d in data:
            self.__setitem__(d[0], d[1])

    def __delitem__(self, key):
        list_number = hash(key) % self.__limit
        for slot in self.__items[list_number]:
            if slot[0] == key:
                del slot[:]
                self.__items[list_number] = [
                    slot for slot in self.__items[list_number] if slot]
                loadfactor = (len(self) / self.__limit)
                if loadfactor <= 0.25:
                    self.__halfhash__()
                return
        raise RuntimeError("Key not present")

    def __halfhash__(self):
        data = iter(self)
        self.__limit = int(self.__limit / 2)
        self.__items = [[] for _ in range(self.__limit)]
        for d in data:
            self.__setitem__(d[0], d[1])

    def __keys__(self):
        keys = []
        for i in iter(self):
            keys.append(i[0])
        return keys

    def __values__(self):
        values = []
        for i in iter(self):
            values.append(i[1])
        return values

    def __eq__(self, value):
        keys1 = self.__keys__()
        values1 = self.__values__()
        keys2 = value.__keys__()
        values2 = value.__values__()
        if keys1 == keys2 and values1 == values2:
            return True
        else:
            return False

    def __items__(self):
        tmp = []
        for i in iter(self):
            tmp.append(tuple(i[:]))
        return tmp
