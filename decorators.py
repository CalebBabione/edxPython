def announce(f):
    def wrapper():
        print("about to run the function...")
        f()
        print("done with the function.")
    return wrapper()

def square (x):
    return x * x

@announce
def test():
    for i in range(10):
        print(f"the square root of {i} is {square(i)}")

           