
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

file_to_load = "Resources/purchase_data.csv"

#Read File and store into Pandas dataframe
purchase_data = pd.read_csv(file_to_load)


# In[2]:


##PLAYER COUNT
#Display total number of players
player_demo = purchase_data.loc[:, ["Gender","SN","Age"]]
player_demo = player_demo.drop_duplicates()
no_players = player_demo.count()[0]

pd.DataFrame({"Total Players": [no_players]})


# In[3]:


## TOTAL PURCHASING ANALYSIS
# Run Basic Calculations
avg_item_price = purchase_data["Price"].mean()
tot_pur_value = purchase_data["Price"].sum()
pur_count = purchase_data["Price"].count()
item_count = len(purchase_data["Item ID"].unique())

# Create a summary dataframe to hold the results
summary_table = pd.DataFrame({"Number of Unique Items": item_count,
                              "Total Revenue": [tot_pur_value],
                              "Number of Purchases": [pur_count],
                              "Avg Price": [avg_item_price]})

summary_table = summary_table.round(2)
summary_table ["Avg Price"] = summary_table["Avg Price"].map("${:,.2f}".format)
summary_table ["Number of Purchases"] = summary_table["Number of Purchases"].map("{:,}".format)
summary_table ["Total Revenue"] = summary_table["Total Revenue"].map("${:,.2f}".format)
summary_table = summary_table.loc[:,["Number of Unique Items", "Avg Price", "Number of Purchases", "Total Revenue"]]

#Display the summary table
summary_table


# In[4]:


##GENDER DEMOGRAPHICS
# Calculate the Number and Percentage by Gender
gender_demo_tot = player_demo["Gender"].value_counts()
gender_demo_percent = gender_demo_tot / no_players * 100
gender_demo = pd.DataFrame({"Total Count": gender_demo_tot, "Percentage of Players": gender_demo_percent})

gender_demo = gender_demo.round(2)

#Show Table
gender_demo


# In[5]:


## GENDER PURCHASING ANALYSIS
#Basic Calculations
gender_pur_tot = purchase_data.groupby(["Gender"]).sum()["Price"].rename("Total Purchase Value")
gender_avg = purchase_data.groupby(["Gender"]).mean()["Price"].rename("Avg Purchase Value")
gender_count = purchase_data.groupby(["Gender"]).count()["Price"].rename("Purchase Num")

# Summary dataframe to hold the results
gender_total = gender_pur_tot / gender_demo["Total Count"]

gender_data = pd.DataFrame({"Purchase Num": gender_count, "Avg Purchase Price": gender_avg, "Total Purchase Value": gender_pur_tot, "Avg Total Per Person": gender_total})

gender_data["Total Purchase Value"] = gender_data["Total Purchase Value"].map("${:,.2f}".format)
gender_data["Purchase Num"] = gender_data["Purchase Num"].map("{:,}".format)
gender_data["Avg Purchase Price"] = gender_data["Avg Purchase Price"].map("${:,.2f}".format)
gender_data["Avg Total Per Person"] = gender_data["Avg Total Per Person"].map("${:,.2f}".format)
gender_data = gender_data.loc[:, ["Purchase Num", "Avg Purchase Price", "Total Purchase Value", "Avg Total Per Person"]]

# Display Table
gender_data


# In[6]:


## AGE DEMOGRAPHICS
# Establish bin
age_bins = [0,9.90,14.90,19.90,24.9,29.9,34.90,39.90,99999]
age_group = ["<10","10-14","15-19","20-24","25-29","30-34","35-39","40+"]

# Categorize existing players in age bins
player_demo["Age Groups"] = pd.cut(player_demo["Age"], age_bins, labels=age_group)

# Calculate by Age Group
age_demo_total = player_demo["Age Groups"].value_counts()
age_demo_percent = age_demo_total / no_players * 100
age_demo = pd.DataFrame({"Total Count": 
age_demo_total, "Percentage of Players":
age_demo_percent})

age_demo = age_demo.round(2)

#Age Demo Table
age_demo.sort_index()


# In[7]:


##AGE PURCHASING ANALYSIS
#Bin the purchase_data dataframe by age
purchase_data["Age Groups"]= pd.cut(purchase_data["Age"], age_bins, labels=age_group)

