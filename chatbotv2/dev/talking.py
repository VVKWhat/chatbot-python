from db_bot import *
from colors import *
import time
import random
def usr_talk(ask):
    while ask:
        if ask in start:
            print(random.choice(privet))
        if "stop" in ask:
            break
