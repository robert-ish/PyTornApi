# handles rate limits but might be a bit inconvinient since you have to wait.
import PyTornApi as pt
import time

def try_call(func, *args):
  try:
    func(*args)
  except pt.RateLimitError as e:
    time.sleep(int(e.retry_after)+0.1) # yes, you can do this
    func(*args)
