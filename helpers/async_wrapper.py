import asyncio

# Wrapper to use async functions inside of threads


def async_wrapper(func, *args):
    asyncio.run(func(*args))