def authenticate(role):

    def decorator(func):

        def wrapper(user):
            if user == role:
                return func(user)
            else:
                print("Access Denied")

        return wrapper

    return decorator


@authenticate("admin")
def dashboard(user):
    print("Welcome to admin dashboard")


dashboard("admin")
dashboard("guest")