def fib(n):
    res = [0, 1]
    for i in range(2, n+1):
        res.append(res[i-1] + res[i-2])
    return res[n]

def main():
    n = int(input())
    print(fib(n))


if __name__ == "__main__":
    main()
