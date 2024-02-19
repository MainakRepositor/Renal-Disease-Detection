"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Renal Disease Predictor")

    # Add image to the home page
    st.image("./images/home.jpeg")

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
             Kidney disease means your kidneys are damaged and can’t filter blood the way they should. You are at greater risk for kidney disease if you have diabetes or high blood pressure. If you experience kidney failure, treatments include kidney transplant or dialysis. Other kidney problems include acute kidney injury, kidney cysts, kidney stones, and kidney infections.
        </p>
    """, unsafe_allow_html=True)

    st.markdown('''<iframe src="https://www.google.com/maps/embed?pb=!1m16!1m12!1m3!1d124393.84960547274!2d80.13058794435608!3d13.01606059733078!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!2m1!1sspecialist%20doctor%20in%20chennai%20for%20kidney!5e0!3m2!1sen!2sin!4v1708302774572!5m2!1sen!2sin" width="900" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>''',unsafe_allow_html=True)
