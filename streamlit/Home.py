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
    Properties price is determined by numerous factors such as locality, living area, 
    number of bedrooms and many others.

    The Properties Price Prediction API aims to help property sellers and buyers 
    find out a fair price estimation.

    API has been trained on immoweb.be data. 
"""
)
