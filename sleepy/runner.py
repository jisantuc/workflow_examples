import random
import os

vals = [random.random() * 20. for _ in range(25)]

for v in vals:
    os.system('python sleepytime.py SleepyTime --seconds {} &'.format(v))
