from functools import wraps

def log_method(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[METHOD] {func.__name__}{args, kwargs}")
        result = func(*args, **kwargs)
        return result
    return wrapper