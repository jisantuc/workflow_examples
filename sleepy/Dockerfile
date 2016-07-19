FROM ubuntu

RUN mkdir /sleepy
COPY requirements.txt /sleepy
COPY sleepytime.py /sleepy
COPY runner.py /sleepy

WORKDIR /sleepy

RUN apt-get update && apt-get install -y python-pip

RUN pip install -r requirements.txt

RUN PYTHONPATH='' luigi SleepyTime --module sleepytime --seconds 30 --local-scheduler
