def fib_mod(n, m):
    f0, f1 = 0, 1
    cached = [f0, f1]

    for i in range(1, n):
        f0, f1 = f1, (f1 + f0) % m

        if f0 == 0 and f1 == 1:
            cached.pop()
            break
        else:
            cached.append(f1)

    offset = n % len(cached)
    return cached[offset]


def main():
    n, m = map(int, input().split())
    print(fib_mod(n, m))


if __name__ == "__main__":
    main()
