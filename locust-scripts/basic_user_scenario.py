import math

from locust import HttpUser, TaskSet, between, task


class UserTasks(TaskSet):
    @task
    def get_root(self):
        self.client.get("/public/api/v1/users")


class WebUser(HttpUser):
    host = "http://127.0.0.1:5000"
    wait_time = between(3, 10)
    tasks = [UserTasks]