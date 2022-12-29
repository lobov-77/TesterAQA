text = 'Function {} was called {} times.\n'
counter = {}


def call_times(file_name):
    def inner(func):
        def wrapper():
            wrapper.count += 1
            if not file_name in counter:
                counter[file_name] = {}
            counter[file_name][func.__name__] = wrapper.count
            with open(file_name, 'w') as f:
                for func_name, quantity in counter[file_name].items():
                    f.write(text.format(func_name, quantity))

            return func()

        wrapper.count = 0
        return wrapper

    return inner


@call_times('foo.txt')
def foo():
    pass


@call_times('foo.txt')
def boo():
    pass


@call_times('calls.txt')
def doo():
    pass


foo()
boo()
foo()
foo()
boo()
doo()

name_first_file = 'File foo.txt'
name_second_file = 'File calls.txt'

ffile = open('foo.txt').read()
second_file = open('calls.txt').read()

print(f'{name_first_file}:\n{ffile}\n{name_second_file}:\n{second_file}')