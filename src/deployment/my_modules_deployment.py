import streamlit as st
import pickle
import sklearn
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()


def user_report():
    loan_amnt = st.number_input("Enter Loan Amount", 500, 100000)
    installment = st.number_input("Enter Installment Amount", 10, 1000)
    annual_inc = st.number_input("Enter Annual Intrest", 0, 100000)
    total_pymnt = st.number_input("Enter Total Amount", 0, 10000)
    last_pymnt_amnt = st.number_input("Last Payment Amount", 0, 100000)

    term = st.selectbox('Term in months', ('36', '60'))
    grade = st.selectbox('Grades', ('A', 'B', 'C', "D", 'E',"F","G"))

    emp_length = st.number_input('Experience', 1, 20)
    home_ownership = st.selectbox('Ownership', ('Rent', 'Mortage'))
    purpose = st.selectbox('Purpose', (
    'debt_consolidation', 'other', 'credit_card ', 'home_improvement', 'major_purchase', 'small_business', 'car'))

    user_report_data = {
        'loan_amnt': loan_amnt,
        'installment': installment,
        'annual_inc': annual_inc,
        'total_pymnt': total_pymnt,
        'last_pymnt_amnt': last_pymnt_amnt,
        'term': term,
        'grade': grade,
        'emp_length': emp_length,
        'home_ownership': home_ownership,
        'purpose': purpose

    }
    df = pd.DataFrame(user_report_data, index=[0])
    df['grade'] = le.fit_transform(df['grade'])
    df['home_ownership'] = le.fit_transform(df['home_ownership'])
    df['term'] = le.fit_transform(df['term'])

    df['purpose'] = le.fit_transform(df['purpose'])

    return df