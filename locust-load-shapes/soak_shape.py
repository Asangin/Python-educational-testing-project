import math
from locust import LoadTestShape


class SoakShape(LoadTestShape):
    """
    Soak test stages

    2m -> 70 simulates ramp-up of traffic from 1 to 100 over 5 minutes
    4h -> 70 stays at normal load for 10 minutes
    2m -> 0 ramp-down to 0 users during 5m

    Keyword arguments:

        stages -- A list of dicts, each representing a stage with the following keys:
            period -- When this many seconds pass the test is advanced to the next stage
            users -- Total user count
            spawn_rate -- Number of users to start/stop per second
            stop -- A boolean that can stop that test at a specific stage

        stop_at_end -- Can be set to stop once all stages have run.
    """

    stages = [
        {"period": 2 * 60, "users": 60, "spawn_rate": 2},
        {"period": 4 * 60 * 60, "users": 60, "spawn_rate": 1},
        {"period": 2 * 60 + 4 * 60 * 60, "users": 1, "spawn_rate": 2},
    ]

    def tick(self):
        run_time = self.get_run_time()

        for stage in self.stages:
            if run_time < stage["period"]:
                tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data

        return None