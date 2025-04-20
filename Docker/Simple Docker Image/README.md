# Simple Docker Image

This excercise creates a simple docker container that runs a python script to print hello world.

## Create image

We can use a docker image as a base and then create our own custom image.

```bash
docker build -t hello-world-python:v0.0.1 ./
```

```bash
REPOSITORY           TAG       IMAGE ID       CREATED         SIZE

hello-world-python   v0.0.1    e11f9657153d   5 seconds ago   48.3MB
```

## Run a container with the image

To run a container which will use the image, execute the following command:

```bash
docker run hello-world-python:v0.0.1
```

```bash
Hello World
```