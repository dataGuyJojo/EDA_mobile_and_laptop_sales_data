# -*- coding: utf-8 -*-

#Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Upload file
#from google.colab import files
#uploaded = files.upload()

#make the dataframe
df = pd.read_csv(r"mobile_sales_data.csv")
df

df

"""# Data Cleaning"""

#change the missing vales:
df = df.replace(['n/a', 'N/A', 'NaN', 'nan'], '', regex=True)
df = df.fillna('')
df

"""## Now that data has been cleaned: Talking to the data

1. Basic Analysis
"""

df

df2 = df

# Count of total sold
df2 = df.groupby(["Product"], as_index=False)["Quantity Sold"].sum()
df2["Percentage Sold"] = round (df2["Quantity Sold"] / df2["Quantity Sold"].sum() * 100, 2)
df2

"""Ans: Total laptop sold was: 138019 (50.06% of data)
and, total mobile sold was; 127670 (49.94% of gata)
"""

#ne data frame df2, to test adn keep df safe. group_by product, then Brand.
df2 = df.groupby(["Product", "Brand"], as_index=False)["Quantity Sold"].sum()
df2

#use df2 to get the brand that most sold each product (phone and laptops)

df2.sort_values(["Product","Quantity Sold"], ascending=[True, False], inplace=True)
df2

#Top sold
top_sold = df2.groupby('Product').head(1)
top_sold
#Ans: So Apple laptops and Google Phones are the most sold in their category

"""Ans: Apple laptops and Google Phones are the most sold in their category"""

# Average Price by type
df3= df
Average_Price = round(df3.groupby(["Product"], as_index=False)["Price"].mean(), 2)
Average_Price

"""Ans: Average prices for laptops is 102784.61 rupees and average price for a mobile phone is 102498.01 rupees"""

df3

"""## 2. Intermediate

Which region buys the most overall (central, east, west)
"""

df3 = df.groupby(["Region", "Product"], as_index=False)["Quantity Sold"].sum().sort_values("Quantity Sold", ascending=False)
df3

# sort the previous table
df3.sort_values(["Product","Quantity Sold"], ascending=[True, False], inplace=True)
df3

#take top for each
top_sold_Region = df3.groupby('Product').head(1)
top_sold_Region

"""Top 5 customers who purchased the most based on quantity sold"""

df_x =(
    (df[["Customer Name", "Quantity Sold"]])
    .groupby("Customer Name", as_index=False)["Quantity Sold"]
    .sum()
    .sort_values("Quantity Sold", ascending=False)
    .head(5)
        )

Customer_region = df.drop_duplicates(subset = "Customer Name")[["Customer Name", "Region"]]
df_x = pd.merge(df_x, Customer_region, on="Customer Name")

#Re arrange columns
df_x = df_x[["Customer Name", "Region", "Quantity Sold"]]
df_x

"""Which processor type is the most common among sold products?"""

# Calculate top processors
Top_Processors = (df[["Processor Specification", "Quantity Sold", "Product"]]
 .groupby(["Processor Specification", "Product"], as_index=False)["Quantity Sold"]
 .sum()
 .sort_values("Quantity Sold", ascending=False, ignore_index=True)
 )
Top_Processors

#Based on previous Querry(Top_Processors) calculate Top 3 Mobile phone Processors
Top_Mobile_Processors = Top_Processors.query("Product == 'Mobile Phone'").head(3)
Top_Mobile_Processors

#Based on previous Querry(Top_Processors) calculate Top 3 Laptop Processors
Top_Laptop_Processors = Top_Processors.query("Product == 'Laptop'").head(3)

#reset the index
Top_Laptop_Processors.reset_index(drop=True, inplace=True)
Top_Laptop_Processors

# Concatenate the two DataFrames vertically
Top_Processors_Merged = pd.concat([Top_Mobile_Processors, Top_Laptop_Processors], ignore_index=True)

# Display the merged DataFrame
Top_Processors_Merged

"""# Advance

Which Month had the heighest total sales revenue? Using Dispatch date

-> get dispatch month, and revenue |
group by dispatch month and sort by revenue | Take first 10
"""

#Create Revenue
df["Revenue"] = df["Price"] * df["Quantity Sold"]
df

#Convert dispatch date to standard form
df["Dispatch Date"] = pd.to_datetime(df["Dispatch Date"])

#make dispatch month
df["Dispatch Month"] = df["Dispatch Date"].dt.to_period("M")
df

#group by dispatch month and sort by revenue

df6 =(df[["Dispatch Month", "Quantity Sold", "Revenue"]]
 .groupby("Dispatch Month", as_index=False).sum()
 .sort_values("Revenue", ascending=False)
 .reset_index(drop=True)
 .head(10)
 )

df6['Revenue (Formatted_str)'] = df6['Revenue'].apply(lambda x: f"৳{x:,}")
# Convert 'Dispatch Month' from Period to string format like "August 2023"
df6['Month Name'] = df6['Dispatch Month'].astype(str)
df6['Month Name'] = pd.to_datetime(df6['Month Name']).dt.strftime('%B %Y')
df6 = df6[["Month Name", "Quantity Sold", "Revenue (Formatted_str)"]]
df6



#group by dispatch month and sort by revenue
df['Dispatch Date'] = pd.to_datetime(df['Dispatch Date'])  # Ensure datetime
df['Dispatch Quarter'] = df['Dispatch Date'].dt.to_period('Q')


df7 =(df[["Dispatch Quarter", "Quantity Sold", "Revenue"]]
 .groupby("Dispatch Quarter", as_index=False).sum()
 .sort_values("Revenue", ascending=False)
 .reset_index(drop=True)
 )

