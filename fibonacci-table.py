def fib(n):
    assert n >= 0
    if n not in fib_cache:
        fib_cache[n] = n if n <= 1 else fib(n - 1) + fib(n - 2)
    return fib_cache[n]


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    fib_cache = {}
    main()
