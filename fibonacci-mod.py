def piz_seq(m):
    a = 1
    b = 1

    for i in range(2, 6 * m + 2):
        c = a + b
        a = b
        b = c

        if a % m == 0 and b % m == 1:
            return i


def fib_iter(n):
    assert n >= 0
    if n == 0:
        return 0
    f0, f1 = 0, 1
    for i in range(n - 1):
        f0, f1 = f1, f0 + f1
    return f1


def fib_mod(n, m):
    if 6 * m < n:
        period = piz_seq(m)
        return fib_iter(n % period) % m
    else:
        return fib_iter(n) % m


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == '__main__':
    main()
