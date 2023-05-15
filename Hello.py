import streamlit as st

def hello_world():
    st.write("Hello World")


st.set_page_config(page_title='Multipage Website',
    page_icon='📱',
    layout='wide',
    initial_sidebar_state='expanded')


if "my_input" not in st.session_state:
    st.session_state["my_input"] = ""

my_input = st.text_input("Enter your name:",st.session_state["my_input"])
submit = st.button("Submit")

if submit:
    st.session_state["my_input"] = my_input
    st.write(st.session_state.my_input)






# # Using object notation
# add_selectbox = st.sidebar.selectbox(
#     "How would you like to be contacted?",
#     ("Email", "Home phone", "Mobile phone")
# )

# # Using "with" notation
# with st.sidebar:
#     add_radio = st.radio(
#         "Choose a shipping method",
#         ("Standard (5-15 days)", "Express (2-5 days)")
#     )




if __name__ == "__main__":
    hello_world()