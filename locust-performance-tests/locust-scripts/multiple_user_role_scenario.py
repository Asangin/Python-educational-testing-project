import math

from locust import HttpUser, LoadTestShape, between, task


class GuestUser(HttpUser):
    host = "http://127.0.0.1:5000"
    wait_time = between(3, 10)

    @task
    def get_user_list(self):
        self.client.get("/public/api/v1/users")


class RegularUser(HttpUser):
    host = "http://127.0.0.1:5000"
    wait_time = between(3, 10)

    def on_start(self):
        response = self.client.post("/api/v1/login", json={"username": "batman", "password": "password"})
        print("Response status code:", response.status_code)
        print("Response text:", response.text)
        body = response.json()
        self.client.access_token = body["access_token"]

    @task
    def who_am_i(self):
        headers = {'Authorization': f'Bearer {self.client.access_token}'}
        self.client.get("/api/v1/who_am_i", headers=headers)


class StagesShapeWithCustomUsers(LoadTestShape):
    """
    A simply load test shape class that has different user and spawn_rate at
    different stages.

    Keyword arguments:

        stages -- A list of dicts, each representing a stage with the following keys:
            duration -- When this many seconds pass the test is advanced to the next stage
            users -- Total user count
            spawn_rate -- Number of users to start/stop per second
            stop -- A boolean that can stop that test at a specific stage

        stop_at_end -- Can be set to stop once all stages have run.
    """

    stages = [
        {"duration": 60, "users": 10, "spawn_rate": 10, "user_classes": [GuestUser]},
        {"duration": 100, "users": 50, "spawn_rate": 10, "user_classes": [RegularUser]},
        {"duration": 180, "users": 100, "spawn_rate": 5, "user_classes": [GuestUser, RegularUser]},
        {"duration": 220, "users": 30, "spawn_rate": 10},
        {"duration": 230, "users": 10, "spawn_rate": 10},
        {"duration": 240, "users": 1, "spawn_rate": 1},
    ]

    def tick(self):
        run_time = self.get_run_time()

        for stage in self.stages:
            if run_time < stage["duration"]:
                # Not the smartest solution, TODO: find something better
                try:
                    tick_data = (stage["users"], stage["spawn_rate"], stage["user_classes"])
                except KeyError:
                    tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data

        return None
