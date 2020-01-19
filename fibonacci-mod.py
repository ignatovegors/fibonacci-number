def piz_seq(m):
    a = 1
    b = 1

    for i in range(2, 6 * m + 1):
        c = a + b
        a = b
        b = c

        if a % m == 0 and b % m == 1:
            return i


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return c


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
