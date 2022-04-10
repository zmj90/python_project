import logging
from functools import wraps


def time_test_date(*args):
    def decorator_(test_func):
        @wraps(test_func)
        def wrapper():
            logging.info(args[2])
            logging.info(args[3])
            d1 = {f"{args[0]}": args[2], f"{args[1]}": args[3]}
            test_func(**d1)
        return wrapper
    return decorator_


n1, n2, n3, n4 = "a", "b", 123, 456


@time_test_date(n1, n2, n3, n4)
def fun1(a, b):
    print(a)
    print(b)


fun1()
