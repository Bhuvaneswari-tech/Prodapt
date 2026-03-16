import time

# Decorator 1 → Authentication
def authenticate(func):
    def wrapper(*args, **kwargs):
        print("Checking user authentication...")
        user = kwargs.get("user")
        if user == "admin":
            return func(*args, **kwargs)
        else:
            print("Access Denied")
    return wrapper


# Decorator 2 → Logging
def log_request(func):
    def wrapper(*args, **kwargs):
        print(f"Logging: Function {func.__name__} called")
        return func(*args, **kwargs)
    return wrapper


# Decorator 3 → Execution Time
def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Execution Time:", round(end-start,5), "seconds")
        return result
    return wrapper


@authenticate
@log_request
@measure_time
def process_payment(amount, user=None):
    print("Processing payment of", amount)