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

def normalize_data():
    pass

def cross_validation():
    pass

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