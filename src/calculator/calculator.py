import re

class Calculator:
    _instance = None  # Singleton instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        # Mapping of number words in different languages
        self.words = {
            # English
            "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
            "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9,
            # German
            "null": 0, "eins": 1, "zwei": 2, "drei": 3, "vier": 4,
            "fünf": 5, "sechs": 6, "sieben": 7, "acht": 8, "neun": 9,
            # Spanish
            "cero": 0, "uno": 1, "dos": 2, "tres": 3, "cuatro": 4,
            "cinco": 5, "seis": 6, "siete": 7, "ocho": 8, "nueve": 9,
            # Russian (Cyrillic)
            "ноль": 0, "один": 1, "два": 2, "три": 3, "четыре": 4,
            "пять": 5, "шесть": 6, "семь": 7, "восемь": 8, "девять": 9,
            # Chinese (Simplified)
            "零": 0, "一": 1, "二": 2, "三": 3, "四": 4,
            "五": 5, "六": 6, "七": 7, "八": 8, "九": 9,
        }

        # Roman numerals
        self.romans = {
            "I": 1, "V": 5, "X": 10, "L": 50,
            "C": 100, "D": 500, "M": 1000
        }

    # --- internal helpers ---

    def _to_number(self, x):
        """Convert string, int, float, roman, or word into float."""
        if isinstance(x, (int, float)):
            return float(x)

        if isinstance(x, str):
            s = x.strip().upper()
            # try numeric string
            try:
                return float(s)
            except ValueError:
                pass

            # try lowercase word in multiple languages
            low = x.strip().lower()
            if low in self.words:
                return float(self.words[low])

            # try roman numerals
            if all(ch in self.romans for ch in s):
                return float(self._roman_to_int(s))

        raise ValueError(f"Cannot convert '{x}' to number")

    def _roman_to_int(self, s):
        result = 0
        prev = 0
        for ch in reversed(s):
            val = self.romans[ch]
            if val < prev:
                result -= val
            else:
                result += val
            prev = val
        return result

    # --- calculator methods ---

    def add(self, a, b):
        return self._to_number(a) + self._to_number(b)

    def sub(self, a, b):
        return self._to_number(a) - self._to_number(b)

    def mul(self, a, b):
        return self._to_number(a) * self._to_number(b)

    def div(self, a, b):
        return self._to_number(a) / self._to_number(b)

    def factorize(self, n):
        num = int(self._to_number(n))
        factors = []
        d = 2
        while d * d <= num:
            while num % d == 0:
                factors.append(d)
                num //= d
            d += 1
        if num > 1:
            factors.append(num)
        return factors

