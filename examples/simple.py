# gets a random user's bars
# i have no idea what bars does and why would i.
import PyTornApi as pt
import random
randomuserbars = pt.get_user(random.randint(1,999999), 'bars')
print(randomuserbars)
