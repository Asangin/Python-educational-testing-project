# Service under Performance test

## Locust

>[Locust documentation](https://docs.locust.io/en/stable/index.html)

### Structure

> [Load Shape Documantation](https://docs.locust.io/en/stable/custom-load-shape.html)

[locust-scripts](locust-scripts) contains all the scenarios to do performance testing written on Python using Locust
library
[locust-load-shapes](locust-load-shapes) contains different custom load shapes for performance scenarios

### Basic scenario

Run basic scenario with GUI just typing `locust` which will pick [locustfile.py](locustfile.py) or by custom specifying
locust scenario:

```bash
locust -f locust-scripts/basic_user_scenario.py
```

Run basic scenario with custom load shape:

step load shape
```bash
locust -f locust-scripts/basic_user_scenario.py,locust-load-shapes/step_load_shape.py
```

Stress load shape
```bash
locust -f locust-scripts/basic_user_scenario.py,locust-load-shapes/stress_shape.py
```
![Stress test load shape](img/stress_test_user_load_shape.png)

Spike load shape
```bash
locust -f locust-scripts/basic_user_scenario.py,locust-load-shapes/spike_shape.py
```
![Spike load shape](img/spike_load_shape.png)

Load shape
```bash
locust -f locust-scripts/basic_user_scenario.py,locust-load-shapes/load_shape.py
```
![Load shape](img/load_shape.png)

Soak shape
```bash
locust -f locust-scripts/basic_user_scenario.py,locust-load-shapes/soak_shape.py
```

## Service under test written in Flask

### Run server

```bash
python app.py
```

### Request, response examples

User login

```bash
curl --location --request POST 'http://127.0.0.1:5000/api/v1/login' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "batman",
    "password": "password"
}'
```

Response example:

```json
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2MzIyNzcyNywianRpIjoiNDNiM2EzYjAtNzFiNS00NjFlLTk5YWYtNzljYzQyOTI5MGZkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InRlc3QiLCJuYmYiOjE2NjMyMjc3MjcsImV4cCI6MTY2MzIyODYyN30.A0OHY0qK5Tc8BDMSC5kLYhA69zme0pn08kHcoW5rmUE"
}
```

- go to my_user_id url with access token

```bash
curl --location --request GET 'http://127.0.0.1:5000/my_user_id' \
--header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY2MzIyNzcyNywianRpIjoiNDNiM2EzYjAtNzFiNS00NjFlLTk5YWYtNzljYzQyOTI5MGZkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InRlc3QiLCJuYmYiOjE2NjMyMjc3MjcsImV4cCI6MTY2MzIyODYyN30.A0OHY0qK5Tc8BDMSC5kLYhA69zme0pn08kHcoW5rmUE'
```

Response example

```json
{
  "logged_in_as": "1"
}
```

- Get all users (public)

```bash
curl --location --request GET 'http://127.0.0.1:5000/public/api/v1/users'
```

Response example:

```json
[
  {
    "full_name": "Bruce Wayne",
    "id": 1,
    "username": "batman"
  },
  {
    "full_name": "Ann Takamaki",
    "id": 2,
    "username": "panther"
  },
  {
    "full_name": "Jester Lavore",
    "id": 3,
    "username": "little_sapphire"
  }
]
```