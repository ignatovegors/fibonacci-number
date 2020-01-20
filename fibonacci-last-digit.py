def fib_last_digit(n):
    assert n >= 0
    f0, f1 = 0, 1
    for i in range(n - 1):
        f0, f1 = f1, (f0 + f1) % 10
    return f1


def main():
    n = int(input())
    print(fib_last_digit(n))


if __name__ == "__main__":
    main()
