"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

# Import necessary functions from web_functions
from web_functions import predict

hide_st_style = """
<style>
MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}
</style>
"""


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

    st.header("The values entered by user")
    st.cache_data()
    df3 = pd.DataFrame(features).transpose()
    df3.columns=["Bp","Al","Su","Bu","Sc","Sod","Pot","Hemo","Wbcc","Rbcc"]
    st.dataframe(df3)

    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        score = score 
     

        if(Bp > 125):
            st.error("The person has high risk of Cardiac problems induced by kidney malfunctioning")
            st.warning("Please consult a Nephrologist")
        
        elif(Bu > 200):
            st.error("High risk of bladder infection or kidney stone")

        elif(Hemo > 13.5):
            st.error("The person is prone to get Renal Diseases!!")
            st.warning("High risk of kidney tumour")

        elif(Sc > 30):
            st.error("The person is prone to get Renal Diseases!!")
            st.warning("Improper filteration")
 
                        
        elif(Su > 0.5):
            st.error("The person is prone to get Renal Diseases!!")
            st.warning("High blood sugar")

        
        elif (Su < 0.5 and Sc<30 and Hemo < 13.5 and Bu < 200 and Bp < 125):
            st.success("The person is relatively safe from Renal Diseases")

            

            
        # Print teh score of the model 
        st.sidebar.write("The model used is trusted by doctor and has an accuracy of ", (score*100),"%")
