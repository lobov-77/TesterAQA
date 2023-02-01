import pytest


@pytest.fixture(scope='class', autouse=True)
def class_fixture():
    print("Let's start")
    yield
    print("The end")