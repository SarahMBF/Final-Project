import streamlit as st
from utils.load_data import load_data
import plotly.graph_objects as go
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("📊 Data Explorer")

df = load_data()

# Filters - Dropdowns for users to filter
countries = st.multiselect("Filter by Country", df['Country_of_Origin'].dropna().unique())
methods = st.multiselect("Filter by Processing Method", df['Processing_Method'].dropna().unique())

# Makes a copy of the DataFrame to apply filters
filtered_df = df.copy()

if countries:
    filtered_df = filtered_df[filtered_df['Country_of_Origin'].isin(countries)]
if methods:
    filtered_df = filtered_df[filtered_df['Processing_Method'].isin(methods)]

# Show table if filtered DataFrame has data, otherwise show warning
if not filtered_df.empty:
    display_cols = ['Farm_Name', 'Region', 'Country_of_Origin', 'Total_Cup_Points']
    st.dataframe(filtered_df[display_cols])
else:
    st.warning("No farms match your selected processing method. Try widening your range.")

selected = st.selectbox("Choose a Farm Name", df['Farm_Name'].dropna().unique())
sample = df[df['Farm_Name'] == selected].iloc[0]

metrics = ['Aroma', 'Flavor', 'Aftertaste', 'Acidity', 'Body',
           'Balance', 'Uniformity', 'Clean_Cup', 'Sweetness', 'Cupper_Points']

# Builds a radar chart of quality attributes
fig = go.Figure(data=go.Scatterpolar(r=[sample[m] for m in metrics],
    theta=metrics,
    fill='toself',
    name=selected
))

fig.update_layout(polar=dict(radialaxis=dict(visible=True)), showlegend=False)
st.plotly_chart(fig)

st.subheader("Average Defects by Country")
avg_defects = df.groupby('Country_of_Origin')[['Category_One_Defects', 'Category_Two_Defects']].mean().round(2).sort_values(by='Category_One_Defects', ascending=False)
st.dataframe(avg_defects)

st.markdown("""
**Category One Defects** are serious issues in green coffee beans that affect cup quality.  
They include black beans, sour beans, pods, and other major defects.

According to the SCA standard:
- **0 defects** → Specialty grade
- **>5 defects** → Not considered specialty coffee
""")

# Filter to remove outliers 
max_defects = st.slider("Max Defect Count to Include", 0, int(df['Category_One_Defects'].max()), value=10)
filtered_df = df[df['Category_One_Defects'] <= max_defects]

# Histogram
st.subheader("📊 Distribution of Category One Defects")
fig1, ax1 = plt.subplots(figsize=(6, 4))
sns.histplot(filtered_df['Category_One_Defects'], bins=15, kde=False, ax=ax1)
ax1.set_xlabel("Category 1 Defects")
ax1.set_ylabel("Number of Coffee Samples")
st.pyplot(fig1)

# Scatter plot
st.subheader("📉 Impact on Total Cup Score")
fig2, ax2 = plt.subplots(figsize=(6, 4))
sns.scatterplot(data=filtered_df, x='Category_One_Defects', y='Total_Cup_Points', ax=ax2)
ax2.set_title("Defects vs. Cup Score")
st.pyplot(fig2)

# Quick summary stats
st.subheader("📌 Summary")
num_clean = (df['Category_One_Defects'] == 0).sum()
total = len(df)
st.markdown(f"- ✅ **{num_clean} of {total} samples** have **0 defects** (likely specialty grade)")
st.markdown(f"- 🧹 This analysis includes samples with up to **{max_defects} defects**")

# "Surprise Me" feature
if st.button("🎲 Surprise Me with a Coffee!"):
    random_row = df.sample(1).iloc[0]
    st.write("**Farm:**", random_row['Farm_Name'])
    st.write("**Country:**", random_row['Country_of_Origin'])
    st.write("**Flavor Score:**", random_row['Flavor'])
    st.write("**Sweetness Score:**", random_row['Sweetness'])
    st.write("**Processing:**", random_row['Processing_Method'])

# "Coffee Fact" feature
if st.button("💡 Coffee Fact"):
    fact = df.loc[df['Total_Cup_Points'].idxmax()]
    st.info(f"The highest scoring coffee is from {fact['Country_of_Origin']} with {fact['Total_Cup_Points']} points!")
