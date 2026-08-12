# handles rate limits but might be a bit inconvinient since you have to wait.
import PyTornApi

def try_call(func, *args):
  try:
    func(*args)
  except RateLimitError as e:
    time.sleep(e.retry_after) # yes, you can do this
    func(*args)
