def read_last(lines, file):
    if lines > 0:
        with open(file) as text:
            file_lines = text.readlines()[-lines:]
        for line in file_lines:
            print(line.strip())


rows = int(input('Enter number of lines: '))
read_last(rows, 'text.txt')
