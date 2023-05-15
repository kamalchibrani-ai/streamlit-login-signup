import streamlit as st

with st.form("my_form"):
   st.write("Inside the form")
   resume = st.file_uploader("Upload a file",type='pdf')
   slider_val = st.slider("Form slider")
   checkbox_val = st.checkbox("Form checkbox")

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if  submitted:
    st.balloons()
    st.write("slider", slider_val, "checkbox", checkbox_val,resume.name)

st.write("Outside the form")