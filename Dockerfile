ARG PYTHON_VERSION=3.9

FROM python:${PYTHON_VERSION} AS py3
FROM spark-base:3.2.0

COPY --from=py3 / /

RUN pip --no-cache-dir install \
    pyspark==3.2.0

WORKDIR /job
COPY src/. .


CMD [ "python", "main.py"]