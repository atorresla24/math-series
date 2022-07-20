def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)


if __name__ == '__main__':
    res = int(input('> '))
    print(fibonacci(res))
    #for i in range(res):
        #print(fibonacci(i))


def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1)+lucas(n-2)


if __name__ == '__main__':
    luc = int(input('> '))
    print(lucas(luc))
    #for i in range(luc):
        #print(lucas(i))


def sum_series(n, s, e):
    if s == 0 and e == 1:
        return fibonacci(n-1) + fibonacci(n-2)
    elif s == 2 and e == 1:
        return lucas(n-1) + lucas(n-2)


if __name__ == '__main__':
    num = int(input('Enter number '))
    start = int(input('First number '))
    second = int(input('Second number '))
    print(
        f"""The {num}th number in Fibonacci makes the sum {sum_series(num, start, second)}
    The {num}th in Lucas makes the sum {sum_series(num, start, second)}
    """)
