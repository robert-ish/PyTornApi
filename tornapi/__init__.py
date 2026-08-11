"""**TornAPI**\n
An API wrapper for Torn API.
Provides methods to fetch data from Torn's public API endpoints.\n
Handles rate limiting, authentication, and error handling automatically.

**Usage**:

client = TornAPI("YOUR_API_KEY")|
items = client.get_torn('', 'items'):

Torn's API returns JSON strings, by the way.

For help, visit api.torn.com

api.torn.com's swagger (v2) has lists of every selection for every method here.
"""

from .exceptions import TornAPIError
from .exceptions import TornAPIResponseError
from .exceptions import InvalidKeyError
from .exceptions import RateLimitError
from .client import TornAPI