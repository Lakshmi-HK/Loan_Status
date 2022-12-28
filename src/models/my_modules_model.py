import pandas as pd
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score, confusion_matrix, roc_auc_score, ConfusionMatrixDisplay
import pickle
import matplotlib.pyplot as plt

def load_df(path):
    df = pd.read_csv(path)
    print('Data uploaded sucessfully')
    return df

def Train_model(x_train, y_train, model):
    model.fit(x_train, y_train)
    return print('model trained sucessfully')

def evalaute_model(y_test, predictions):
    print(f"Recall: {round(recall_score(y_test, predictions) * 100, 4)}")
    print(f"Precision: {round(precision_score(y_test, predictions) * 100, 4)}")
    print(f"F1-Score: {round(f1_score(y_test, predictions) * 100, 4)}")
    print(f"Accuracy score: {round(accuracy_score(y_test, predictions) * 100, 4)}")
    print(f"AUC Score: {round(roc_auc_score(y_test, predictions) * 100, 4)}")

def save_model(model):
    pickle.dump(model, open('../../models/model_random.sav', 'wb'))
    print('model saved')

def confusion_matrix(y_train_test, y_train_test_pred):
    conf = ConfusionMatrixDisplay.from_predictions(y_train_test, y_train_test_pred)
    return conf

def plot_precision_recall_vs_threshold(x_train_test, y_train_test):
    y_scores = model.predict_proba(x_train_test)[:, 1]
    precisions, recalls, thresholds = precision_recall_curve(y_train_test, y_scores_l_t)
    plt.figure(figsize=(12,6))
    plt.plot(thresholds, precisions[:-1], "b--", label="Precision")
    plt.plot(thresholds, recalls[:-1], "g-", label="Recall")
    plt.xlabel("Threshold")
    plt.legend(loc="upper left")
    plt.ylim([0, 1])

def plot_roc_curve(fpr, tpr, label=None):
    y_scores = model.predict_proba(x_train_test)[:, 1]
    fpr, tpr, thresholds = roc_curve(y_train, y_scores)
    plt.figure(figsize=(12,6))
    plt.plot(fpr, tpr, linewidth=2, label=label)
    plt.plot([0, 1], [0, 1], 'k--')
    plt.axis([0, 1, 0, 1])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')

