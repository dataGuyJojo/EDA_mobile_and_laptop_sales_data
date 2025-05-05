# EDA mobile and laptop sales data

These are the guided questions that will be followed to do the EDA
This is the dataSet: [Kaggle](https://www.kaggle.com/datasets/vinothkannaece/mobiles-and-laptop-sales-data)

---

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
---


📊# Unveiling Sales Trends: An EDA of Mobile and Laptop Sales
(using randomly generated data for EDA)
Understanding what sells, where it sells, and who buys it is the heart of any data-driven business. Recently, I explored a fascinating dataset from Kaggle containing sales data of mobile phones and laptops across Indian regions over a period of two years. The goal? To extract insights that could empower better decision-making for marketing, inventory, and customer strategy.

---

🔍# About the Dataset
This dataset includes detailed transaction-level sales records. Each row represents a unit sold and includes:
Product Type (Mobile or Laptop)
Brand
Price
Quantity Sold
Region
Processor Specification
RAM, ROM
Inward and Dispatch Dates

The data spans from March 2023 to May 2025, covering over 265,000 records. Perfect for a comprehensive EDA.

---

📌 # What Questions Did I Ask?
To guide my analysis, I followed a layered approach - starting from simple distributions to more business-specific questions:

---

🧩 Basic Questions
What's the product distribution?
 Turns out, it's almost perfectly balanced:

Laptops: 138,019 units (50.06%)
Mobile Phones: 127,670 units (49.94%)

2.  Who dominates in brand sales?
Apple leads the laptop market.
Google sells the most mobile phones.

3. What's the average price by type?
 Surprisingly close!
Laptops average ₹102,784
Mobiles average ₹102,498

This suggests similar pricing strategies across both categories.

---

🎯 Intermediate Analysis
How do sales trend over time?
 I visualized monthly revenue using a line plot. The sales volume remains relatively steady but peaks in August 2023 and again in March 2024.
Which regions buy the most?
 The West region clearly dominates - both in laptops and mobile sales. This could be due to higher urbanization or tech-savvy customer base.
Top Customers by Quantity Sold
 Some customers are loyal and bulk buyers:

Robert Smith (117 units)
Michael Johnson (113 units)
Michael Williams (110 units)

These insights could guide CRM strategies or targeted loyalty programs.
4. Does more RAM mean a higher price?
 I plotted RAM vs Price, and there is a visible, albeit moderate, positive correlation. More RAM generally means higher price, but other specs (like processor or brand) influence it too.
5. Which processors are most popular?
Top Mobile Processors:
MediaTek Dimensity - 20,063 units sold
Samsung Exynos - 19,928 units sold
Snapdragon 7s - 19,771 units sold

Top Laptop Processors:
Intel i9–17,671 units sold
Intel i5–17,613 units sold
Ryzen 3–17,531 units sold

Visualizing this gave clear trends in buyer preference.

---

🧠 Advanced Insights
Which months bring the highest revenue?
 I calculated monthly revenue (Price × Quantity Sold). 

Top month?
August 2023: ₹1.27 billion
Followed by March 2024 and October 2024

Here's how the revenue distributes by quarter:
Q4: ₹7.15 billion
Q3: ₹7.09 billion 
Q1: ₹7.06 billion
Q2: ₹6.96 billion

Revenue is remarkably consistent across quarters, which speaks to the product category's resilience.
2. i7 vs Ryzen 7 - Who wins?
Units sold: Ryzen 7 (17,300) , i7 (16,913) Ryzen Wins
Revenue: i7 edges ahead with ₹1.77 billion vs ₹1.74 billion

This suggests that i7 models are priced higher - perhaps due to premium configurations.
3. Which category has higher dispatch delays?
 I calculated the delay between Inward Date and Dispatch Date.
Laptops: 30.60 days average delay
Mobiles: 30.58 days

Almost identical - but laptops show slightly more variability.

---

📈 Visuals That Told the Story
A picture is worth a thousand rows. I used several visualizations to explore patterns:
Line chart for monthly revenue trends
Bar plots for processor popularity
Scatter plot for RAM vs Price
Stacked bar chart for region-wise revenue by product

These visuals not only made the analysis clearer but also helped validate assumptions visually.

---

💡 Key Takeaways
West India is the top-performing region.
Apple and Google lead in laptops and mobiles, respectively.
August is a hot month for sales - plan promotions around it.
i7 processors, while sold less than Ryzen 7, generate higher revenue.
Dispatch delays are consistent - but can be optimized for laptops.

---

🚀 Final Thoughts
Exploratory Data Analysis isn't just about numbers - it's about storytelling. From understanding when people buy to what they prefer and how much they spend, this analysis uncovers multiple business levers.
In real-world terms, such insights can:
Help optimize stock before peak months
Enable dynamic pricing strategies
Improve delivery logistics
Guide customer segmentation

This was a rewarding exercise in turning raw data into actionable insights. I'd love to hear your thoughts - how would you take this analysis further?

---

🔗 Dataset: Kaggle - Mobile & Laptop Sales Data
 📌 Tools: Python, Pandas, Seaborn, Matplotlib
 #EDA #DataScience #Python #SalesAnalysis #Kaggle #LinkedInArticles #Analytics
