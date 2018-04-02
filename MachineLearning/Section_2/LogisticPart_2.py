import csv
import math
import random

def load_data(filename):
    dataset = []
    
    with open(filename,'r') as file:
        reader = csv.reader(file)
        
        for row in reader:
            dataset.append(row)
    
    return dataset

def str_to_float(dataset):
    
    for row in range(len(dataset)):
        for col in range(len(dataset[0])):
            dataset[row][col] = float(dataset[row][col].strip())

def minmax_data(dataset):
    minmax = []
    
    for i in range(len(dataset[0])):
        col_values = [row[i] for row in dataset]
        min_value = min(col_values)
        max_value = max(col_values)
        minmax.append([min_value, max_value])
    
    return minmax

def normalize_data(dataset, minmax):
    numer = 0
    denom = 0
    
    for row in dataset:
        for i in range(len(row)):
            numer = row[i] - minmax[i][0]
            denom = minmax[i][1] - minmax[i][0]
            row[i] = numer/denom

def cross_validation(dataset, n_folds):
    dataset_split = []
    dataset_copy = list(dataset)
    fold_size = int(len(dataset) / n_folds)
    for i in range(n_folds):
        fold = []
        while len(fold) < fold_size:
            index = random.randrange(len(dataset_copy))
            fold.append(dataset_copy.pop(index))
        dataset_split.append(fold)
    
    return dataset_split

def accuracy_score():
    pass

def evaluate_alogorithm():
    pass

def predict():
    pass

def sgd_logistic():
    pass

def logistic_regression():
    pass

filename = 'pima-indians-diabetes.data.csv'
dataset = load_data(filename)
str_to_float(dataset)
minmax = minmax_data(dataset)
normalize_data(dataset, minmax)

#c = cross_validation(dataset, 5)
e = cross_validation(dataset, 5)
