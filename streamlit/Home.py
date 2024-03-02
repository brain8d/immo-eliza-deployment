import streamlit as st

# Home page - set up page config
st.set_page_config(
    page_title="Real Estate Price Prediction API",
    page_icon="imgs/icon.png",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get help": "https://github.com/brain8d/immo-eliza-deployment",
        "Report a bug": "https://github.com/brain8d/immo-eliza-deployment",
        "About": """
                ## Price Prediction API
                
                **GitHub**: https://github.com/brain8d/immo-eliza-deployment
                
                Properties price is determined by numerous factors such as locality, living area, 
                number of bedrooms and many others.
                
                The Properties Price Prediction API aims to help property sellers and buyers 
                find out a fair price estimation. 

                API has been trained on immoweb.be data.
            """,
    },
)

horizontal_bar = "<hr style='margin-top: 0; margin-bottom: 0; height: 1px; \
                        border: 1px solid #635985;'><br>"  # thin divider line

# Define the sidebar navigation
# page = st.sidebar.radio("Choose a page", ["Home", "Price prediction", "Contacts"])

# Define the content of the Home page
# Display a logo and a title
st.image("streamlit/imgs/logo.png", width=100)
st.title("Real Estate Price Prediction API")
st.text("by MerMade")
st.markdown(horizontal_bar, True)
st.subheader("Our project")
st.markdown(
    """
    Property prices serve as a significant economic indicator. They play a crucial role for stakeholders such as governments, real estate agents, investors, developers. Equally important we want to focus on private buyers and sellers,  aiding them in making informed decisions.

    Being able to to determine fair property selling price is thus a crucial element of the real estate market.
    Our app is designed to help sellers  to evaluate their property price:
    - independently from any intermediaries
    - in a precise and reliable manner
    - instantly
    - on a user-friendly  interface

    Our objective is to provide a reliable price estimation: 
    - based on most impactful property features of the real estate market
    - identified through strong data collection and analysis
    - generated through a machine learning model

    Further evolution will integrate statistical information on the real estate market to make it more useful for a wider audience. 

    Follow us to stay informed : "https://github.com/brain8d/immo-eliza-deployment"

    By Mermade, with love - Enjoy !
s
"""
)

st.text("Get help: https://github.com/brain8d/immo-eliza-deployment")
st.text("Report a bug https://github.com/brain8d/immo-eliza-deployment")