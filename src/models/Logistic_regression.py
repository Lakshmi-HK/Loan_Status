from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import my_modules_model

# load file
path = 'D:\pythonProject\Loan_Status_Prediction\Loan_Status\data\processed\cleaned_encoded.csv'
df = my_modules_model.load_df(path)
print(df.columns)
df = df.drop(['Unnamed: 0'], axis = 1)
print(df.columns)

x = df.drop(['loan_status'], axis = 1)
y = df['loan_status']

# split of dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, stratify = y, random_state = 7)

# random forest
model = LogisticRegression(class_weight='l2')
# Train model
my_modules_model.Train_model(x_train, y_train, model)

# Evaluate model
predictions = model.predict(x_test)
my_modules_model.evalaute_model(y_test, predictions)

# Save model
my_modules_model.save_model(model)
