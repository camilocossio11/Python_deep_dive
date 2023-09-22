import time

def time_it (fn, *args, rep=1, **kwargs):
    start = time.perf_counter()
    for i in range (rep):
        fn(*args, **kwargs)
    end = time.perf_counter()
    return f'It takes {end - start} seconds (the function was called {rep} times)'