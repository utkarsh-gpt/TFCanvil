import streamlit as st
from utils import decodeRules, solveAnvil, translateToSteps, solveAllHits
import numpy as np

st.title("TFC Anvil Solver")

str_options = ["Draw","Hit", "Punch","Bend","Upset", "Shrink"]
# Define the options for the dropdowns
rules = ["Last", "Second Last", "Third Last", "Not Last"]

# Create the integer input for the target number
target_number = st.number_input("Target Number:", min_value=0, max_value=150, value=0, step=1)

# Create 3 rows with 2 columns each and store rules in a default dictionary
rules_dict = {}

# Add a checkbox for all hits
all_hits = st.checkbox("Are all three hits?")


# Create 2 rows with 2 columns each
for i in range(2):
    col1, col2 = st.columns(2)
    
    with col1:
        left_selection = st.selectbox(f"Left Selection {i+1}", rules, key=f"left_{i}")
    
    with col2:
        right_selection = st.selectbox(f"Right Selection {i+1}", str_options, key=f"right_{i}")
    
    if left_selection == "Not Last":
        if left_selection not in rules_dict:
            rules_dict[left_selection] = [right_selection]  
        else:
            rules_dict[left_selection] += [right_selection]
    else:
        rules_dict[left_selection] = right_selection 

# Optional third row
if st.checkbox("Add third rule"):
    col1, col2 = st.columns(2)
    
    with col1:
        left_selection = st.selectbox("Left Selection 3", rules, key="left_2")
    
    with col2:
        right_selection = st.selectbox("Right Selection 3", str_options, key="right_2")
    
    if left_selection == "Not Last":
        if left_selection not in rules_dict:
            rules_dict[left_selection] = [right_selection]  
        else:
            rules_dict[left_selection] += [right_selection]
    else:
        rules_dict[left_selection] = right_selection 

# Button to generate result
if st.button("Generate Result"):
    try: 
        if all_hits:
            final_result = solveAllHits(target_number)
        else:
            rule_nums = decodeRules(rules_dict)
            final_result = solveAnvil(target_number, rule_nums)
        # st.write(rule_nums)
        # st.write(final_result)
        st.write(translateToSteps(final_result))
    except Exception:
        st.write("Sorry. something went wrong. Try a different one")
