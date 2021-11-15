ARG PYTHON_VERSION=3.9

FROM python:${PYTHON_VERSION} AS py3
FROM spark-base:3.2.0

COPY --from=py3 / /

USER 0

#ENTRYPOINT [ "/spark/kubernetes/dockerfiles/spark/entrypoint.sh" ]
ENTRYPOINT ["tail", "-f", "/dev/null"]
# Specify the User that the actual main process will run as
ARG spark_uid=185
USER ${spark_uid}
