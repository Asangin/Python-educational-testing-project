import pytest

@pytest.fixture(scope="session")
def image_file(tmp_path_factory):
    img = "compute_expensive_image()"
    fn = tmp_path_factory.mktemp("data") / "img.png"
    img.save(fn)
    return fn


# contents of test_image.py
def test_histogram(image_file):
    # img = load_image(image_file)
    pass