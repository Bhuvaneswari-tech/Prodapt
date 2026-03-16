import time

def timer(func):
    def wrapper():
        print("Starting the function...")
        start = time.time()
        func()
        end = time.time()
        print("Execution time:", end-start)
    return wrapper

@timer
def slow():
    time.sleep(5)

slow()
