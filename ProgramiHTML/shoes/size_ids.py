import csv

def load_size_id(shoeSize, path="../info/numsId.csv"):
    dict = {}
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)  # skip the header
        for size, testid in reader:
            dict[size] = testid
    return dict[shoeSize]