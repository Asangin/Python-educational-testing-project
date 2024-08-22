# PyTest tutorial

> [Pytest documentation](https://docs.pytest.org/en/stable/)

## Basic

### Test samples

```bash
pytest src/test/basic/test_sample.py
```

### Assert certain exception is raised

```bash
pytest src/test/basic/test_sysexit.py
```

```bash
pytest src/test/basic/test_exceptiongroup.py
```

### Group multiple tests in a class

```bash
pytest -q src/test/basic/test_class.py
```

```bash
pytest -q src/test/basic/test_class_demo.py
```

```bash
pytest src/test/basic -k TestClassDemoInstance -q
```

### Request a unique temporary directory for functional tests

```bash
pytest -q src/test/basic/test_tmp_path.py
```

## How to invoke pytest

### Run all tests

```bash
pytest
```

### Run particular module

```bash
pytest pytest src/test/basic/test_sample.py
```

### Run tests in a directory

```bash
pytest src/test/basic/
```

### To run a specific test within a module

```bash
pytest src/test/assert/test_assert1.py::test_match
```

### To run all tests in a class

```bash
pytest src/test/basic/test_class.py::TestClass
```

### Specifying a specific test method

```bash
pytest src/test/basic/test_class.py::TestClass::test_one
```

### Profiling test execution duration (Changed in version 6.0)

```bash
pytest --durations=10 --durations-min=1.0
```

## How to write and report assertions in tests

### Different assertion and about expected exceptions

```bash
pytest src/test/assert/test_assert1.py
```

### Context-sensitive comparisons assertion

```bash
pytest src/test/assert/test_assert2.py
```

### Custom comparison assertion

```bash
pytest src/test/assert/test_foocompare.py
```

## How to use fixtures

```bash
pytest src/test/fixtures/test_append.py
```

### Sharing fixtures

```bash
pytest src/test/fixtures/test_module.py
```

### Fixtures teardown/cleanup

```bash
pytest -q src/test/fixtures/test_emaillib.py
```

### Test finalizer

```bash
pytest -s src/test/fixtures/test_finalizers.py
```

## How to parametrize fixtures and test functions

```bash
pytest src/test/parametrize/test_expectation.py
```

## How to use temporary directories and files in tests

```bash
pytest src/test/temporary_directories/test_tmp_path.py
```