import pytest


def return_tree():
    return 3


def test_function():
    assert return_tree() == 4


def test_assertion_with_message():
    a = 5
    assert a % 2 == 0, "value was odd, should be even"


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0


def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:
        def f():
            f()

        f()
    assert "maximum recursion" in str(excinfo.value)


def test_foo_not_implemented():
    def foo():
        raise NotImplementedError

    with pytest.raises(RuntimeError) as excinfo:
        foo()
    assert excinfo.type is RuntimeError


def myfunc():
    raise ValueError("Exception 123 raised")


def test_match():
    with pytest.raises(ValueError, match=r".* 123 .*"):
        myfunc()


def test_exception_in_group():
    with pytest.raises(ExceptionGroup) as excinfo:
        raise ExceptionGroup(
            "Group message",
            [
                RuntimeError("Exception 123 raised"),
            ],
        )
    assert excinfo.group_contains(RuntimeError, match=r".* 123 .*")
    assert not excinfo.group_contains(TypeError)


def test_exception_in_group_at_given_depth():
    with pytest.raises(ExceptionGroup) as excinfo:
        raise ExceptionGroup(
            "Group message",
            [
                RuntimeError(),
                ExceptionGroup(
                    "Nested group",
                    [
                        TypeError(),
                    ],
                ),
            ],
        )
    assert excinfo.group_contains(RuntimeError, depth=1)
    assert excinfo.group_contains(TypeError, depth=2)
    assert not excinfo.group_contains(RuntimeError, depth=2)
    assert not excinfo.group_contains(TypeError, depth=1)


def return_index_error():
    raise IndexError()


@pytest.mark.xfail(raises=IndexError)
def test_index_error():
    return_index_error()
