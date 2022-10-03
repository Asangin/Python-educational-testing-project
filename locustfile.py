from locust import HttpUser, between, task

class WebUser(HttpUser):
    wait_time = between(3, 10)

    