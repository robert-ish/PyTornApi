class TornAPIError(Exception):
    pass
class RateLimitError(TornAPIError):
    pass
class InvalidKeyError(TornAPIError):
    pass
class TornAPIResponseError(TornAPIError):
    pass