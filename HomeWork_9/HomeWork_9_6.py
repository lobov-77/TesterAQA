with open("numbers_2.txt") as f:
    print(sum(int(x) for x in f.read().strip().split()))




