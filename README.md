# Python Basic Web App

A small Flask web application with a responsive page and a `/health` endpoint.
It runs with Gunicorn in a non-root Docker container.

## Build the image

```bash
git clone https://github.com/chandruramaraj10/devops.git
cd devops
sudo docker build -t python-basic-web:v1 .
```

## Run the container

```bash
sudo docker run \
  --name python-basic-web \
  -d \
  -p 8080:8000 \
  -e APP_NAME="My Python App" \
  -e APP_ENV="docker" \
  python-basic-web:v1
```

Open <http://localhost:8080> in a browser.

Check the health endpoint:

```bash
curl http://localhost:8080/health
```

View logs and container health:

```bash
sudo docker logs -f python-basic-web
sudo docker inspect python-basic-web --format '{{json .State.Health}}'
```

Stop and remove the container:

```bash
sudo docker stop python-basic-web
sudo docker rm python-basic-web
```
