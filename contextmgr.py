class ContextManagerClass:
    def __init__(self, generator_func):
        self.generator = generator_func

    def __enter__(self):
        try:
            return next(self.generator)
        except StopIteration:
            raise RuntimeError("Generator didn't yield")

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            next(self.generator)
        except StopIteration :
            return False
        else:
            raise RuntimeError("Generator function not finished")

def contextmanager(func):
    def wrapper(*args, **kwargs):
        return ContextManagerClass(func(*args, **kwargs))
    return wrapper

@contextmanager
def generate():
    print("started the function")
    result="the value are executed"
    yield result
    print("end the execution")

if __name__ == '__main__':
    with generate() as g:
        print(g)