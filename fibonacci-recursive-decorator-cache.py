def memo(f):
    cache = {}

    def inner(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return inner


@memo
def fib_rec(n):
    assert n >= 0
    return n if n <= 1 else fib_rec(n - 1) + fib_rec(n - 2)


def main():
    n = int(input())
    print(fib_rec(n))


if __name__ == '__main__':
    main()
