import streamlit as st

# Logo
with st.sidebar:
  st.image("streamlit/imgs/logo.png", width=100)#

# Define the content of the Contacts page
st.image("streamlit/imgs/logo.png", width=100)
st.title("Real Estate Price Prediction API")
st.text("by MerMade")
horizontal_bar = "<hr style='margin-top: 0; margin-bottom: 0; height: 1px; \
                        border: 1px solid #635985;'><br>"    # thin divider line
st.markdown(horizontal_bar, True)
st.subheader("Contacts")
st.markdown("""
    This is the contacts page. Here you can find our contact information.
""")
st.subheader("Contact Information")
st.markdown("""    
        **Brian Daza**:
            https://github.com/brain8d
        
        **Julio Barizon**:
            https://github.com/DDDines
        
        **Omar Hamdy**:
            https://github.com/theomarcode
        
        **Polina Yarova**:
            https://github.com/polinaya777
        
        **Sylvain Legay**:
            https://github.com/slvg01
                        
""")

st.text("")
st.text('')
st.markdown(''' 
    :question: Get help or :bug: report a bug:
    https://github.com/brain8d/immo-eliza-deployment 
    '''
)