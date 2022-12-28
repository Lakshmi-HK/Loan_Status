import my_modules_cleaning

# load file
path = 'D:\\pythonProject\\Loan_Status_Prediction\\Loan_Status\\data\\raw\\Raw.csv'
df = my_modules_cleaning.load_df(path)

# Drops unncessary columns
drop_columns = (['Unnamed: 0', 'id', 'member_id', 'funded_amnt', 'funded_amnt_inv','int_rate', 'sub_grade', 'emp_title','verification_status', 'issue_d','pymnt_plan','title', 'zip_code', 'addr_state', 'dti', 'delinq_2yrs','earliest_cr_line', 'inq_last_6mths', 'open_acc', 'pub_rec','revol_bal', 'revol_util','total_acc', 'initial_list_status','out_prncp', 'out_prncp_inv','total_pymnt_inv','total_rec_prncp', 'total_rec_int', 'total_rec_late_fee', 'recoveries','collection_recovery_fee', 'last_pymnt_d','last_credit_pull_d', 'collections_12_mths_ex_med', 'policy_code','application_type', 'acc_now_delinq', 'chargeoff_within_12_mths','delinq_amnt', 'pub_rec_bankruptcies', 'tax_liens'])
df = df.drop(drop_columns, axis = 1)

# check null values
my_modules_cleaning.check_null_values(df)

# dropped null values
df = my_modules_cleaning.drop_null_values(df)
my_modules_cleaning.check_null_values(df)

# saves cleaned data
my_modules_cleaning.save_df(df)