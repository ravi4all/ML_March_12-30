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

def accuracy_score(actual,predicted):
    correct = 0
    for i in range(len(predicted)):
        if actual[i] == predicted[i]:
            correct += 1
    return correct / len(actual) * 100

def predict(row, coef):
    yhat = coef[0]
    for i in range(len(row) - 1):
        yhat += coef[i + 1] * row[i]
    return 1 / (1 + math.exp(-yhat))

def evaluate_alogorithm(dataset,algorithm,n_folds,learning_rate,epoch,*args):
    scores = []
    folds = cross_validation(dataset,n_folds)
    for fold in folds:
        train = list(folds)
        train.remove(fold)
        train = sum(train, [])
        test = []
        for row in fold:
            row_copy = list(row)
            test.append(row_copy)
            row_copy[-1] = None
        prediction = algorithm(train,test,learning_rate,epoch)
        actual = [row[-1] for row in fold]
        score = accuracy_score(actual, prediction)
        scores.append(score)
    return scores
    

def sgd_logistic(dataset, nb_epochs, learning_rate):
    coef = [0 for i in range(len(dataset))]
    for epoch in range(nb_epochs):
        for row in dataset:
            ycap = predict(row, coef)
            error = row[-1] - ycap
            coef[0] = coef[0] + learning_rate * error * (1 - ycap)
            for i in range(len(row) - 1):
                coef[i+1] = coef[i+1] + learning_rate * error * (1 - ycap) * row[i]
        print("Epoch :",epoch,"Prediction :",error)
    return coef
    

def logistic_regression(train,test,learning_rate,epoch):
    predictions = []
    coef = sgd_logistic(train,epoch,learning_rate)
    for row in test:
        pred = predict(row,coef)
        pred = round(pred)
        predictions.append(pred)
    return predictions

filename = 'pima-indians-diabetes.data.csv'
dataset = load_data(filename)
str_to_float(dataset)
minmax = minmax_data(dataset)
normalize_data(dataset, minmax)

#c = cross_validation(dataset, 5)
e = cross_validation(dataset, 5)
#coef = sgd_logistic(dataset,100,0.01)

n_folds = 5
learning_rate = 0.01
epoch = 10000
scores = evaluate_alogorithm(dataset,logistic_regression,n_folds,learning_rate,epoch)
mean_accuracy = sum(scores) / len(scores)
print("Accuracy :",mean_accuracy)