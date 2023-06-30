from django.http import HttpResponse

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Create a Fibonacci number generator object
fib_gen = fibonacci_generator()

def get_next_fibonacci(request):
    next_fib = next(fib_gen)
    return HttpResponse(str(next_fib))