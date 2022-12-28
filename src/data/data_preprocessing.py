import my_modules_cleaning
from sklearn.preprocessing import LabelEncoder

# loads cleaned dataset
path = '..\..\data\processed\Cleaned_dataset_encoded.csv'
# F:\TopMentor\Batch-63\Machine Learning\Portfolio Project -II\Loan_status_prediction_with_deployment\Loan_Status\data\processed\Cleaned_dataset_encoded.csv
df = my_modules_cleaning.load_df(path)

# values count of categorical data
print(df['purpose'].value_counts())
print(df['loan_status'].value_counts())
print(df['term'].value_counts())
print(df['home_ownership'].value_counts())
print(df['grade'].value_counts())

# Removes ouliers

# Employment length
mapping_dict = {
    "emp_length": {
        "10+ years": 10,
        "9 years": 9,
        "8 years": 8,
        "7 years": 7,
        "6 years": 6,
        "5 years": 5,
        "4 years": 4,
        "3 years": 3,
        "2 years": 2,
        "1 year": 1,
        "< 1 year": 0,
        "n/a": 0
    }
}
df = df.replace(mapping_dict)
# purpose
df['purpose'] = df['purpose'].apply(my_modules_cleaning.remove_purpose_outlier)
# loan_status
df['loan_status'] = df['loan_status'].apply(my_modules_cleaning.remove_loanstatus_outlier)
# home_ownership
df['home_ownership'] = df['home_ownership'].apply(my_modules_cleaning.remove_ownership_outlier)
# grades
df['grade'] = df['grade'].apply(my_modules_cleaning.remove_grade_outlier)

print(df['purpose'].value_counts())
print(df['loan_status'].value_counts())
print(df['term'].value_counts())
print(df['home_ownership'].value_counts())
print(df['grade'].value_counts())

# encoding the categorical_data
le = LabelEncoder()
df['grade'] = le.fit_transform(df['grade'])
df['home_ownership'] = le.fit_transform(df['home_ownership'])
df['term'] = le.fit_transform(df['term'])
df['purpose'] = le.fit_transform(df['purpose'])
df['loan_status'] = le.fit_transform(df['loan_status'])


df = df.drop(['Unnamed: 0'], axis = 1)
# saves encoded and cleaned dataset
df = df.to_csv('cleaned_encoded.csv')
