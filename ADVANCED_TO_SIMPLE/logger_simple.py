"""
Simplified version of logger.py

ORIGINAL (Advanced): Custom decorator with manual file writing,
sys.exit() on errors, raw exception handling with sys.exc_info().

SIMPLIFIED: Uses Python's built-in logging module and a cleaner
decorator pattern. No sys.exit(), graceful error handling.
"""

import logging
import functools

# Set up a file logger
logging.basicConfig(
    filename="log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)


def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Log function call with arguments
        logging.info(f"Calling {func.__name__}(args={args}, kwargs={kwargs})")

        try:
            result = func(*args, **kwargs)
            logging.info(f"{func.__name__} returned: {result} (type: {type(result).__name__})")
            return result
        except Exception as e:
            logging.error(f"{func.__name__} raised {type(e).__name__}: {e}")
            raise

    return wrapper
