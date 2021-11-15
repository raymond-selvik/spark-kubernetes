SPARK_IMAGE=spark-executor:3.2.0
PYSPARK_IMAGE=pyspark-executor:3.2.0
JOB_IMAGE=testjob:0.1

build-spark:
	sudo docker build -t ${SPARK_IMAGE} ./docker-images/spark-executor-image/.
	##sudo docker build -t ${PYSPARK_IMAGE} ./docker-images/pyspark-executor-image/.

build:
	sudo docker build -t ${JOB_IMAGE} .

#run: build
#	sudo docker run ${JOB_IMAGE}

run:
	cd src && python main.py

kube-deploy: build
	kubectl apply -f spark-job/service.yaml
	kubectl apply -f spark-job/pod.yaml
	kubectl logs spark-job-pod   


kube-clean:
	kubectl delete -f spark-job/service.yaml
	kubectl delete -f spark-job/pod.yaml
	kubectl delete pods --all






