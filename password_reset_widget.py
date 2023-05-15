import streamlit_authenticator as stauth
from login_widget import writeForLogin , getAuthenticator
import yaml
from yaml.loader import SafeLoader
import streamlit as st
from login2 import save_session_state

name, authentication_status, username = save_session_state()
print(name, authentication_status, username)
authenticator = stauth.Authenticator()

if authentication_status:
    try:
        if authenticator.reset_password(username, 'Reset password'):
            st.success('Password modified successfully')

            with open('config.yaml', 'w') as file:
                yaml.dump(config, file, default_flow_style=False)
    except Exception as e:
        st.error(e)

