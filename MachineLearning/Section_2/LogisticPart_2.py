import csv

file = open('pima-indians-diabetes.data.csv')
reader = csv.reader(file)
dataset = []
for data in reader:
    dataset.append(data)

X = []
y = []

for i in dataset:
    X.append(i[:-1])
    y.append(i[-1])