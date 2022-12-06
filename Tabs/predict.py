"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Decision Tree Classifier</b> for the Renal Disease Prediction.
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.
    Bp = st.slider("Blood Pressure", int(df["Bp"].min()), int(df["Bp"].max()))
    Al = st.slider("Albumin Level", int(df["Al"].min()), int(df["Al"].max()))
    Su = st.slider("Sugar Level", float(df["Su"].min()), float(df["Su"].max()))
    Bu = st.slider("Blood Urea Level", int(df["Bu"].min()), int(df["Bu"].max()))
    Sc = st.slider("Serum Creatinine Level", int(df["Sc"].min()), int(df["Sc"].max()))
    Sod = st.slider("Sodium Level", int(df["Sod"].min()), int(df["Sod"].max()))
    Pot = st.slider("Potassium Level", float(df["Pot"].min()), float(df["Pot"].max()))
    Hemo = st.slider("Hemoglobin Level", float(df["Hemo"].min()), float(df["Hemo"].max()))
    Wbcc = st.slider("White Blood Cell Count", int(df["Wbcc"].min()), int(df["Wbcc"].max()))
    Rbcc = st.slider("Red Blood Cell Count", int(df["Rbcc"].min()), int(df["Rbcc"].max()))

    
    # Create a list to store all the features
    features = [Bp,Al,Su,Bu,Sc,Sod,Pot,Hemo,Wbcc,Rbcc]

    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        score = score 
        st.info("Predicted Sucessfully...")

        # Print the output according to the prediction
        if (prediction == 1):
            st.warning("The person is prone to get Renal Diseases!!")
        else:
            st.success("The person is relatively safe from Renal Diseases")

        # Print teh score of the model 
        st.write("The model used is trusted by doctor and has an accuracy of ", (score*100),"%")
