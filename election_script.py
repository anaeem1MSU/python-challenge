#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# Read the csv file
df = pd.read_csv('C:/Users/theen/Downloads/Starter_Code (11)/Starter_Code/PyPoll/Resources/election_data.csv')

# Calculate the total number of votes cast
total_votes = df.shape[0]

# Get a complete list of candidates who received votes
candidates = df['Candidate'].unique()

# Calculate the total number of votes and the percentage of votes each candidate won
vote_counts = df['Candidate'].value_counts()
vote_percentages = df['Candidate'].value_counts(normalize=True) * 100

# Determine the winner of the election based on popular vote
winner = vote_counts.idxmax()

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidates:
    print(f"{candidate}: {vote_percentages[candidate]:.3f}% ({vote_counts[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")


# In[ ]:




