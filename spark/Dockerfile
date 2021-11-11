ARG OPENJDK_VERSION=11

FROM openjdk:${OPENJDK_VERSION}

ARG SPARK_VERSION=3.2.0
ARG HADOOP_VERSION=3.2

RUN wget https://dlcdn.apache.org/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz -O spark.tgz && \
    mkdir spark && \
    tar -xvf spark.tgz --strip-components=1 -C spark && \
    rm spark.tgz

ENV SPARK_HOME=/spark
ENV PATH="$PATH:/$SPARK_HOME/bin"