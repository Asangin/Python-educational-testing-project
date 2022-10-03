# Flask test

## Run server

```bash
python -m flask run
```

## JWT

- login

```bash
curl --location --request POST 'http://127.0.0.1:5000/login' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "test",
    "password": "test"
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
