import streamlit as st
from utils.load_data import load_data

st.set_page_config(page_title="Coffee Quality Explorer Dashboard", layout="wide")

st.title("☕ Global Coffee Quality Dashboard")
st.markdown("""
Welcome to the **Coffee Quality Explorer** — a data-driven tool that helps you discover the perfect coffee region based on your personal taste preferences.

### 🔍 About the Project
This project is built using a real-world dataset originally published on the [Coffee Quality Institute Database](https://database.coffeeinstitute.org/), and sourced via Kaggle. It includes detailed evaluations of coffee samples from farms around the world — including sensory scores, processing methods, altitude information, and more.

### 🎯 Project Focus
We focus on **coffee quality attributes** such as:
- Aroma
- Flavor
- Acidity
- Sweetness
- Body
- Aftertaste
...and more — each rated on a scale from 1 to 10

By adjusting sliders based on your preferred flavor profile, you'll receive a personalized list of farms and regions that most closely match your ideal coffee experience.

### 🌍 What You Can Do
- Explore top coffee-producing regions based on your taste
- Filter by **processing method**, such as Washed, Natural, or Honey
- Visualize correlations between quality attributes and overall rating

---

Whether you're a coffee enthusiast, roaster, or just curious, this app provides insights into what makes great coffee — and where to find it.
""")

# Display an image
st.image(r"C:\Users\sarah\app\pages\coffee_farm.png", caption="coffee farm", width=300)



