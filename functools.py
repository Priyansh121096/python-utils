def map_args(*args1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            args = list(args)         # convert args to a list here
            for i in range(len(args)):
                args[i] = args1[i](args[i])
            result = func(*args, **kwargs)  # *args works for both tuples and lists
            return result
        return wrapper
    return decorator
