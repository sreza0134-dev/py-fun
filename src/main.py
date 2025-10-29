from src.calculator.calculator import Calculator

def main():
    c1 = Calculator()
    c2 = Calculator()

    print(f' 1: c1.add(1, 2)\t-> {c1.add(1, 2)}')
    print(f' 2: c2.add(8, 3)\t-> {c2.add(8, 3)}')
    print(f' 3: c1.add("1", "1.600") -> {c1.add("1", "1.600")}')
    print(f' 4: c1.add("three", "1.600") -> {c1.add("three", "1.600")}')
    print(f' 5: c1.add("cinco", "siete") -> {c1.add("cinco", "siete")}')
    print(f' 6: c1.add("семь", "восемь") -> {c1.add("семь", "восемь")}')
    print(f' 7: c1.add("III", "VIII") -> {c1.add("III", "VIII")}')
    print(f' 8: c1.add("三", "五") -> {c1.add("三", "五")}')

    print()
    print(f'factorize("три") -> {c2.factorize("три")}')
    print(f'factorize("X") -> {c2.factorize("X")}')
    print(f'factorize("ocho") -> {c2.factorize("ocho")}')
    print(f'factorize(32768) -> {c2.factorize(32768)}')
    print(f'factorize(1092) -> {c2.factorize(1092)}')

if __name__ == "__main__":
    main()

