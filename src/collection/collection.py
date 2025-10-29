import itertools

class Collection:
    def contains(self, s, e):
        return s.count(e)

    def zip(self, s, p):
        return list(zip(s, p))

    def pset(self, s):
        s = list(s)
        return [list(subset) for i in range(len(s)+1) for subset in itertools.combinations(s, i)]

    def perm(self, p):
        return [list(x) for x in itertools.permutations(p)]
