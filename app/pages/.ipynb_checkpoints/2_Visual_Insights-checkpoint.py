import streamlit as st
import plotly.express as px
from utils.load_data import load_data
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns

st.title("📈 Visual Insights")

df = load_data()

# Average cup points per country
fig1 = px.bar(
    df.groupby('Country_of_Origin')['Cupper_Points'].mean().sort_values(ascending=False).head(10),
    labels={'value': 'Avg. Cupper Points', 'index': 'Country'},
    title="Top 10 Countries by Avg. Cupper Score"
)
st.plotly_chart(fig1)


# Get the top 10 regions by average Total Cup Points
top_regions = df.groupby("Region_Country")["Total_Cup_Points"].mean().reset_index()
top_10 = top_regions.nlargest(10, "Total_Cup_Points")

# Create the horizontal bar chart
chart = alt.Chart(top_10).mark_bar().encode(
    x="Total_Cup_Points:Q",
    y=alt.Y("Region_Country:N", sort=alt.SortField("Total_Cup_Points", order="descending")),  
    color=alt.Color("Total_Cup_Points:Q", scale=alt.Scale(type="linear", scheme="blues")),  
    tooltip=["Region_Country", "Total_Cup_Points"]
).properties(
    title="Top 10 Regions by Total Cup Points (with Country)",
    width=600,
    height=400
)

# Display in Streamlit
st.subheader("Top 10 Regions by Total Cup Points")
st.altair_chart(chart)



import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# Your existing data
country_avg = df.groupby('Country_of_Origin', as_index=False)['Total_Cup_Points'].mean()

# Approximate country centroids (sample for top countries — can be expanded)
country_coords = {'Mexico': (23.6345, -102.5528),
	"Colombia": [4.5709, -74.2973],
    "Guatemala": [15.7835, -90.2308],
    "Brazil": [-14.235, -51.9253],
    "United States": [37.0902, -95.7129],
    "Taiwan": [23.6978, 120.9605],
    "Honduras": [15.2000, -86.2419],
    "Costa Rica": [9.7489, -83.7534],
    "Ethiopia": [9.145, 40.4897],
    "Tanzania": [-6.3690, 34.8888],
    "Uganda": [1.3733, 32.2903],
    "Thailand": [15.8700, 100.9925],
    "Nicaragua": [12.8654, -85.2072],
    "Kenya": [-1.2921, 36.8219],
    "El Salvador": [13.7942, -88.8965],
    "Indonesia": [-0.7893, 113.9213],
    "China": [35.8617, 104.1954],
    "India": [20.5937, 78.9629],
    "Malawi": [-13.2543, 34.3015],
    "Peru": [-9.1900, -75.0152],
    "Vietnam": [14.0583, 108.2772],
    "Myanmar": [21.9162, 95.9560],
    "Haiti": [18.9712, -72.2852],
    "Philippines": [12.8797, 121.7740],
    "Panama": [8.5379, -80.7821],
    "Ecuador": [-1.8312, -78.1834],
    "Laos": [19.8563, 102.4955],
    "Burundi": [-3.3731, 29.9189],
    "Papua New Guinea": [-6.3149, 143.9555],
    "Japan": [36.2048, 138.2529],
    "Rwanda": [-1.9403, 29.8739],
    "Zambia": [-13.1339, 27.8493],
    "Mauritius": [-20.3484, 57.5522],
    "Côte d'Ivoire": [7.5399, -5.5471]}
    

# Match coordinates
country_avg['lat'] = country_avg['Country_of_Origin'].map(lambda x: country_coords.get(x, (None, None))[0])
country_avg['lon'] = country_avg['Country_of_Origin'].map(lambda x: country_coords.get(x, (None, None))[1])

# Create the choropleth map
fig = go.Figure()

fig.add_trace(go.Choropleth(
    locations=country_avg['Country_of_Origin'],
    locationmode='country names',
    z=country_avg['Total_Cup_Points'],
    colorscale='YlGnBu',
    colorbar_title='Cup Points',
    showscale=True,
))

# Add text labels as scattergeo
fig.add_trace(go.Scattergeo(
    lon=country_avg['lon'],
    lat=country_avg['lat'],
    text=country_avg['Country_of_Origin'],
    mode='text',
    textfont=dict(size=10, color='black'),
    showlegend=False
))

fig.update_geos(showcountries=True, showcoastlines=True, projection_type='natural earth')
fig.update_layout(title="🌍 Average Coffee Cup Score with Country Labels")

st.plotly_chart(fig)


# cupper

st.title("🔍 What Influences Cupper's Overall Score?")

st.markdown("""
**Cupper_Points** is the overall score given by a professional coffee taster.  
Let’s explore which sensory features (like aroma, acidity, flavor) most strongly influence their score.
""")

# Select relevant features
quality_cols = ['Aroma', 'Flavor', 'Aftertaste', 'Acidity', 'Body', 
                'Balance', 'Uniformity', 'Clean_Cup', 'Sweetness', 'Cupper_Points']

corr_matrix = df[quality_cols].corr()

# Sort correlations with Cupper_Points
cupper_corr = corr_matrix['Cupper_Points'].drop('Cupper_Points').sort_values(ascending=False)

st.subheader("📊 Feature Importance: Correlation with Cupper_Points")

# Show sorted bar chart of correlations
st.bar_chart(cupper_corr)

# Heatmap of all correlations
st.subheader("🧪 Correlation Heatmap of Quality Attributes")
fig, ax = plt.subplots(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
ax.set_title("Correlation Between Cupper Points and Other Attributes")
st.pyplot(fig)

# Summary
st.subheader("📌 Interpretation")
st.markdown(f"""
The attributes most strongly correlated with **Cupper_Points** are:

- 🥇 **Flavor**: {cupper_corr['Flavor']:.2f}
- 🥈 **Aftertaste**: {cupper_corr['Aftertaste']:.2f}
- 🥉 **Balance**: {cupper_corr['Balance']:.2f}
- 🌟 **Aroma** and **Acidity** also play significant roles.

Lower correlations with:
- 🔹 **Sweetness**: {cupper_corr['Sweetness']:.2f}
- 🔹 **Clean_Cup**: {cupper_corr['Clean_Cup']:.2f}
- 🔹 **Uniformity**: {cupper_corr['Uniformity']:.2f}

These results suggest the cupper score is driven by overall flavor experience rather than technical perfection.
""")