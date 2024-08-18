import sys

import pytest


class MyPlugin:
    def pytest_sessionfinish(self):
        print("*** test run reporting finishing")


if __name__ == "__main__":
    """
    python src/main/myinvoke.py
    """
    sys.exit(pytest.main(["-qq"], plugins=[MyPlugin()]))