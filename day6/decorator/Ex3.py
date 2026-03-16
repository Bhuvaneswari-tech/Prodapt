#Logging Decorator
def log(level):

    def decorator(func):

        def wrapper(*args, **kwargs):
            print(f"[{level}] Executing {func.__name__}")
            return func(*args, **kwargs)

        return wrapper

    return decorator


@log("INFO")
def add(a, b):
    print(a + b)

add(5,3)

# Authentication Decorator
# Scenario
# Allow only admin users.