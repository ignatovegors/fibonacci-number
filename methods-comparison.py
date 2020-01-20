from matplotlib import pyplot as plt
import time


def fib_iter(n):
    assert n >= 0
    f0, f1 = 0, 1
    for i in range(n - 1):
        f0, f1 = f1, f0 + f1
    return f1


def fib_rec(n):
    assert n >= 0
    return n if n <= 1 else fib_rec(n - 1) + fib_rec(n - 2)


def timed(f, *args, n_iter=100):
    acc = float("inf")
    for i in range(n_iter):
        t0 = time.perf_counter()
        f(*args)
        t1 = time.perf_counter()
        acc = min(acc, t1 - t0)
    return acc


def plotting(fs, args):
    for f in fs:
        plt.plot(args, [timed(f, arg) for arg in args], label=f.__name__)
        plt.legend()
        plt.grid(True)
    plt.show()


def main():
    n = 20
    plotting([fib_rec, fib_iter], list(range(n)))
    plotting([fib_rec], list(range(n)))
    plotting([fib_iter], list(range(n)))


if __name__ == '__main__':
    main()
