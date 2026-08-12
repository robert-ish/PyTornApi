class TornAPIError(Exception):
    """torn api error"""
    pass
class RateLimitError(TornAPIError):
    """happens when you hit the rate limit of 100 requests per minute."""
    def __init__(self, message, retry_after=None):
        super().__init__(message)
        self.retry_after = retry_after
class InvalidKeyError(TornAPIError):
    """happens when you enter an invalid key when using TornAPI()"""
    pass
class TornAPIResponseError(TornAPIError):
    """happens when torn api doesnt respond"""
    pass
class WrongReturnError(TornAPIError):
    """happens when torn api doesnt return JSON. Likely caused by cloudflare protection blocking you."""
    pass
