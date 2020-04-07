# encoding: utf-8
# https://realpython.com/primer-on-python-decorators/
import functools
import logging


def foo():
    print("foo")


def bar(func):
    func()


def car(func, *args, **kwargs):
    func(*args, **kwargs)


def logit(func):
    logging.warning("this is logging")
    func()

# simple decorator

def log_decorator(func):
    
    def wrapper():
        logging.warning("this is logging,%s"%func.__name__)
        return func()
    return wrapper


def log_decorator_new(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper

@log_decorator
def foo_new():
    print("foo new")


@log_decorator_new
def foo_again():
    print("foo new")


bar(foo)
car(foo)
logit(foo)
decorated_foo = log_decorator(foo)
decorated_foo()
print(decorated_foo.__name__) # wrapper
foo_new()
help(foo_again)
foo_again()