def piz_seq(m):
    assert n >= 0
    f0, f1 = 0, 1
    for i in range(6 * m - 1):
        f0, f1 = f1, f0 + f1
        if f0 % m == 0 and f1 % m == 1:
            return i


def fib(n):
    assert n >= 0
    f0, f1 = 0, 1
    for i in range(n - 1):
        f0, f1 = f1, f0 + f1
    return f1


def fib_mod(n, m):
    if 6 * m < n:
        period = piz_seq(m)
        return fib(n % period) % m
    else:
        return fib(n) % m


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == '__main__':
    main()
