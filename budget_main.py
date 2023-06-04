#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd

# Load the dataset
df = pd.read_csv('C:/Users/theen/Downloads/Starter_Code (11)/Starter_Code/PyBank/Resources/budget_data.csv')

# Calculate total months
total_months = df['Date'].count()

# Calculate net total amount of "Profit/Losses" over the entire period
net_total = df['Profit/Losses'].sum()

# Calculate changes in "Profit/Losses" over the entire period
df['Changes'] = df['Profit/Losses'].diff()
average_change = df['Changes'].mean()

# Calculate greatest increase in profits (date and amount) over the entire period
greatest_increase = df['Changes'].max()
greatest_increase_date = df.loc[df['Changes'] == greatest_increase, 'Date'].iloc[0]

# Calculate greatest decrease in profits (date and amount) over the entire period
greatest_decrease = df['Changes'].min()
greatest_decrease_date = df.loc[df['Changes'] == greatest_decrease, 'Date'].iloc[0]

# Print the analysis
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




