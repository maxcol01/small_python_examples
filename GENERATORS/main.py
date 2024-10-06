# list version
def fibonacci(num):
    fib_list = [0, 1]
    if num == 0:
        return [fib_list[0]]
    elif num == 1:
        return fib_list
    else:
        for item in range(0, num):
            current = fib_list[item] + fib_list[item + 1]
            fib_list.append(current)
        return fib_list


# print(fibonacci(0))

# Generator version
def fibonacci_gen(num):
    first, second = 0, 1
    yield first
    if num > 0:
        yield second
    for _ in range(2, num + 1):
        first, second = second, first + second
        yield second


for number in fibonacci_gen(10):
    print(number)
