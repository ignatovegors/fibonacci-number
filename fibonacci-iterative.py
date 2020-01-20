def fib_iter(n):
    assert n >= 0
    if n == 0:
        return 0
    f0, f1 = 0, 1
    for i in range(n - 1):
        f0, f1 = f1, f0 + f1
    return f1


def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
