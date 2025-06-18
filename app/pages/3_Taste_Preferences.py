import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

# Load data
@st.cache_data
def load_data():
    df = pd.read_excel(r"C:\Users\sarah\OneDrive\Documentos\GitHub\Final-Project\cleaned_version.xlsx")
    return df.dropna(subset=qualities + ['Total_Cup_Points', 'Country_of_Origin', 'Farm_Name'])

# --- Define Quality Attributes ---
qualities = ['Aroma', 'Flavor', 'Aftertaste', 'Acidity', 'Body',
             'Balance', 'Uniformity', 'Clean_Cup', 'Sweetness', 'Cupper_Points']

# --- Streamlit UI ---
st.title("☕ Find Your Ideal Coffee Match")

df = load_data()

st.sidebar.header("🎯 Select Your Preferred Quality Profile (1–10)")
user_input = {q: st.sidebar.slider(q, 0.0, 10.0, 7.5, 0.1) for q in qualities}
user_df = pd.DataFrame([user_input])

# --- Compute Match Score ---
df['Match_Score'] = df[qualities].apply(
    lambda row: -np.linalg.norm(row.values - np.array(list(user_input.values()))), axis=1
)
# np.linalg.norm(...)This calculates the Euclidean distance between the two vectors.
# negating the result to turn small distances into bigger match scores, so higher Match_Score = better match.
#Lower distance = more similar to user's input.

# --- Total Preference Sum ---
user_sum = user_df.sum(axis=1).values[0]
st.markdown(f"### 🧾 Your Total Preference Score: **{user_sum:.2f}**")

# --- Top Matches ---
top_matches = df.sort_values(by='Match_Score', ascending=False).head(5)
st.subheader("🏅 Top Matching Farms")
st.dataframe(top_matches[['Farm_Name', 'Region', 'Country_of_Origin', 'Total_Cup_Points']])

# --- Map Coordinates (Optional Predefined) ---
country_coords = {
    "Mexico": [23.6345, -102.5528], "Colombia": [4.5709, -74.2973],
    "Guatemala": [15.7835, -90.2308], "Brazil": [-14.235, -51.9253],
    "United States": [37.0902, -95.7129], "Taiwan": [23.6978, 120.9605],
    "Honduras": [15.2, -86.2419], "Costa Rica": [9.7489, -83.7534],
    "Ethiopia": [9.145, 40.4897], "Tanzania": [-6.3690, 34.8888],
    "Uganda": [1.3733, 32.2903], "Thailand": [15.87, 100.9925],
    "Nicaragua": [12.8654, -85.2072], "Kenya": [-1.2921, 36.8219],
    "El Salvador": [13.7942, -88.8965], "Indonesia": [-0.7893, 113.9213],
    "China": [35.8617, 104.1954], "India": [20.5937, 78.9629],
    "Peru": [-9.19, -75.0152], "Vietnam": [14.0583, 108.2772],
    "Panama": [8.5379, -80.7821], "Ecuador": [-1.8312, -78.1834],
    "Japan": [36.2048, 138.2529], "Rwanda": [-1.9403, 29.8739],
}

top_matches['lat'] = top_matches['Country_of_Origin'].map(lambda c: country_coords.get(c, [None, None])[0])
top_matches['lon'] = top_matches['Country_of_Origin'].map(lambda c: country_coords.get(c, [None, None])[1])
map_df = top_matches.dropna(subset=['lat', 'lon'])

# --- Show Map ---
if not map_df.empty:
    st.subheader("🗺️ Coffee Farm Countries on Map")
    st.pydeck_chart(
        pdk.Deck(
            map_style="mapbox://styles/mapbox/light-v9",
            initial_view_state=pdk.ViewState(
                latitude=0,
                longitude=0,
                zoom=1.5,
                pitch=0,
            ),
            layers=[
                pdk.Layer(
                    "ScatterplotLayer",
                    data=map_df,
                    get_position=["lon", "lat"],
                    get_color=[0, 180, 0, 140],
                    get_radius=300000,
                    pickable=True,
                ),
            ],
        )
    )
# --- Get Top Matches ---
top_matches = df.sort_values(by='Match_Score', ascending=False).head(5)
top_match = top_matches.iloc[0]

# --- Store in Session State ---
st.session_state['user_input'] = user_input
st.session_state['user_sum'] = sum(user_input.values())
st.session_state['top_matches'] = top_matches
st.session_state['df'] = df