#calculations
age_pur_tot = purchase_data.groupby(["Age Groups"]).sum()["Price"].rename("Total Purchase Value")
age_avg = purchase_data.groupby(["Age Groups"]).mean()["Price"].rename("Average Purchase Price")
age_counts = purchase_data.groupby(["Age Groups"]).count()["Price"].rename("Purchase Num")

# Calculate total purchase
age_total = age_pur_tot / age_demo["Total Count"]

# Convert to DataFrame
age_data = pd.DataFrame({"Purchase Num": age_counts, "Avg Purchase Price": age_avg, "Total Purchase Value": age_pur_tot, "Avg Total Per Person": age_total})

age_data ["Purchase Num"] = age_data["Purchase Num"].map("{:,}".format)
age_data["Avg Purchase Price"] = age_data["Avg Purchase Price"].map("${:.2f}".format)
age_data["Total Purchase Value"] = age_data["Total Purchase Value"].map("${:.2f}".format)
age_data["Avg Total Per Person"] = age_data["Avg Total Per Person"].map("${:.2f}".format)
age_data = age_data.loc[:, ["Purchase Num", "Avg Purchase Price", "Total Purchase Value", "Avg Total Per Person"]]

# Display the Age Table
age_data


# In[13]:


##TOP SPENDERS
#Calculation
user_total= purchase_data.groupby(["SN"]).sum()["Price"].rename("Total Purchase Value")
#print(user_total.sort_values(ascending=False))
user_average= purchase_data.groupby(["SN"]).mean()["Price"].rename("Avg Purchase Price")
user_count= purchase_data.groupby(["SN"]).count()["Price"].rename("Purchase Num")

user_data = pd.DataFrame({"Total Purchase Value": user_total, "Avg Purchase Price": user_average, "Purchase Num": user_count})


user_data = user_data.sort_values("Total Purchase Value", ascending=False)
user_data["Avg Purchase Price"]= user_data["Avg Purchase Price"].map("${:.2f}".format)
#user_data = user_data.sort_values("Avg Purchase Price",ascending=False)
user_data["Total Purchase Value"]= user_data["Total Purchase Value"].map("${:.2f}".format)
#user_data.sort_values("Total Purchase Value",ascending=False)
user_data= user_data.loc[:,["Purchase Num", "Avg Purchase Price", "Total Purchase Value"]]

# Display Table
user_data.head()


# In[21]:


##Most POpular Items
# Extract item Data
item_data = purchase_data.loc[:,["Item ID", "Item Name", "Price"]]

# Perform basic calculations

total_item_purchase = item_data.groupby(["Item ID", "Item Name"]).sum()["Price"].rename("Total Purchase Value")
avg_item_purchase = item_data.groupby(["Item ID", "Item Name"]).mean()["Price"]
item_count = item_data.groupby(["Item ID", "Item Name"]).count()["Price"].rename("Purchase Num")

item_data_pd = pd.DataFrame({"Total Purchase Value":total_item_purchase, "Item Price":avg_item_purchase, "Purchase Num":item_count})

item_data_pd = item_data_pd.sort_values("Purchase Num", ascending=False).head(5)
item_data_pd["Item Price"] = item_data_pd["Item Price"].map("${:.2f}".format)
item_data_pd ["Purchase Num"] = item_data_pd["Purchase Num"].map("{:,}".format)
item_data_pd["Total Purchase Value"] = item_data_pd["Total Purchase Value"].map("${:.2f}".format)
item_data_pd = item_data_pd.loc[:,["Purchase Num", "Item Price", "Total Purchase Value"]]

#Display the Item Table
item_data_pd


# In[26]:


##MOst Profitable
# Display Item Table (Sorted by Total Purchase Value)
item_data_pd_new = item_data_pd.sort_values("Total Purchase Value",ascending=False).head(5)
item_data_pd_new


# In[ ]:


'''# Observed Trends
1.Age group(20-24)with 44.79 % is the key demographic group with maximum participants, followed by (15 -19) with 18.58%
2.From the total of 576 players, the vast majority are male (84.3%) generating 82.68% of total revenue.
3.Oathbreaker,Last Hope of the Breaking Storm is the most profitable item despite of selling
    at a lower cost($4.43) than other top sellers.
'''

