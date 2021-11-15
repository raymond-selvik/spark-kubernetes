ARG OPENJDK_VERSION=11

FROM openjdk:${OPENJDK_VERSION}

ARG SPARK_VERSION=3.2.0
ARG HADOOP_VERSION=3.2
ARG spark_uid=185

ENV DEBIAN_FRONTEND=noninteractive

RUN wget https://dlcdn.apache.org/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz -O spark.tgz && \
    mkdir spark && \
    tar -xvf spark.tgz --strip-components=1 -C spark && \
    rm spark.tgz

RUN set -ex && \
    sed -i 's/http:\/\/deb.\(.*\)/https:\/\/deb.\1/g' /etc/apt/sources.list && \
    apt-get update && \
    ln -s /lib /lib64 && \
    apt install -y bash tini libc6 libpam-modules krb5-user libnss3 procps && \
    mkdir -p /opt/spark && \
    mkdir -p /opt/spark/examples && \
    mkdir -p /opt/spark/work-dir && \
    touch /opt/spark/RELEASE && \
    rm /bin/sh && \
    ln -sv /bin/bash /bin/sh && \
    echo "auth required pam_wheel.so use_uid" >> /etc/pam.d/su && \
    chgrp root /etc/passwd && chmod ug+rw /etc/passwd && \
    rm -rf /var/cache/apt/*

RUN cp -r spark/jars /opt/spark/jars &&\
    cp -r spark/bin /opt/spark/bin &&\
    cp -r spark/sbin /opt/spark/sbin &&\
    cp -r spark/kubernetes/dockerfiles/spark/entrypoint.sh /opt/  &&\
    cp -r spark/kubernetes/dockerfiles/spark/decom.sh /opt/ &&\
    cp -r spark/examples /opt/spark/examples &&\
    cp -r spark/kubernetes/tests /opt/spark/tests

ENV SPARK_HOME /opt/spark

WORKDIR /opt/spark/work-dir
RUN chmod g+w /opt/spark/work-dir
RUN chmod a+x /opt/decom.sh

## Install Python
RUN mkdir ${SPARK_HOME}/python
RUN apt-get update && \
    apt install -y python3 python3-pip && \
    pip3 install --upgrade pip setuptools && \
    rm -r /root/.cache && rm -rf /var/cache/apt/*

RUN cp -r /spark/python/pyspark ${SPARK_HOME}/python/pyspark
RUN cp -r /spark/python/lib ${SPARK_HOME}/python/lib

WORKDIR /
RUN rm -r spark

ENTRYPOINT [ "/opt/entrypoint.sh" ]
USER ${spark_uid}
