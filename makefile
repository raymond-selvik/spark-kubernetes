SPARK_IMAGE=sparkbase:3.2.0
JOB_IMAGE=testjob:0.1

build-spark:
	sudo docker build -t ${SPARK_IMAGE} spark/.

build:
	sudo docker build -t ${JOB_IMAGE} .

run: build
	sudo docker run ${JOB_IMAGE}




