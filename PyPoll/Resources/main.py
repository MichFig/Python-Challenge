# import the os module
import os
import csv
csvpath = os.path.join('election_data.csv')

#Set Variables
total_votes = 0
Khan_votes = 0
Correy_votes = 0
Li_votes = 0
OTooley_votes = 0

# Method 2: Improved Reading using CSV module
with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)  
# Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
# Read each row of data after the header
    for row in csvreader:
        voter_id = row[0]
        county = row[1]
        candidate = row[2]
        total_votes +=1
        
        if candidate == 'Khan':
            Khan_votes += 1
        elif candidate == 'Correy':
            Correy_votes +=1
        elif candidate == 'Li':
            Li_votes +=1
        elif candidate == 'O\'Tooley':
            OTooley_votes +=1        
    KP = Khan_votes / total_votes * 100 
    CP = Correy_votes / total_votes * 100
    LP = Li_votes / total_votes * 100
    OP = OTooley_votes / total_votes * 100
    
    most_votes = max(Khan_votes, Correy_votes, Li_votes, OTooley_votes)
        
    if most_votes == Khan_votes:
        winner = 'Khan'
    elif most_votes == Correy_votes:
        winner = 'Correy'
    elif most_votes == Li_votes:
        winner = 'Li'
    elif most_votes == OTooley_votes:
        winner = 'O\'Tooley'
    
    
#Print to terminal 
print(f"Total Votes: {total_votes}")
print('Khan: %3.3f' % KP, Khan_votes)  
print('Correy: %3.3f' % CP,  Correy_votes)
print('Li: %3.3f' % LP,  Li_votes)
print("O'Tooley: %3.3f" % OP,  OTooley_votes ) 


print(f"Winner: {winner}")

#print to file
