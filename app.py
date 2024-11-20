import streamlit as st
from main import VirtualCat  # Importing the VirtualCat class from main.py

# Title of the Streamlit app
st.title("Virtual Cat Interaction")

# Create an instance of the VirtualCat
cat_name = st.text_input("Enter your cat's name:", "Simba")
simba = VirtualCat(cat_name)

# Display cat's status
if st.button("Show Status"):
    simba.display_status()

# Interaction options
st.header("What would you like to do with your cat?")
action = st.selectbox("Choose an action:", ["Play", "Feed", "Rest", "Health Check", "Talk to Simba"])

if st.button("Perform Action"):
    if action == "Play":
        simba.play()
    elif action == "Feed":
        simba.feed()
    elif action == "Rest":
        simba.rest()
    elif action == "Health Check":
        simba.health_check()
    elif action == "Talk to Simba":
        simba.talk_to_simba()

# Display the current status after action
if st.button("Update Status"):
    simba.display_status()
