from time import time


def performance(func):
    def wrap_func(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f"It took {(end - start):.4f} s")
        return result

    return wrap_func


@performance
def long_time():
    for i in range(1000000000):
        i * 5


long_time()