# 📊 EDA of Mobile and Laptop Sales Data (Mar 2023 – May 2025)

An in-depth Exploratory Data Analysis (EDA) project based on 50,000+ sales records of mobile and laptop products. The dataset includes customer purchases, product specs, prices, dispatch dates, and more — offering a great opportunity to extract business insights through data storytelling.

---

## 🔗 Links

- 📘 **Kaggle Notebook**: [View Notebook](https://www.kaggle.com/code/syedasifjohan/eda-of-mobile-and-laptop-sales-data/)
- ✍️ **Medium Blog**: [Read Article](https://medium.com/@connect.syedasifjohan/unveiling-sales-trends-an-eda-of-mobile-and-laptop-sales-82592f591019)
- 📊 **Dataset on Kaggle**: [Mobiles and Laptop Sales Data](https://www.kaggle.com/datasets/vinothkannaece/mobiles-and-laptop-sales-data)

---

## 📌 Project Brief

This project analyzes sales transactions from March 2023 to May 2025, focusing on brand performance, regional sales, pricing patterns, and processor preferences. The goal is to identify sales trends and actionable insights using Python and popular data libraries.

---

## 🛠️ Tools & Libraries

- Python 3
- Pandas
- Matplotlib
- Seaborn
- Colab Notebook

---

## 🔄 Project Flow

- **🔍 Data Collection**  
  Dataset collected from Kaggle, containing detailed records of mobile and laptop sales.

- **🧹 Data Cleaning & Preprocessing**  
  Cleaned missing values, converted data types, and created new time-related features like month and quarter.

- **📊 Exploratory Data Analysis (EDA)**  
  Performed groupings and aggregations to analyze trends across brands, regions, product types, and processors.

- **📈 Data Visualization**  
  Visualized monthly revenues, top brands, regional distributions, and processor-wise sales using Matplotlib and Seaborn.

- **💡 Insight Extraction**  
  Derived insights around pricing similarities, customer behavior, and product-category performance.

- **📤 Reporting & Sharing**  
  Published the analysis through a well-structured Jupyter Notebook and shared it across Kaggle, Medium, and GitHub.

---


**These are the guided questions that will be followed to do the EDA**

# 🧩 Basic (3 questions)

1. **What is the distribution of products sold?**
    
    (Count of *Mobile Phones* vs *Laptops*)

    **Ans**: Total laptop sold was: 138019 (50.06% of data)
    and, total mobile sold was; 127670 (49.94% of data)
    
2. **Which brand has the highest number of sales (quantity sold)?**

   **Ans**: Apple(Laptop), Google(Mobile)
3. **What is the average price of products by type (Mobile Phone vs Laptop)?**

   **Ans**: Average prices for laptops is 102784.61 rupees and average price for a mobile phone is 102498.01 rupees

---

# 🎯 Intermediate (5 questions)

1. **What is the trend of sales over time?** (visual_later)
    
    (Use *Inward Date* or *Dispatch Date* for a time series)
    
<br>

    
2. **Which region (Central, South, East) buys the most products overall?**
  -> West buyes the most mobile phones (28007) and laptops (28595)

<br>

  
3. **Top 5 customers who purchased the most (based on Quantity Sold)?**

| Customer Name     | Region | Quantity Sold |
|-------------------|--------|----------------|
| Robert Smith      | West   | 117            |
| Michael Johnson   | South  | 113            |
| Michael Williams  | West   | 110            |
| John Smith        | North  | 107            |
| James Brown       | East   | 99             |


4. **Is there any relation between the RAM size and price?**
    
    (Maybe a scatter plot)
    
<br>

5. **Which processor type is the most common among sold products?**
    
    (*Processor Specification* analysis)

    **Ans:** Top 3 mobile processors and top 3 Laptop Processors

| Processor Specification | Product     | Quantity Sold |
|-------------------------|-------------|---------------|
| MediaTek Dimensity      | Mobile Phone| 20063         |
| Samsung Exynos          | Mobile Phone| 19928         |
| Snapdragon 7s           | Mobile Phone| 19771         |
| i9                      | Laptop      | 17671         |
| i5                      | Laptop      | 17613         |
| Ryzen 3                 | Laptop      | 17531         |


<br>


---

# 🧠 Advanced (3 questions)

1. **Which month had the highest total sales revenue?**
    
    (Revenue = Price × Quantity Sold, group by month)

| Month Name     | Quantity Sold | Revenue (Formatted_str) |
|----------------|----------------|--------------------------|
| August 2023    | 12,224         | ৳1,273,073,633           |
| March 2024     | 12,164         | ৳1,244,000,047           |
| October 2024   | 11,712         | ৳1,228,183,686           |
| August 2024    | 11,692         | ৳1,221,646,578           |
| December 2023  | 11,866         | ৳1,209,435,055           |
| October 2023   | 11,690         | ৳1,203,487,840           |
| July 2024      | 11,773         | ৳1,198,454,453           |
| December 2024  | 11,476         | ৳1,198,076,421           |
| April 2024     | 11,458         | ৳1,197,595,357           |
| January 2024   | 11,573         | ৳1,178,292,062           |

Most sold was Aug 2023.

If we check Quarterly,

| Quarters | Quantity Sold |     Revenue     | Percentage Quarter |
|----------|----------------|------------------|---------------------|
| Q4       |     69,258     | 7,156,666,880    |       25.31%        |
| Q3       |     69,012     | 7,093,968,715    |       25.09%        |
| Q1       |     69,047     | 7,062,865,735    |       24.98%        |
| Q2       |     68,372     | 6,965,579,792    |       24.63%        |

Q4 is the quarter where most of the sale comes from. though the quarters are very evenly distributed revenue wise.

<br>

    
2. **Compare the sales performance of 'i7' vs 'Ryzen 7' processors.**
    
    (Total quantity sold or revenue)

    **Ans:** Ryzen 7 sold more units. But i7 generated more Revenue

| **Processor** | **Quantity Sold** | **Revenue** |
| --- | --- | --- |
| **i7** | 16913 | 1769318353 |
| **Ryzen 7** | 17300 | 1743525557 |

<br>
    

3. **Do laptops or mobile phones have a higher average dispatch delay?**
    
    (Calculate days between *Inward Date* and *Dispatch Date*)
    (Calculate days between *Inward Date* and *Dispatch Date*)

**Ans:** Both have similar dispatch delay (Avg. (Inward date - Dispatch Date)) and similar Standard Deviation. But Laptop has slightly more delay and more std deviation

| **Product** | **Average Delay** | **Std Deviation** |
| --- | --- | --- |
| **Laptop** | 30.599 | 17.385 |
| **Mobile Phone** | 30.586 | 17.260 |

<br>

    

---



## 🧠 Key Insights

- 📱 **Balanced Market**: Sales were evenly distributed between laptops and mobile phones.
- 💰 **Price Similarity**: Average prices for laptops and mobiles were surprisingly close (~₹102K).
- 🌍 **Regional Sales**: Western India dominated sales in both categories.
- 🧑‍💼 **Bulk Buyers**: Certain customers bought over 100 units.
- 🧠 **Processor Trends**: MediaTek and Exynos led in mobile sales; Intel i9 and Ryzen 3 dominated laptops.
- ⏳ **Dispatch Delays**: Average dispatch times were ~30 days for both categories.

---

# ✅Conclusion
This project served as a comprehensive exercise in exploratory data analysis, enabling a deep understanding of both the dataset and the business context behind mobile and laptop sales. From uncovering dominant brands and pricing strategies to identifying regional performance and customer behavior, this analysis highlights how EDA can drive meaningful insights for strategic decision-making.

It also helped me strengthen my skills in data cleaning, visualization, and storytelling — while improving my ability to present findings clearly through notebooks and blog posts.




