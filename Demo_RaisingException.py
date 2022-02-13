try:
    raise NameError("Hi There...")
except NameError:
    print("A name Error exception has been raised")
    raise
