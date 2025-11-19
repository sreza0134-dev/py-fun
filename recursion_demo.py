from src.recursion.recursion import RecursionExercises

n1 = RecursionExercises()

# Challenge 1
lst = [9, 4, 8, 10, 2, 4, 8, 3, 14, 4, 8]
print("n1.numbers:", lst)
print("sum(n1.numbers):", n1.sum(lst))
print()

# Challenge 2
for ns, fibs in n1.fib_gen(20):
    print("n:     ", ns)
    print("fib(n):", fibs)
n = 30
print(f"fib({n}): {n1.fib(n, memoize=True)}")
n = 60
print(f"fib({n}): {n1.fib(n, memoize=True)}")
n = 90
print(f"fib({n}): {n1.fib(n, memoize=True)}")
print()

# Challenge 3
lst = [1, 2, 3]
print(f"perm({lst}) -> {n1.perm(lst)}")
lst = [1, 2, 3, 4]
print(f"perm({lst}) -> {n1.perm(lst)}")
print()

# Challenge 4
lst = [1, 2, 3]
print(f"pset({lst}) -> {n1.pset(lst)}")
print()

# Challenge 5
lst = [9, 4, 8, 10, 2, 4, 8, 3, 14, 4, 8]
div3 = n1.find(lst, match_func=lambda n: n % 3 == 0)
print(f"find numbers divisible by 3: {div3}")
p = [4, 8]
adj = n1.find_adjacent(p, lst)
print(f"find_adjacent({p}, list): {adj}")
pairs = n1.find_pairs(12, lst)
print(f"find_pairs(12, list) -> {pairs}")
print()

# Challenge 6
lst = [8, 10, 2, 14, 4]
print(f"find_all_sums(14, lst) -> {n1.find_all_sums(14, lst)}")
lst_big = [260,720,225,179,101,767,167,200,157,289,318,303,153,290,201,594,457,607,592,246]
print(f"find_all_sums(469, lst_big) -> {n1.find_all_sums(469, lst_big)}")
print()

# Challenge 7 (hard) - use dp/backtracking
lst64 = [
    260,720,225,179,101,767,167,200,157,289,
    318,303,153,290,201,594,457,607,592,246,
    132,135,584,432,591,204,417,405,362,658,
    136,751,583,536,293,493,431,780,563,703,
    400,618,397,320,513,708,319,317,685,347,
    758,439,145,378,158,384,551,110,408,648,
    847,498,50,19
]
res = n1.find_all_sums_dp(469, lst64)
res_sorted = sorted(res, key=lambda s: (len(s), s[0] if s else 0))
for i,s in enumerate(res_sorted, start=1):
    print(f" {i:2}: sum({sum(s)}) -> {s}")
