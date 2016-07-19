import os
from copy import deepcopy
import luigi
from luigi.parameter import Parameter
from luigi.s3 import S3Target, S3Client
from luigi.contrib.spark import SparkSubmitTask

VERSION = '0.0.1'

class UploadFile(luigi.Task):

    version = Parameter(default=VERSION)
    input_file = Parameter(default='frankenstein.txt')

    client = S3Client(os.getenv('AWS_ACCESS_KEY_ID'),
                      os.getenv('AWS_SECRET_ACCESS_KEY'))

    def run(self):
        self.client.put(self.input_file,
                        's3://test.objects/' + self.input_file)
        self.complete()

    def complete(self):
        if self.client.exists('s3://test.objects/' + self.input_file):
            return True
        return False


class CountWords(SparkSubmitTask):

    version = Parameter(default=VERSION)
    input_file = Parameter(default='frankenstein.txt')

    # basic config options from
    # https://github.com/spotify/luigi/blob/master/examples/pyspark_wc.py
    driver_memory = '2g'
    executor_memory = '3g'
    total_executor_cores = luigi.IntParameter(100, significant=False)

    name = 'SparkSubmit Word Count'
    app = 'target/scala-2.10/word-count_2.10-1.0.jar'

    def requires(self):
        return UploadFile(version=self.version, input_file=self.input_file)

    # define what to do with the output
    def output(self):
        return luigi.LocalTarget('wc_{}'.format(self.input_file))

    def input(self):
        return S3Target('s3n://test.objects/' + self.input_file)

    def app_options(self):
        return [self.input().path, self.output().path]

if __name__ == '__main__':
    luigi.run()
