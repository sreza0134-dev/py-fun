class Stream:
    """
    Data stream class using an inner chainable operator class.
    """

    class __Stream_op:
        def __init__(self, data):
            self.__data = data

        # helper to create new op
        def __new(self, data):
            return Stream._Stream__Stream_op(data)

        def slice(self, i1, i2=None, i3=1):
            if i2 is None:
                i2, i1 = i1, 0
            return self.__new(self.__data[i1:i2:i3])

        def filter(self, filter_func=lambda d: True):
            return self.__new([d for d in self.__data if filter_func(d)])

        def map(self, map_func=lambda d: d):
            return self.__new([map_func(d) for d in self.__data])

        def reduce(self, reduce_func, start=0):
            r = start
            for d in self.__data:
                r = reduce_func(r, d)
            return r

        def sort(self, comparator_func=None):
            if comparator_func is None:
                return self.__new(sorted(self.__data))

            # convert comparator to key
            def cmp_to_key(comparator):
                class K:
                    def __init__(self, obj):
                        self.obj = obj

                    def __lt__(self, other):
                        return comparator(self.obj, other.obj) < 0

                return K

            return self.__new(sorted(self.__data, key=cmp_to_key(comparator_func)))

        def cond(self, cond, conditional):
            if cond:
                return conditional(self)
            return self

        def print(self, text=''):
            print(text + str(self.__data))
            return self

        def count(self):
            return len(self.__data)

        def get(self):
            return self.__data

    # END INNER CLASS

    def __init__(self, data):
        self.__data = data

    def source(self):
        return Stream._Stream__Stream_op(self.__data)

