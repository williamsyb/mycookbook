img_ver=v1
img_name=iris_demo

build:
	docker build -t $(img_name):$(img_ver) .
	docker image ls | grep $(img_name)

export:
	docker save -o ../$(img_name)$(img_ver).tar $(img_name):$(img_ver)

debug:
	docker run -it --rm --name "iris_instance" -p 8080:8080 --entrypoint "/go/bin/iris" $(img_name):$(img_ver)

