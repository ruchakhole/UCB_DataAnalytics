
# coding: utf-8

# In[ ]:


import os
import csv
list = os.listdir()
number_files = len(list)

for numbers in range(number_files):
    electioncsv = os.path.join('/Users/ruchakhole/Desktop/Berkeley/03-Python/Homework/Instructions/PyPoll/Resources/election_data.csv')
    
#empty variables
    County= []
    Candidate = []
    CandidateUnique =[]
    CVoteCount = []
    CVotePercent =[]
    TotalCount = 0

    with open(electioncsv,'r') as csvFile:
        csvReader = csv.reader(csvFile, delimiter=',')
            #skip headers
        next(csvReader, None)

        for row in csvReader: 
            TotalCount = TotalCount + 1
            Candidate.append(row[2])
        for x in set(Candidate):
            CandidateUnique.append(x)
            cc = Candidate.count(x)
            CVoteCount.append(cc)
            CVotePercent.append(Candidate.count(x)/TotalCount)
        
        Winner = CandidateUnique[CVoteCount.index(max(CVoteCount))]

    
    with open('Election_Results_' + str(numbers+1) + '.txt', 'w') as text:
        text.write("Election Results for file 'election_data_"+str(numbers+1) + ".csv'"+"\n")
        text.write("----------------------------------------------------------\n")
        text.write("Total Vote: " + str(TotalCount) + "\n")
        text.write("----------------------------------------------------------\n")
        for i in range(len(set(Candidate))):
            text.write(CandidateUnique[i] + ": " + str(round(CVotePercent[i]*100,1)) +"% (" + str(CVoteCount[i]) + ")\n")
        text.write("----------------------------------------------------------\n")
        text.write("Winner: " + Winner +"\n")
        text.write("----------------------------------------------------------\n")

