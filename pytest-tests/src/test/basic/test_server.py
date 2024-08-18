import pytest


@pytest.mark.webtest
def test_send_http():
    """
    Run this test by passing mark @webtest
    pytest -v -m webtest
    Or the inverse, running all tests except the webtest ones:
    pytest -v -m "not webtest"
    """
    pass  # perform some webtest test for your app


@pytest.mark.device(serial="123")
def test_something_quick():
    """
    Run this particular test, specifying "device" mark and "123" serial
    pytest -v -m "device(serial='123')"
    """
    pass


@pytest.mark.device(serial="abc")
def test_another():
    pass


class TestClass:
    def test_method(self):
        pass