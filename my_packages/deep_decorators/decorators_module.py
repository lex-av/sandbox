# -*- coding: utf-8 -*-


def multiple_execution(times=5):
    def executor(func):
        def wrapper(*args, **kwargs):
            for i in range(times):
                yield func(*args, **kwargs)

        return wrapper

    return executor


@multiple_execution(10)
def mul(a, b):
    return a * b


if __name__ == "__main__":
    print([i for i in mul(2, 3)])
