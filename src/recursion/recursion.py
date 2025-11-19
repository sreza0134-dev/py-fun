from functools import lru_cache
from typing import List, Callable, Generator, Tuple

class RecursionExercises:
    def __init__(self):
        self._fib_memo = {}

    # Challenge 1: simple recursive sum
    def sum(self, _numbers: List[int]) -> int:
        if not _numbers:
            return 0
        if len(_numbers) == 1:
            return _numbers[0]
        first, rest = _numbers[0], _numbers[1:]
        return first + self.sum(rest)

    # Challenge 2: Fibonacci number (with optional memoization)
    def fib(self, _n: int, memoize: bool = False) -> int:
        if _n <= 0:
            return 0
        if _n == 1:
            return 1
        if memoize:
            if _n in self._fib_memo:
                return self._fib_memo[_n]
            val = self.fib(_n - 1, memoize=True) + self.fib(_n - 2, memoize=True)
            self._fib_memo[_n] = val
            return val
        return self.fib(_n - 1, memoize=False) + self.fib(_n - 2, memoize=False)

    def fib_gen(self, _n: int) -> Generator[Tuple[List[int], List[int]], None, None]:
        ns = list(range(0, _n + 1))
        self._fib_memo.clear()
        fibs = [self.fib(i, memoize=True) for i in ns]
        yield ns, fibs

    # Challenge 3: permutations (recursive)
    def perm(self, _numbers: List[int]) -> List[List[int]]:
        if _numbers is None:
            return []
        if len(_numbers) == 0:
            return [[]]
        if len(_numbers) == 1:
            return [[_numbers[0]]]
        res = []
        first = _numbers[0]
        rest = _numbers[1:]
        perms_rest = self.perm(rest)
        for p in perms_rest:
            for i in range(len(p) + 1):
                new = p[:i] + [first] + p[i:]
                res.append(new)
        return res

    # Challenge 4: powerset (recursive)
    def pset(self, _numbers: List[int]) -> List[List[int]]:
        if _numbers is None:
            return [[]]
        if len(_numbers) == 0:
            return [[]]
        first = _numbers[0]
        rest = _numbers[1:]
        subsets_rest = self.pset(rest)
        with_first = [s + [first] for s in subsets_rest]
        return subsets_rest + with_first

    # Challenge 5: find functions
    def find(self, _numbers: List[int], match_func: Callable[[int], bool]) -> List[int]:
        res = []
        for x in _numbers:
            if match_func(x):
                res.append(x)
        return res

    def find_adjacent(self, pair: List[int], _numbers: List[int]) -> List[int]:
        res = []
        if not pair or len(pair) != 2:
            return res
        a, b = pair
        for i in range(len(_numbers) - 1):
            if _numbers[i] == a and _numbers[i + 1] == b:
                res.append(i)
        return res

    def find_pairs(self, n: int, _numbers: List[int]) -> List[List[int]]:
        res = []
        values = _numbers[:]
        unique_values = sorted(set(values))
        left = 0
        right = len(unique_values) - 1
        while left <= right:
            a = unique_values[left]
            b = unique_values[right]
            s = a + b
            if s == n:
                if a in values and b in values:
                    res.append([a, b])
                left += 1
                right -= 1
            elif s < n:
                left += 1
            else:
                right -= 1
        return res

    # Challenge 6: combinations that sum to n (backtracking)
    def find_all_sums(self, n: int, _numbers: List[int]) -> List[List[int]]:
        nums = sorted(_numbers)
        results = []
        combo = []
        def backtrack(start: int, remaining: int):
            if remaining == 0:
                results.append(combo.copy())
                return
            if remaining < 0:
                return
            prev = None
            for i in range(start, len(nums)):
                val = nums[i]
                if prev is not None and val == prev:
                    continue
                if val > remaining:
                    break
                combo.append(val)
                backtrack(i + 1, remaining - val)
                combo.pop()
                prev = val
        backtrack(0, n)
        return results

    # Challenge 7: optimized backtracking with pruning
    def find_all_sums_dp(self, n: int, _numbers: List[int]) -> List[List[int]]:
        nums = sorted(_numbers)
        results = []
        combo = []
        suffix_sum = [0] * (len(nums) + 1)
        for i in range(len(nums) - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + nums[i]
        def backtrack(start: int, remaining: int):
            if remaining == 0:
                results.append(combo.copy())
                return
            if start >= len(nums):
                return
            if remaining < 0:
                return
            if suffix_sum[start] < remaining:
                return
            prev = None
            for i in range(start, len(nums)):
                val = nums[i]
                if prev is not None and val == prev:
                    continue
                if val > remaining:
                    break
                combo.append(val)
                backtrack(i + 1, remaining - val)
                combo.pop()
                prev = val
        backtrack(0, n)
        return results
