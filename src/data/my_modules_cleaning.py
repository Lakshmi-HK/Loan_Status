import pandas as pd


def load_df(path):
    df = pd.read_csv(path)
    print('Data uploaded sucessfully')
    return df

def check_null_values(df):
    null_values = df.isnull().sum()
    return print(null_values)

def drop_null_values(df):
    df = df.dropna()
    return df

def save_df(df):
    df_1 = df.to_csv('cleaned_df.csv')
    print('Data saves sucessfully')
    return df_1

def remove_grade_outlier(value):
    if value not in ['B', 'A', 'C', 'D', 'E']:
        return 'E'
    else:
        return value

def remove_purpose_outlier(value):
    if value not in ['debt_consolidation', 'credit_card', 'home_improvement', 'other', 'major_purchase', 'small_business', 'car']:
        return 'other'
    else:
        return value

def remove_loanstatus_outlier(value):
    if value not in ['Fully Paid', 'Charged Off']:
        return 'Charged Off'
    else:
        return value

def remove_ownership_outlier(value):
    if value not in ['RENT', 'MORTGAGE']:
        return 'MORTGAGE'
    else:
        return value

