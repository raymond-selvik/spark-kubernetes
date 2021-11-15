FROM ubuntu:21.10

ARG SPARK_VERSION=3.2.0
ARG HADOOP_VERSION=3.2
ARG spark_uid=185

RUN apt-get update && \
    apt install -y wget bash tini libc6 libpam-modules krb5-user libnss3 procps 

RUN apt-get update && \
    apt install -y default-jre ca-certificates-java ca-certificates


RUN wget https://dlcdn.apache.org/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz -O spark.tgz && \
    mkdir spark && \
    tar -xvf spark.tgz --strip-components=1 -C spark && \
    rm spark.tgz

ENV SPARK_HOME=/spark
ENV PATH="$PATH:/$SPARK_HOME/bin"

ENTRYPOINT [ "/spark/kubernetes/dockerfiles/spark/entrypoint.sh" ]

#ENTRYPOINT ["tail", "-f", "/dev/null"]
# Specify the User that the actual main process will run as
#USER ${spark_uid}
