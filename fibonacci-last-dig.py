def fib_digit(n):
    a = 0
    b = 1
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        for i in range(2, n + 1):
            c = (a + b) % 10
            a = b
            b = c
        return c


def main():
    n = int(input())
    print(fib_digit(n))


if __name__ == "__main__":
    main()
