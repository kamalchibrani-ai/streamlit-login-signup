import streamlit as st
from streamlit_login_auth_ui.widgets import __login__
from dotenv import load_dotenv
load_dotenv('.env')
import os

auth_token = os.getenv("AUTH_TOKEN")
print(auth_token)

__login__obj = __login__(auth_token = "auth_token", 
                    company_name = "Course_Buddy",
                    width = 200, height = 250, 
                    logout_button_name = 'Logout', hide_menu_bool = False, 
                    hide_footer_bool = False, 
                    lottie_url = 'https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json')

LOGGED_IN = __login__obj.build_login_ui()

if LOGGED_IN == True:

    st.markdown("Your Streamlit Application Begins here!")

