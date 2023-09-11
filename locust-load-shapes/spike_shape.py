import math
from locust import LoadTestShape


class SpikeLoadShape(LoadTestShape):
    """
    Spike test stages

    10s -> 30 below normal load
    1m -> 30
    10s -> 100 spike to beyond the breaking point
    3m -> 100 stay beyond the breaking point
    10s -> scale down. Recovery stage
    3m -> 30 below normal load
    10s -> 0

    Keyword arguments:

        stages -- A list of dicts, each representing a stage with the following keys:
            period -- When this many seconds pass the test is advanced to the next stage
            users -- Total user count
            spawn_rate -- Number of users to start/stop per second
            stop -- A boolean that can stop that test at a specific stage

        stop_at_end -- Can be set to stop once all stages have run.
    """

    stages = [
        {"period": 10, "users": 30, "spawn_rate": 10},
        {"period": 10 + 1 * 60, "users": 30, "spawn_rate": 1},
        {"period": 20 + 1 * 60, "users": 100, "spawn_rate": 10},
        {"period": 20 + 5 * 60, "users": 100, "spawn_rate": 1},
        {"period": 30 + 5 * 60, "users": 30, "spawn_rate": 10},
        {"period": 30 + 8 * 60, "users": 30, "spawn_rate": 1},
        {"period": 40 + 8 * 60, "users": 1, "spawn_rate": 10},
    ]

    def tick(self):
        run_time = self.get_run_time()

        for stage in self.stages:
            if run_time < stage["period"]:
                tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data

        return None

