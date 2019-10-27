#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv
from pathlib import Path


# In[2]:


csvpath = Path('election_data.csv')
total_votes = 0
unique_candidates = []
vote_count = []


# In[3]:


with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        total_votes=total_votes+1
        candidate = (row[2])
        if candidate in unique_candidates:
            candidate_index = unique_candidates.index(candidate)
            vote_count[candidate_index] = vote_count[candidate_index] + 1
        else:
            unique_candidates.append(candidate)
            vote_count.append(1)


# In[4]:


percentage = []
max_votes = vote_count[0]
max_index = 0

for x in range(len(unique_candidates)):
    #calculation to get the percentage, x is the looper value
    vote_percentage = round(vote_count[x]/total_votes*100, 4)
    percentage.append(vote_percentage)
    
    if vote_count[x] > max_votes:
        max_votes = vote_count[x]
        max_index = x

election_winner = unique_candidates[max_index] 


# In[7]:


print('---------------------------')
print('Election Results')
print('---------------------------')
print(f'Total Votes: {total_votes}')
print('---------------------------')
for x in range(len(unique_candidates)):
    print(f'{unique_candidates[x]} : {percentage[x]}% ({vote_count[x]})')
print('---------------------------')
print(f'Winner: {election_winner.upper()}')
print('---------------------------')


# In[8]:


output = os.path.join("pypoll_election_results.txt")
with open(output, "w", newline="") as datafile:
    datafile.write('---------------------------\n')
    datafile.write('Election Results\n')
    datafile.write('---------------------------\n')
    datafile.write(f'Total Votes: {total_votes}\n')
    datafile.write('---------------------------\n')
    for x in range(len(unique_candidates)):
        datafile.write(f'{unique_candidates[x]} : {percentage[x]}% ({vote_count[x]})\n')
    datafile.write('---------------------------\n')
    datafile.write(f'Election winner: {election_winner.upper()}\n')
    datafile.write('---------------------------')


# In[ ]:





# In[ ]:




