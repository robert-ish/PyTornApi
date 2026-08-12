"""**PyTornAPI**\n
An API wrapper for Torn API.
Provides methods to fetch data from Torn's public API endpoints.\n

this has enums btw

**Usage**:
Import tornapi

client = TornAPI("YOUR_API_KEY")|
items = client.get_torn('', TornField.ITEMS):

Torn's API returns JSON strings, by the way.

For help, visit api.torn.com

api.torn.com's swagger (v2) has lists of every selection for every method here.
"""

from .exceptions import TornAPIError
from .exceptions import TornAPIResponseError
from .exceptions import InvalidKeyError
from .exceptions import RateLimitError

from .client import TornAPI

from .enums import UserField
from .enums import PropertyField
from .enums import FactionField
from .enums import CompanyField
from .enums import MarketField
from .enums import TornField

__all__ = ["TornAPI", "TornAPIError", "TornAPIResponseError", "InvalidKeyError", "RateLimitError",
           "UserField", "PropertyField", "FactionField", "CompanyField", "MarketField", "TornField"]
