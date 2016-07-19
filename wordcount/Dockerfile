FROM java:8

ENV SCALA_VERSION 2.11.7
ENV SBT_VERSION 0.13.11
ENV AWS_ACCESS_KEY_ID YOUR_KEY_HERE
ENV AWS_SECRET_ACCESS_KEY YOUR_KEY_HERE
ENV SPARK_HOME=spark-1.6.2-bin-hadoop2.4


RUN \
    curl -fsL http://downloads.typesafe.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz | tar xfz - -C /root/ && \
    echo >> /root/.bashrc && \
    echo 'export PATH=~/scala-$SCALA_VERSION/bin:$PATH' >> /root/.bashrc

RUN \
    curl -L -o sbt-$SBT_VERSION.deb http://dl.bintray.com/sbt/debian/sbt-$SBT_VERSION.deb && \
    dpkg -i sbt-$SBT_VERSION.deb && \
    rm sbt-$SBT_VERSION.deb && \
    apt-get update && \
    apt-get install sbt && \
    sbt sbtVersion

RUN \
    wget http://apache.claz.org/spark/spark-1.6.2/$SPARK_HOME.tgz && \
    tar xvf $SPARK_HOME.tgz && \
    echo 'export PATH=$PATH:$SPARK_HOME/bin/'


RUN apt-get update && apt-get install -y \
    python-dev \
    python-pip

COPY requirements.txt /
COPY frankenstein250.txt /
COPY wordcount.py /
COPY wordcount.sbt /
COPY src/ /src/
COPY luigi.cfg /

RUN pip install -r requirements.txt
RUN sbt package

RUN python -c "import os; print 'lolz' if os.path.exists('frankenstein250.txt') else ':('"
RUN python -c "import os; print 'lolz' if os.path.exists('/spark-1.6.2') else ':('"

RUN PYTHONPATH='' luigi RunAll --module wordcount --input-file frankenstein250.txt
