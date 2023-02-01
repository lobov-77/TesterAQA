import pytest


@pytest.fixture(scope='function')
def function_fixture():
    print('\nStart parameterization test')
    yield
    print('\nFinish parameterization test')