# Python application under tests

## Docker development

### Build the image
```bash
docker-compose build app-development --no-cache
```

### Run the container
```bash
docker-compose up app-development -d
```

### How to enter the container
```bash
docker exec -it python-sut-dev sh
```

### Run application inside the container

```bash
FLASK_APP=app.py flask run -h 0.0.0 -p 5000
```

## Build production image

### Build the image
```bash
docker-compose build
```

### Run container
```bash
docker-compose up app-production -d
```