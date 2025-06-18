import streamlit as st
import plotly.graph_objects as go

# --- Access stored session state ---
user_input = st.session_state.get('user_input')
user_sum = st.session_state.get('user_sum')
top_matches = st.session_state.get('top_matches')

# --- Safety check ---
if user_input is None or top_matches is None:
    st.warning("Please complete your taste preference selection first.")
    st.stop()

top_match = top_matches.iloc[0]

# --- 1. Summary of User Profile ---
st.title("🎯 Your Coffee Match Summary")
st.subheader("🧾 Your Profile Summary")
st.write(f"Based on your preference profile with a total score of **{user_sum:.1f}**, we found coffee farms that closely match your taste.")
st.write("**Your Selected Preferences:**")
st.json(user_input)

# --- 2. Top Match Recap ---
st.subheader("🏆 Best Matching Farm")

st.write(f"""
- **Farm Name:** {top_match['Farm_Name']}
- **Region & Country:** {top_match['Region']}, {top_match['Country_of_Origin']}
- **Total Cup Points:** {top_match['Total_Cup_Points']}
- **Processing Method:** {top_match.get('Processing.Method', 'Unknown')}
""")

# --- 3. Radar Chart Comparison ---
import pandas as pd
import plotly.graph_objects as go
import streamlit as st

# --- Assumes these are in session_state ---
user_input = st.session_state['user_input']
user_sum = st.session_state['user_sum']
df_full = st.session_state.get('df')  # Make sure the full dataframe is stored earlier
qualities = list(user_input.keys())

# --- Safety Check ---
if df_full is None:
    st.warning("Full dataset not found. Make sure to store df in session_state['df'] in an earlier step.")
    st.stop()

# --- Get max values per attribute from full dataset ---
max_profile = df_full[qualities].max().to_dict()

# --- Radar Chart ---
st.subheader("📊 Preference Comparison (You vs. Best in Data)")

fig = go.Figure()

# User profile
fig.add_trace(go.Scatterpolar(
    r=list(user_input.values()),
    theta=qualities,
    fill='toself',
    name='Your Preference'
))

# Max profile
fig.add_trace(go.Scatterpolar(
    r=list(max_profile.values()),
    theta=qualities,
    fill='toself',
    name='Best Coffee in Dataset'
))

fig.update_layout(
    polar=dict(radialaxis=dict(visible=True, range=[0, 10])),
    showlegend=True
)

st.plotly_chart(fig)

import io

st.subheader("📥 Download Your Coffee Match")

# --- 1. Download Top Matches as CSV ---
csv = top_matches.to_csv(index=False).encode('utf-8')
st.download_button(
    label="⬇️ as CSV",
    data=csv,
    file_name='my_coffee_matches.csv',
    mime='text/csv'
)
