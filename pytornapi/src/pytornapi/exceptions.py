class TornAPIError(Exception):
    """torn api error"""
    pass
class RateLimitError(TornAPIError):
    """happens when you hit the rate limit of 100 requests per minute."""
    pass
class InvalidKeyError(TornAPIError):
    """happens when you enter an invalid key when using TornAPI()"""
    pass
class TornAPIResponseError(TornAPIError):
    """happens when torn api doesnt respond"""
    pass