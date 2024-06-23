import streamlit as st
from src.inference import get_prediction

#Initialise session state variable
if 'input_features' not in st.session_state:
    st.session_state['input_features'] = {}

def app_sidebar():
    st.sidebar.header('Details')

    gender_options = ['Male','Female']
    gender = st.sidebar.radio("Customer Gender", gender_options)

    SeniorCitizen_options = [0,1]
    SeniorCitizen = st.sidebar.selectbox("Customer Age >= 65 (1 for Yes)", SeniorCitizen_options)

    tenure = st.sidebar.slider('Tenure Months', 1, 70, 35, 1)

    YN_options = ['Yes','No']
    Partner = st.sidebar.selectbox("Customer Has a Partner", YN_options)
    Dependents= st.sidebar.selectbox("Customer Live with Dependents", YN_options)
    PhoneService = st.sidebar.selectbox("Phone Service Subscription", YN_options)
    PaperlessBilling = st.sidebar.selectbox("Opted for Paperless Billing", YN_options)

    InternetService_options = ['DSL','Fiber optic','No']
    InternetService = st.sidebar.selectbox("Internet Service Subscription", InternetService_options)

    YN_NoInternet_options = ['Yes','No','No internet service']
    MultipleLines = st.sidebar.selectbox("Multiple Lines Subscription", YN_NoInternet_options)
    OnlineSecurity = st.sidebar.selectbox("Online Security Subscription", YN_NoInternet_options)
    OnlineBackup = st.sidebar.selectbox("Online Backup Subscription", YN_NoInternet_options)
    DeviceProtection = st.sidebar.selectbox("Device Protection Subscription", YN_NoInternet_options)
    TechSupport = st.sidebar.selectbox("Technical Support Subscription", YN_NoInternet_options)
    StreamingTV = st.sidebar.selectbox("Streaming TV Subscription", YN_NoInternet_options)
    StreamingMovies = st.sidebar.selectbox("Streaming Movies Subscription", YN_NoInternet_options)

    Contract_options = ['Month-to-month', 'One year', 'Two year']
    Contract = st.sidebar.selectbox("Contract Type", Contract_options)

    PaymentMethod_options = ['Bank transfer (automatic)','Credit card (automatic)','Electronic check','Mailed check']
    PaymentMethod = st.sidebar.selectbox("Payment Method", PaymentMethod_options)

    def get_input_features():
        input_features = {
                          'gender': gender,
                          'SeniorCitizen': int(SeniorCitizen),
                          'Partner': Partner,
                          'Dependents': Dependents,
                          'tenure': int(tenure),
                          'PhoneService': PhoneService,
                          'MultipleLines': MultipleLines,
                          'InternetService': InternetService,
                          'OnlineSecurity': OnlineSecurity,
                          'OnlineBackup': OnlineBackup,
                          'DeviceProtection': DeviceProtection,
                          'TechSupport': TechSupport,
                          'StreamingTV': StreamingTV,
                          'StreamingMovies': StreamingMovies,
                          'Contract': Contract,
                          'PaperlessBilling': PaperlessBilling,
                          'PaymentMethod': PaymentMethod,
                          'MonthlyCharges': int(65), #Mean
                          'TotalCharges': int(2283), #Mean
                        }
        return input_features
    sdb_col1, sdb_col2 = st.sidebar.columns(2)
    with sdb_col1:
        predict_button = st.sidebar.button("Assess", key="predict")
    with sdb_col2:
        reset_button = st.sidebar.button("Reset", key="clear")
    if predict_button:
        st.session_state['input_features'] = get_input_features()
    if reset_button:
        st.session_state['input_features'] = {}
    return None

def app_body():
    title = '<p style="font-family:arial, sans-serif; color:Black; font-size: 40px;"><b> Welcome to Customer Churn Assessment</b></p>'
    st.markdown(title, unsafe_allow_html=True)
    default_msg = '**System assessment says:** {}'
    if st.session_state['input_features']:
        assessment = get_prediction(
                                    gender=st.session_state['input_features']['gender'],
                                    SeniorCitizen=st.session_state['input_features']['SeniorCitizen'],
                                    Partner=st.session_state['input_features']['Partner'],
                                    Dependents=st.session_state['input_features']['Dependents'],
                                    tenure=st.session_state['input_features']['tenure'],
                                    PhoneService=st.session_state['input_features']['PhoneService'],
                                    MultipleLines=st.session_state['input_features']['MultipleLines'],
                                    InternetService=st.session_state['input_features']['InternetService'],
                                    OnlineSecurity=st.session_state['input_features']['OnlineSecurity'],
                                    OnlineBackup=st.session_state['input_features']['OnlineBackup'],
                                    DeviceProtection=st.session_state['input_features']['DeviceProtection'],
                                    TechSupport=st.session_state['input_features']['TechSupport'],
                                    StreamingTV=st.session_state['input_features']['StreamingTV'],
                                    StreamingMovies=st.session_state['input_features']['StreamingMovies'],
                                    Contract=st.session_state['input_features']['Contract'],
                                    PaperlessBilling=st.session_state['input_features']['PaperlessBilling'],
                                    PaymentMethod=st.session_state['input_features']['PaymentMethod'],
                                    MonthlyCharges=st.session_state['input_features']['MonthlyCharges'],
                                    TotalCharges=st.session_state['input_features']['TotalCharges'])
        if assessment.lower() == 'yes':
            st.success(default_msg.format('Churn'))
        else:
            st.warning(default_msg.format('Not Churn'))
    return None

def main():
    app_sidebar()
    app_body()
    return None

if __name__ == "__main__":
    main()