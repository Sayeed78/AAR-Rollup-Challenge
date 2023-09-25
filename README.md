# AAR-Rollup-Challenge
This is a coding challenge given to me as part of an interview for a industry programing position. 
The goal of this exercise is to demonstrate industy programing practices.

This challenge is outlined in the PDF file AAR-Rollup-Challenge.pdf. The basic description of this
challenge is generate three columns in accounts.csv: ultimate_parent_id, arr, and hierarchy_arr.
 Ultimate_parent_id has the ultimate parent of the account. arr has the revenue for the account.
 and hierarchy_arr has the revenue for the account heirarchy. 

The database folder is to simulate where the data comes from. In practice, it would connect to
a database server and access data that way.

All the main files are located in the src folder.

Currently I have constructed a simple parent/child class system that will be used to relate the 
accounts together based on ids. I have also created a function that determines if subscriptions
are active or not. Which will be used to calculate the total revenue of an account. 

The revenue function is still in progress. 

I chose to use phython for this project mainly because the timeframe given to me and how fast I thought
I could get this finished. In practice phython is not as efficient as other languages. Prefered languages
would be SQL and/or C++.