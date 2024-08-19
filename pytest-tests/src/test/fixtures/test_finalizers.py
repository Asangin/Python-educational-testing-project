from functools import partial
import pytest

@pytest.fixture
def fix_w_finalizers(request):
    request.addfinalizer(partial(print, "finalizer_2"))
    request.addfinalizer(partial(print, "finalizer_1"))


def test_bar(fix_w_yield1, fix_w_yield2, fix_w_finalizers):
    print("test_bar")


@pytest.fixture
def fix_w_yield1():
    yield
    print("after_yield_1")


@pytest.fixture
def fix_w_yield2():
    yield
    print("after_yield_2")