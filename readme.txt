Datasets sources:

https://www.kaggle.com/datasets/volpatto/coffee-quality-database-from-cqi
https://database.coffeeinstitute.org/
PowerPoint:
https://prezi.com/view/bW2zNTSsKvMG5E6IVi5h/

Final Project: 

A dashboard that uses data to track the performance of farms and the impact on coffee Quality


Project Goal:

To build an end-to-end data analysis pipeline that Identifies key quality factors in coffee production and supports decision-making at farm and product level using dashboards powered by Python and Streamlit.


Proposed Project Pipeline:
Data Overview:
Quality scores**: Aroma, Flavor, Aftertaste, Acidity, etc.
Origin attributes**: Country, Region, Farm.Name, Variety, Processing.Method
Certification** and Altitude info
44 Columns/ 1339 rows
two csv files arabica and robusta
one merged csv file
Farm & region details
Processing method
total cup points


Data Cleaning & Wrangling:
using Python/Pandas + SQL
Dashboard Visualization (Streamlit)
Checking for Missing Data
Cleaned and standardized 44 columns (name, type etc.)
dropped Columns that don't support the goal
Merged region & country into a single field
dropping null values
filling null values
data aggregation and grouping
understang streamlit errors
apply multiple filters(python)
compute Euclidean distances and match user input with coffee profiles (np.linalg.norm())
st.session_state to store user input, match scores, and the full dataset


The attributes most strongly correlated with Cupper_Points are:

🥇 Flavor: 0.79
🥈 Aftertaste: 0.79
🥉 Balance: 0.72
🌟 Aroma and Acidity also play significant roles.
Lower correlations with:

🔹 Sweetness: 0.22
🔹 Clean_Cup: 0.36
🔹 Uniformity: 0.36
These results suggest the cupper score is driven by overall flavor experience rather than technical perfection

What You Can Do with the App (in Streamlit)
Explore top coffee-producing regions based on your taste
Filter by processing method, such as Washed, Natural, or Honey
Visualize correlations between quality attributes and overall rating


