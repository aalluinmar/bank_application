from typing import Callable

from tenacity import retry, stop_after_attempt, RetryCallState, RetryError

from services import utils


def before_retry(retry_state: RetryCallState):
    """Prints a message before each retry."""
    if retry_state.attempt_number > 1:
        print(f"      Note: You have only {4 - retry_state.attempt_number} attempts left.")


def retry_wrapper(attempts: int = 3):
    """
    A decorator that applies retry logic to a function.
    
    :param attempts: Number of retry attempts before failing.
    """
    def decorator(func: Callable):
        return retry(stop=stop_after_attempt(attempts), before=before_retry)(func)
    return decorator


def retry_wrapper(attempts: int = 3):
    """
    A decorator that applies retry logic to a function and handles failures.
    
    :param attempts: Number of retry attempts before failing.
    """
    def decorator(func: Callable):
        def wrapped_function(*args, **kwargs):
            try:
                return retry(stop=stop_after_attempt(attempts), before=before_retry)(func)(*args, **kwargs)
            except (RetryError, ValueError):
                # Handle retries exceeded case gracefully
                utils.typewriter_effect("\n     ❌ Maximum attempts reached for this session. Exiting the application process. 😞\n\n\n")
                exit()  # Exit the program gracefully
        return wrapped_function
    return decorator
