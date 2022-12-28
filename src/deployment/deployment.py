import my_modules_deployment
import streamlit as st
import pickle



model = pickle.load(open('model_random.sav', 'rb'))

st.title('Loan Current Status')

user_data = my_modules_deployment.user_report()
st.header('Details')
st.write(user_data)

Status = model.predict(user_data)

st.subheader('Loan Status')

if st.button('Generate Prediction'):
	if Status == 1:
		st.write('Fully Paid')
	elif Status == 0:
		st.write('Default')
	else:
		st.write("Please fill inputs ")