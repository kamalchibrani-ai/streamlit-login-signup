import yaml
from yaml.loader import SafeLoader
import streamlit as st
import streamlit_authenticator as stauth
import login_widget

def writeForLogin():
    with open('config.yaml') as file:
        config = yaml.load(file, Loader=SafeLoader)
        return config

def getAuthenticator():
    config = writeForLogin()
    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['preauthorized']
    )

    return authenticator
