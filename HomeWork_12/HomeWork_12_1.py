def is_power_of_two(number: int, iteration: int = 1):
    new_number = number / 2

    _result = False

    if new_number == 2:
        return True

    elif new_number.is_integer():
        _result = is_power_of_two(new_number, iteration + 1)

    return _result


result = is_power_of_two(125)

print('yes' if result else 'no')
