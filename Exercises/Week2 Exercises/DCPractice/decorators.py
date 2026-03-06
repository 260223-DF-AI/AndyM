from functools import wraps, cache
import time

def timer(func):
    """
    Measure and print function execution time.
    
    Usage:
        @timer
        def slow_function():
            time.sleep(1)
    
    Output: "slow_function took 1.0023 seconds"
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        s =time.time()
        res = func(*args, **kwargs)
        e = time.time()
        print(f"{func.__name__} took {e-s} seconds")
        return res
    return wrapper



#### Task 1.2: Logger Decorator (20 min)

def logger(func):
    """
    Log function calls with arguments and return value.
    
    Usage:
        @logger
        def add(a, b):
            return a + b
        
        add(2, 3)
    
    Output:
        "Calling add(2, 3)"
        "add returned 5"
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_str = ",".join(str(arg) for arg in args)
        kwargs_str = ",".join(str(value) for arg,value in kwargs)
        print(f"Calling {func.__name__}({args_str}{kwargs_str})")
        val = func(*args, **kwargs)
        print(f"{func.__name__} returned {val}")
        return val
    return wrapper


#### Task 1.3: Retry Decorator with Arguments (30 min)

def retry(max_attempts=3, delay=1, exceptions=(Exception,)):
    """
    Retry a function on failure.
    
    Args:
        max_attempts: Maximum number of retry attempts
        delay: Seconds to wait between retries
        exceptions: Tuple of exceptions to catch
    
    Usage:
        @retry(max_attempts=3, delay=0.5)
        def flaky_api_call():
            # might fail sometimes
            pass
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(max_attempts):
                try:
                    val = func(*args, **kwargs)
                    return val
                except exceptions: # failed, try again after delay
                    time.sleep(delay)
            raise Exception# max attempts reached raise error
        return wrapper
    return decorator

#### Task 1.4: Cache Decorator (30 min)

def cache(max_size=128):
    """
    Cache function results.
    Similar to lru_cache but with visible cache inspection.
    
    Usage:
        @cache(max_size=100)
        def expensive_computation(x):
            return x ** 2
        
        expensive_computation(5)  # Computes
        expensive_computation(5)  # Returns cached
        
        # Inspect cache
        expensive_computation.cache_info()
        expensive_computation.cache_clear()
    """
    @cache(max_size=max_size)
    def decorator(func):
        @wraps
        def wrapper(*args, **kwargs):
            val = func(*args,**kwargs)
            return val
        return wrapper
    return decorator