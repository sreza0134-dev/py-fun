from expressions.expressions import Expressions

def main():
    e = Expressions()

    lists = [
        [4, 12, 3, 8, 17, 12, 1, 8, 7],
        [1, 4, 6, 67, 6, 8, 23, 8, 34, 49, 67, 6, 8, 23, 37, 67, 6, 34, 19, 67, 6, 8]
    ]

    for l in lists:
        e.update_numbers(l)
        e.print_all()
        print()  # separate output for clarity

if __name__ == "__main__":
    main()

