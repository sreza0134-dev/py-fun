class Expressions:
    # Must be class attribute for the professor's tests
    default_numbers = [4, 12, 3, 8, 17, 12, 1, 8, 7]

    def __init__(self, numbers=None):
        # Use default_numbers if no list is provided
        self.numbers = numbers if numbers is not None else self.default_numbers
        self.update_all()

    def update_numbers(self, numbers):
        self.numbers = numbers
        self.update_all()

    def update_all(self):
        numbers = self.numbers

        # handle empty list
        if not numbers:
            self.a = 0
            self.b = []
            self.c = []
            self.d = []
            self.e = []
            self.f = 0
            self.g = 0
            self.h = []
            self.i = 0
            self.j = []
            self.k = "EMPTY_LIST"
            return

        self.a = len(numbers)
        self.b = numbers[:3]
        self.c = numbers[-3:]
        self.d = numbers[-3:][::-1]
        self.e = [x for x in numbers if x % 2 != 0]
        self.f = len(self.e)
        self.g = sum(self.e)
        self.h = list(dict.fromkeys(numbers))  # remove duplicates
        self.i = len(numbers) - len(self.h)
        self.j = sorted([x*x for x in self.h])
        self.k = "ODD_LIST" if len(numbers) % 2 else "EVEN_LIST"

    def print_all(self):
        print(f"numbers: {self.numbers}")
        print(f"a) number of numbers: {self.a}")
        print(f"b) first three numbers: {self.b}")
        print(f"c) last three numbers: {self.c}")
        print(f"d) last three numbers reverse: {self.d}")
        print(f"e) odd numbers: {self.e}")
        print(f"f) number of odd numbers: {self.f}")
        print(f"g) sum of odd numbers: {self.g}")
        print(f"h) duplicate numbers removed: {self.h}")
        print(f"i) number of duplicate numbers: {self.i}")
        print(f"j) ascending, de-dup (n^2) numbers: {self.j}")
        print(f"k) length: {self.k}")

