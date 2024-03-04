import streamlit as st

horizontal_bar = "<hr style='margin-top: 0; margin-bottom: 0; height: 1px; \
                        border: 1px solid #635985;'><br>"  # thin divider line

# Define the content of the Home page
# Display a logo and a title
st.image("streamlit/imgs/header.png")
st.sidebar.image("streamlit/imgs/logo.png", use_column_width=True)
st.title("Real Estate Price Prediction API")
st.text("by MerMade")
st.markdown(horizontal_bar, True)
st.subheader("Our project")
st.markdown(
    '''
    Property prices serve as a significant economic indicator. They play a crucial role for stakeholders such as governments, real estate agents, investors, developers. Equally important we want to focus on private buyers and sellers,  aiding them in making informed decisions.

    Being able to to determine fair property selling price is thus a crucial element of the real estate market.

    **Our app is designed to help sellers  to evaluate their property price:**
    - independently from any intermediaries
    - in a precise and reliable manner
    - instantly
    - on a user-friendly  interface

    **Our objective is to provide a reliable price estimation:** 
    - based on most impactful property features of the real estate market
    - identified through strong data collection and analysis
    - generated through a machine learning model

    Further evolution will integrate statistical information on the real estate market to make it more useful for a wider audience. 

    Follow us to stay informed : https://github.com/brain8d/immo-eliza-deployment

    By MerMade, with love - Enjoy !

'''
)
st.text("")
st.text("")
st.markdown(":question: Get help: https://github.com/brain8d/immo-eliza-deployment")
st.markdown(":bug: Report a bug https://github.com/brain8d/immo-eliza-deployment ")