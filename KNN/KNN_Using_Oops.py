
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import os
import sys

class KNN:
    def __init__(self, path):
        try:
            self.df = pd.read_csv(path)
            self.df = self.df.drop(self.df.columns[0], axis=1)
            self.df['diagnosis'] = self.df['diagnosis'].map({'M': 0, 'B': 1})
            self.X = self.df.iloc[:, 1:]
            self.y = self.df.iloc[:, 0]
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
                self.X, self.y, test_size=0.2, random_state=42)
        except Exception as e:
            er_type, er_msg, line_no = sys.exc_info()
            print(f'Error in line no: {line_no.tb_lineno} and Error Message: {er_msg}')

    def find_best_k(self):
        try:
            accuracy = []
            k_values = np.arange(3, 50, 2)
            for i in k_values:
                self.reg = KNeighborsClassifier(n_neighbors=i)
                self.reg.fit(self.X_train, self.y_train)
                accuracy.append(self.reg.score(self.X_test,self.y_test))
            best_k = k_values[accuracy.index(max(accuracy))]
            return best_k
        except Exception as e:
            er_type, er_msg, line_no = sys.exc_info()
            print(f'Error in line no: {line_no.tb_lineno} and Error Message: {er_msg}')

    def training(self, best_k):
        try:
            self.reg = KNeighborsClassifier(n_neighbors=best_k)
            self.reg.fit(self.X_train, self.y_train)
            self.y_train_pred = self.reg.predict(self.X_train)
            self.train = np.array(self.y_train)
            print(f'Confusion Matrix (Train):\n{confusion_matrix(self.train,self.y_train_pred)}')
            train_accuracy = accuracy_score(self.train, self.y_train_pred)
            print(f'Training Accuracy with k={best_k}: {train_accuracy}')
            print(f'Classification Report (Train):\n{classification_report(self.train,self.y_train_pred)}')
        except Exception as e:
            er_type, er_msg, line_no = sys.exc_info()
            print(f'Error in line no: {line_no.tb_lineno} and Error Message: {er_msg}')

    def testing(self, best_k):
        try:
            self.y_test_pred = self.reg.predict(self.X_test)
            self.test = np.array(self.y_test)
            print(f'Confusion Matrix (Test):\n{confusion_matrix(self.test,self.y_test_pred)}')
            test_accuracy = accuracy_score(self.test, self.y_test_pred)
            print(f'Testing Accuracy with k={best_k}: {test_accuracy}')
            print(f'Classification Report (Test):\n{classification_report(self.test, self.y_test_pred)}')
        except Exception as e:
            er_type, er_msg, line_no = sys.exc_info()
            print(f'Error in line no: {line_no.tb_lineno} and Error Message: {er_msg}')


if __name__ == "__main__":
    try:
        obj = KNN('D:\Lavanya\Classification\breast-cancer.csv')
        best_k = obj.find_best_k()
        print(f'\nBest k value found: {best_k}')
        obj.training(best_k)
        obj.testing(best_k)
    except Exception as e:
        er_type, er_msg, line_no = sys.exc_info()
        print(f'Error in line no: {line_no.tb_lineno} and Error Message: {er_msg}')

