https://www.kaggle.com/datasets/volpatto/coffee-quality-database-from-cqi
https://database.coffeeinstitute.org/


clean the dataset
1 bag weight in kg all
2 Harvest.Year



## ✅ **Final Project Title:**

A dashboard that uses data to track the performance of farms and the impact on coffee Quality


---

## 🎯 **Project Goal:**

To build an end-to-end data analysis pipeline that identifies key quality factors in coffee production and supports farm/product decision-making using dashboards powered by SQL, Python, and Streamlit or Tableau/Power BI.

---

## 🧱 **Proposed Project Pipeline (Based on Your Columns):**

### 🔹 1. **Data Understanding**

* Get familiar with fields like:

  * **Quality scores**: Aroma, Flavor, Aftertaste, Acidity, etc.
  * **Origin attributes**: Country, Region, Farm.Name, Variety, Processing.Method
  * **Certification** and **Altitude** info

---

### 🔹 2. **Data Cleaning & Wrangling** *(Python/Pandas + SQL)*

* Drop or fix `Unnamed: 0`, missing `Altitude` values, duplicates
* Convert dates (like `Grading.Date`, `Expiration`) to datetime
* Normalize `Region`, `Variety`, `Processing.Method` strings
* Create new variables like:

  * `High_Quality` = 1 if `Total.Cup.Points > 85`
  * `Altitude Category`: Low (<1000m), Medium, High (>1500m)

---

### 🔹 3. **SQL Analysis**

Use SQL (via SQLite or PostgreSQL) to:

* Group farms by average `Total.Cup.Points`
* Compare average quality by `Country.of.Origin`
* Analyze impact of `Processing.Method` on quality
* Rank top `Farm.Name` by `Cupper.Points`
* Query defect types vs `Sweetness`/`Clean.Cup` scores

---

### 🔹 4. **Feature Engineering**

* `Quality Score` = mean of Aroma, Flavor, Aftertaste, etc.
* `Defect Ratio` = (Category.One.Defects + Category.Two.Defects) / Number.of.Bags
* Flag `Certified` vs `Non-Certified` farms

---

### 🔹 5. **Exploratory & Statistical Analysis**

* Correlation heatmap of cup quality metrics
* Altitude vs Quality: regression line
* Impact of region or variety on `Total.Cup.Points`

---

### 🔹 6. **Dashboard Visualization** *(Streamlit OR Tableau/Power BI)*

Include:

* **Map** of farms by country with quality scores
* **Bar charts** of average scores by processing method
* **Filters**: by country, certification, variety
* **Line chart** for quality over harvest years
* **Scatter plot**: Altitude vs Total Cup Points
* **Summary KPIs**: Top countries, average quality, avg. defects

---


## 🧾 Optional Enhancements

* Add ML: Predict high-quality coffee using logistic regression or decision trees
* Cluster farms by cup profile using KMeans

---

Would you like a template folder structure or Streamlit layout sketch for this project next?
