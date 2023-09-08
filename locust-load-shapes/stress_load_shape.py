import math
from locust import LoadTestShape


class StressLoadShape(LoadTestShape):
    """
    Stress test stages

    2m -> 30 below normal load
    5m -> 30
    2m -> 60 normal load
    5m -> 60
    2m -> 80 around the breaking point
    5m -> 80
    2m -> 100 beyond the breaking point
    5m -> 100
    10m -> 0 scale down, Recovery stage

    Keyword arguments:

        stages -- A list of dicts, each representing a stage with the following keys:
            period -- When this many seconds pass the test is advanced to the next stage
            users -- Total user count
            spawn_rate -- Number of users to start/stop per second
            stop -- A boolean that can stop that test at a specific stage

        stop_at_end -- Can be set to stop once all stages have run.
    """

    stages = [
        {"period": 2 * 60, "users": 30, "spawn_rate": 1},
        {"period": 4 * 60, "users": 60, "spawn_rate": 1},
        {"period": 6 * 60, "users": 80, "spawn_rate": 1},
        {"period": 8 * 60, "users": 100, "spawn_rate": 1},
        {"period": 10 * 60, "users": 1, "spawn_rate": 1},
    ]

    def tick(self):
        run_time = self.get_run_time()

        for stage in self.stages:
            if run_time < stage["period"]:
                tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data

        return None

