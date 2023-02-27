from time import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()

        print(f"[ INFO ] Time taken to execute :- {end - start}")
        return result
    return wrapper
