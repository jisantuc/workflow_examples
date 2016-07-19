import os
import luigi
from luigi.parameter import FloatParameter
from luigi.task import Task
import random

class SleepyTime(Task):

    seconds = FloatParameter(default=3.)

    def run(self):
        os.system('sleep {}'.format(self.seconds))

if __name__ == '__main__':
    luigi.run()