df7["Quarters"] = df7["Dispatch Quarter"].astype(str).str[-2:]
df7.drop("Dispatch Quarter", axis=1, inplace=True)

#Percentage Quarter
df8 = df7.groupby("Quarters").sum()
df8["Percentage Quarter"] = round((df8["Revenue"] / df8["Revenue"].sum())*100, 2)
df8 = df8.sort_values("Percentage Quarter", ascending=False)
df8

"""**Compare the sales performance of 'i7' vs 'Ryzen 5' processors.**
    
    (Total quantity sold or revenue)
  
"""

df9 = df[df["Processor Specification"].str.contains("i7") | df["Processor Specification"].str.contains("Ryzen 7")]
df9 = (
    df9[["Processor Specification", "Quantity Sold", "Revenue"]]
       .groupby("Processor Specification").sum()
       .sort_values(by = "Revenue", ascending=False)
)
df9

""" **Do laptops or mobile phones have a higher average dispatch delay?**
    
    (Calculate days between Inward Date and Dispatch Date)
"""

df10 = df.copy()
df10["Dispatch Delay"] = (
    pd.to_datetime(df10["Dispatch Date"]) - pd.to_datetime(df10["Inward Date"])
).dt.days

df10 = df10[["Product", "Dispatch Delay"]]

# Calculate both mean and std deviation
Dispatch_Delay_Table = (
    df10.groupby("Product")["Dispatch Delay"]
    .agg(["mean", "std"])
    .rename(columns={"mean": "Average Delay", "std": "Std Deviation"})
    .sort_values("Average Delay", ascending=False)
    .round(3)
)

Dispatch_Delay_Table

"""# Visualisations"""

monthly_sales = df.groupby("Dispatch Month")["Revenue"].sum().reset_index()
monthly_sales["Dispatch Month"] = monthly_sales["Dispatch Month"].astype(str)  # for plotting

monthly_sales

#Plot
plt.figure(figsize=(20,6))
sns.lineplot(x="Dispatch Month", y="Revenue", data=monthly_sales, marker="o")
plt.xticks(rotation=90)
plt.title("Monthly Sales Trend Over Time")
plt.ylabel("Revenue (Billion)")
plt.xlabel("Month")
plt.tight_layout()
plt.show()

"""Region Comparison"""

#Region comparison table
Region_Comp = df
Region_Comp = Region_Comp.groupby("Region")["Revenue"].sum().sort_values(ascending=False)
Region_Comp = Region_Comp.to_frame().reset_index()

df.groupby(["Product", "Region"])["Revenue"].sum()
Region_Comp

# Custom label formatting function
def format_billion(x):
    return f'{x / 1e9:.2f} Billion'  # Convert to billions and format

plt.figure(figsize=(9,5))

# Create bar plot
ax = sns.barplot(x="Region", y="Revenue", data=Region_Comp, hue="Region")

# Iterate over all containers and add formatted labels
for container in ax.containers:
    ax.bar_label(container, labels=[format_billion(val.get_height()) for val in container], fontsize=10)


plt.title("Region Comparison")
plt.ylabel("Revenue (Billion)")
plt.xlabel("Region")
plt.tight_layout()

plt.show()

Laptop_Revenue = (df.groupby(["Product", "Region"])["Revenue"].sum()).loc["Laptop"].reset_index()
Laptop_Revenue.columns = ["Region", "Laptop"]

Region_Comp = Region_Comp.merge(Laptop_Revenue, on="Region", how="left")
Region_Comp
Region_Comp["Mobile Phone"] = Region_Comp["Revenue"] - Region_Comp["Laptop"]
Region_Comp

# Based on region comp Show a stacked barchart
plt.figure(figsize= (9, 4))
plt.bar(Region_Comp["Region"], Region_Comp["Laptop"], label="Laptop")
plt.bar(Region_Comp["Region"], Region_Comp["Mobile Phone"], bottom=Region_Comp["Laptop"], label="Mobile Phone")
plt.title("Region Comparison")
plt.ylabel("Revenue (Billion)")
plt.xlabel("Region")
plt.legend()
plt.tight_layout()
plt.show()

df

# separate laptops and mobile phones

df_laptop = df[df["Product"] == "Laptop"]
df_mobile = df[df["Product"] == "Mobile Phone"]

# To add lables in the charts
def add_labels(x, y):
    for i in range(len(x)):
        plt.text(i, y.iloc[i], y.iloc[i], ha = 'center', bbox = dict(facecolor = 'white', alpha = 0.5))

df_laptop.groupby("Processor Specification")["Quantity Sold"].sum().sort_values(ascending=False)

#for laptops
laptop_processors_visu = df_laptop.groupby("Processor Specification")["Quantity Sold"].sum().sort_values(ascending=False)
laptop_processors_visu

plt.figure(figsize= (15, 4))

plt.bar(x = laptop_processors_visu.index, height = laptop_processors_visu)
plt.ylabel("Quantity Sold", color = "blue")
plt.xlabel("Processor Specification", color = "blue")
plt.title("Laptop Phone Processor Comparison")
add_labels(laptop_processors_visu.index, laptop_processors_visu)

plt.tight_layout()
plt.show()

#for mobile phones
mobile_processors_visu = df_mobile.groupby("Processor Specification")["Quantity Sold"].sum().sort_values(ascending=False)
mobile_processors_visu

plt.figure(figsize= (15, 4))

plt.bar(x = mobile_processors_visu.index, height = mobile_processors_visu)
plt.ylabel("Quantity Sold", color = "blue")
plt.xlabel("Processor Specification", color = "blue")
plt.title("Mobile Phone Processor Comparison")
add_labels(mobile_processors_visu.index, mobile_processors_visu)

plt.tight_layout()
plt.show()
