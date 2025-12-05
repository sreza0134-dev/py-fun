# demo_stream.py
import random
from stream import Stream

names = ['Gonzalez', 'Gill', 'Hardin', 'Richardson', 'Buckner', 'Marquez',
    'Howe', 'Ray', 'Navarro', 'Talley', 'Bernard', 'Gomez', 'Hamilton',
    'Case', 'Petty', 'Lott', 'Casey', 'Hall', 'Pena', 'Witt', 'Joyner',
    'Raymond', 'Crane', 'Hendricks', 'Vance', 'Cleveland', 'Duncan', 'Soto',
    'Brock', 'Graham', 'Nielsen', 'Rutledge', 'Strong', 'Cox']

print("=== Example 1: filter length == 4, print, count")
result = Stream(names).source() \
    .filter(lambda n: len(n) == 4) \
    .print() \
    .count()
print(f'found {result} names with 4 letters.')
print()

print("=== Example 2: slice, map to lengths, print")
Stream(names).source() \
    .slice(8) \
    .print() \
    .map(lambda n: len(n)) \
    .print()
print()

print("=== Example 3: slice, map, reduce to sum lengths")
result = Stream(names).source() \
    .slice(8) \
    .print() \
    .map(lambda n: len(n)) \
    .print() \
    .reduce(lambda x, y: x + y)
print(f'compound number of letters in names is: {result}.')
print()

print("=== Example 3.1: compound n-letter names to uppercase string (n=3 then n=5)")
for n in (3, 5):
    res = Stream(names).source() \
        .filter(lambda name: len(name) == n) \
        .print() \
        .map(lambda s: s.upper()) \
        .reduce(lambda x, y: str(x) + str(y), '')
    print(f'compounded {n}-letter names: {res}.')
    print()

print("=== Example 4: sort default (slice 8) unsorted and sorted")
Stream(names).source() \
    .slice(8) \
    .print('unsorted: ') \
    .sort() \
    .print('  sorted: ')
print()

# comparator: sort by length ascending, then alphabetically
def len_alpha_comperator(n1, n2):
    if len(n1) != len(n2):
        return len(n1) - len(n2)
    # alphabetical comparison
    return (n1 > n2) - (n1 < n2)

print("=== Example 4.1: sort by (length, alphabetic)")
Stream(names).source() \
    .sort(len_alpha_comperator) \
    .print('sorted: ')
print()

# 4.2: transform to (name, reversed.capitalized(), len) and keep odd lengths
print("=== Example 4.2: sort, transform, filter odd lengths, print and count")
res_stream = Stream(names).source() \
    .sort(len_alpha_comperator) \
    .map(lambda n: (n, n[::-1].capitalize(), len(n))) \
    .filter(lambda t: t[2] % 2 == 1) \
    .print('sorted: ')
count_odd = Stream(names).source() \
    .sort(len_alpha_comperator) \
    .map(lambda n: (n, n[::-1].capitalize(), len(n))) \
    .filter(lambda t: t[2] % 2 == 1) \
    .count()
print("\\\\")
print(f"{count_odd} odd-length names found.")
print()

print("=== Example 5: Pipeline for Product Codes (deterministic via seed)")
random.seed(42)  # deterministic output for demo
for i in range(1, 5):
    numbers = [random.randint(100000, 999999) for _ in range(5)]
    # pipeline: sort numbers, map to 'X' + number + '-' + checksum
    codes = Stream(numbers).source() \
        .sort() \
        .map(lambda n: f"X{n}-{sum(int(d) for d in str(n)) % 10}") \
        .get()
    print(f'batch {i}: {codes}')
print()

print("=== Example 5.1: even-digit codes only (same seed)")
random.seed(42)
for i in range(1, 5):
    numbers = [random.randint(100000, 999999) for _ in range(10)]
    codes = Stream(numbers).source() \
        .map(lambda n: str(n)) \
        .filter(lambda s: all(int(ch) % 2 == 0 for ch in s)) \
        .map(lambda s: f"X{s}-{sum(int(d) for d in s) % 10}") \
        .sort() \
        .get()
    # take first 5 codes per batch
    codes = codes[:5]
    print(f'batch {i}: {codes}')
print()

