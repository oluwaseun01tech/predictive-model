import streamlit as st 
import joblib 

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: #f9f9f9; /* Light grey background */
        font-family: 'Arial', sans-serif; /* Font style */
    }
    .header {
        font-size: 40px !important;
        color: #ffffff; /* White text color */
        background-color: #4a90e2; /* Sky blue background */
        padding: 20px; /* Padding around the text */
        border-radius: 10px; /* Rounded corners */
        text-align: center; /* Center align text */
        margin-bottom: 20px; /* Space below the header */
    }
    .description {
        font-size: 20px;
        color: #333333; /* Dark gray text */
        text-align: center; /* Center align text */
        margin-bottom: 20px; /* Space below the description */
    }
    .button {
        display: block;
        width: 220px; /* Button width */
        margin: 0 auto; /* Center the button */
        padding: 10px;
        background-color: #e94e77; /* Vibrant pink background */
        color: #ffffff; /* White text */
        text-align: center; /* Center text */
        border: none;
        border-radius: 5px; /* Rounded corners */
        font-size: 18px; /* Button text size */
        cursor: pointer; /* Pointer cursor on hover */
        transition: background-color 0.3s; /* Smooth transition */
    }
    .button:hover {
        background-color: #c83b65; /* Darker pink on hover */
    }
    .footer {
        font-size: 14px;
        color: #777777; /* Light gray text */
        text-align: center; /* Center align text */
        margin-top: 40px; /* Space above footer */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Header
st.markdown('<div class="header">Diabetes Prediction Project</div>', unsafe_allow_html=True)

# Description
st.markdown('<div class="description">Welcome to the Diabetes Prediction Project. Here, we utilize machine learning to predict diabetes based on various health metrics.</div>', unsafe_allow_html=True)

# Button
if st.button('Get Started', key='start_button', help='Click to begin'):
    st.success('Let’s get started with the diabetes prediction!')  # Feedback on button click

# Footer
st.markdown('<div class="footer">© 2024 Diabetes Prediction Project</div>', unsafe_allow_html=True)

#lood the pre-trained model
model = joblib.load('diabetes_logistic.model')


# Create two columns for input fields
col1, col2 = st.columns(2)

# Collect user input through the input fields
Pregnancies = col1.number_input(label="Enter the number of Pregnancies", min_value=0, max_value=20)
Glucose = col2.number_input(label="Enter the Glucose level", min_value=0, max_value=200)
BMI = col1.number_input(label="Enter the BMI value", min_value=0.0, max_value=60.0)
DiabetesPedigreeFunction = col2.number_input(label="Enter the Diabetes Pedigree Function", min_value=0.0, max_value=2.5)
Age = col1.number_input(label="Enter the Age of the passenger", min_value=0, max_value=120)


# Define a button to submit the input and predict the result
if st.button("Predict"):
    # Use the model to make a prediction
    prediction = model.predict([[Pregnancies, Glucose, BMI, DiabetesPedigreeFunction, Age,]])
    
    # Display the prediction result
    if prediction == 1:
        st.success("The model predicts that the patient is diabetic.")
    else:
        st.warning("The model predicts that the patient is not diabetic.")

