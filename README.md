# python-challenge
UCI Bootcamp - Module 3 Challenge
Used Python to analyze two data sets: PyBank and PyPoll

PyBank:
The PyBank data set consists of financial data. It contains two columns: "Date" and "Profit/Loss"
The goal is to:
1.) Calculate:
    - Total Months
    - Net Total Profit
    - Change in Profit/Loss for each month
    - Average Change in Profit/Losses
2.) Find:
    - Greatest increase in profits
    - Greatest decrease in profits

The change in Profit/Loss for each month was stored in a list. 
The Average Change in Profit/Losses was calculated by taking the sum of the Change in Profit/Loss and dividing by the length of the change in Profit/Loss list.


PyPoll:
The PyPoll data set consists of election data and has three columns: "Voter ID", "County", and "Candidate".
The goal is to find the winning candidate.

The winning candidate is the candidate with the most amount of votes. The following information was used to find the winning candidate:
- Total votes
- A list of the unique candidates
- Total votes per candidate
- Percentage of votes per candidate = Total votes per candidate / Total votes * 100

The unique candidates and corresponding vote values were stored in a dictionary with the dictionary keys as candidate names and their corresponding election results as key values.


