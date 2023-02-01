import pytest


@pytest.mark.param
@pytest.mark.parametrize('cars', ['BMW', 'Mercedes', 'Audi', 'Rolls Royce'])
def test_solo_value(cars, function_fixture):
    print(f'\nAutomobile {cars}')
    assert True


@pytest.mark.param
@pytest.mark.parametrize('brand, model', [('BMW', 'X5'), ('Audi', 'A8'), ('Mercedes', 'C200')])
def test_pairs_value(brand, model, function_fixture):
    print(f'\n{model} is the model of {brand}')
    assert True


@pytest.mark.param
@pytest.mark.parametrize('val1, val2', [(1, ['a', 'b', 'c']), (1, 1.453), ({'a', 'b', 'c'}, True)],
                         ids=['int and list', 'int and float', 'set and bool'])
def test_info(val1, val2, function_fixture):
    assert True