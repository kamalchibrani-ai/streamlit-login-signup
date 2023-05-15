import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import login_widget

# hashed_passwords = stauth.Hasher(['password', 'password']).generate()
# print(hashed_passwords)

authenticator = login_widget.getAuthenticator()
name, authentication_status, username = authenticator.login('Login', 'main')

def save_session_state():
    st.session_state["name"] = name
    st.session_state["authentication_status"] = authentication_status
    st.session_state["username"] = username
    return name, authentication_status, username

if st.session_state["authentication_status"]:
    authenticator.logout('Logout', 'main', key='unique_key')
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title('Some content')
    
elif st.session_state["authentication_status"] is False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None:
    st.warning('Please enter your username and password')