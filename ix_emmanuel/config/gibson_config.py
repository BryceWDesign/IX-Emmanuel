"""
Gibson Configuration — IX-Emmanuel

Defines communication parameters for connecting IX-Emmanuel
to the IX-Gibson central intelligence node.
"""

# IX-Gibson API endpoint URL
GIBSON_API_URL = "http://localhost:9000/api/query"

# Timeout for API requests (seconds)
REQUEST_TIMEOUT_SECONDS = 5

# Retry attempts for failed requests
RETRY_ATTEMPTS = 3

# Backoff interval between retries (seconds)
RETRY_BACKOFF_SECONDS = 2
