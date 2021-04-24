# -*- coding: UTF-8 -*-
# author: yuanpx

class ArraysUtils:
    @classmethod
    def arrays_remove_duplicate(cls, array_large, array_small):
        array_new = []
        for e in array_small:
            if e not in array_large:
                array_new.append(e)
        return array_new

    @classmethod
    def arrays_get_duplicate(cls, array1, array2):
        array_new = []
        for e in array2:
            if e in array1:
                array_new.append(e)
        return array_new