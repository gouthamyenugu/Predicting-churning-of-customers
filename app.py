
# Import necessary libraries
import pickle
import streamlit as st

# Load the trained model
pickle_in = open('churn_rf.pkl', 'rb')
classifier = pickle.load(pickle_in)

# Define the prediction function
def prediction(area_code, account_length, voice_plan, voice_messages, intl_plan, intl_mins, intl_calls, intl_charge, day_mins, day_calls, day_charge, eve_mins, eve_calls, eve_charge, night_mins, night_calls, night_charge, customer_calls):
    if area_code == 'area_code_415':
        area_code_415 = 1
        area_code_408 = 0
        area_code_510 = 0
    elif area_code == 'area_code_408':
        area_code_415 = 0
        area_code_408 = 1
        area_code_510 = 0
    else:
        area_code_415 = 0
        area_code_408 = 0
        area_code_510 = 0

    if voice_plan == 'yes':
        voice_plan_yes = 1
        voice_plan_no = 0
    else:
        voice_plan_yes = 0
        voice_plan_no = 1

    if intl_plan == 'yes':
        intl_plan_yes = 1
        intl_plan_no = 0
    else:
        intl_plan_yes = 0
        intl_plan_no = 1

    # Making prediction
    prediction = classifier.predict([[area_code, account_length,voice_plan,voice_messages, intl_plan, intl_mins, intl_calls, intl_charge, day_mins, day_calls, day_charge, eve_mins, eve_calls, eve_charge, night_mins, night_calls, night_charge, customer_calls]])

    if prediction == 0:
        pred = 'will not churn'
    else:
        pred = 'is likely to churn'
    return pred

# Main function for the Streamlit app
def main():
    # Front-end elements of the web page
    st.title("Churn Prediction of customers")

    # User input fields
    area_code = st.number_input('Area Code')
    account_length = st.number_input('Account Length')
    voice_plan = st.number_input('Voice Plan')
    voice_messages = st.number_input('Voice Messages')
    intl_plan = st.number_input('International Plan')
    intl_mins = st.number_input('International Minutes')
    intl_calls = st.number_input('International Calls')
    intl_charge = st.number_input('International Charge')
    day_mins = st.number_input('Day Minutes')
    day_calls = st.number_input('Day Calls')
    day_charge = st.number_input('Day Charge')
    eve_mins = st.number_input('Evening Minutes')
    eve_calls = st.number_input('Evening Calls')
    eve_charge = st.number_input('Evening Charge')
    night_mins = st.number_input('Night Minutes')
    night_calls = st.number_input('Night Calls')
    night_charge = st.number_input('Night Charge')
    customer_calls = st.number_input('Customer Calls')
    result = ""

    # When predict button is clicked
    if st.button('Predict'):
        result = prediction(area_code, account_length, voice_plan, voice_messages, intl_plan, intl_mins, intl_calls, intl_charge, day_mins, day_calls, day_charge, eve_mins, eve_calls, eve_charge, night_mins, night_calls, night_charge, customer_calls)
        st.success('Customer {}'.format(result))

if __name__ == '__main__':
    main()
