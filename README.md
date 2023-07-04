Python Challenge 
PyBank: Analysis of monthly profit/loss data.
PyPoll: Analysis of election results.

Background: 
In this assignment we were tasked with creating two seperate Python scripts to properly analyze a set of financial data, and a set of election results. In the PyBank dataset found in the PyBank folder Resources, we used two columns to help us develop a script to run through all of it and produce certain results. The PyPoll dataset found in the same folder under PyPoll had us look through data of an election and print out the winner along with the total votes, votes per candidate and percentage of votes won. 

PyBank: 
In this script we set out to find the total months in the dataset, the net amount of profit/losses over the whole period of time, average changes in the P&L over that time, and the greatest increases and decrease in profits nad losses. I utilized for loops and if statements to help me run through the dataset comparing current profit loss and months to our CSV. This allowed me to then determine the net profit loss by stating if months is equal to 1 then the previous month loss was equal to the current profit loss. And then I determined the change and appended our month and overall profit loss variables to reflect what we had found. Once I did that, we simply used fuctions like sum, max, min, round, and index to sort through all of the data we have. Then I simply printed it to the terminal and wrote it to a text file to be saved in our Analysis folder. Below is our text file results.

[analysis.txt](https://github.com/stoddow313/Python-Challenge/files/11944138/analysis.txt)

![image](https://github.com/stoddow313/Python-Challenge/assets/134353666/371ddfa1-f021-4606-b319-13acd9b81cbc)


PyPoll:
This script was similar but had a few more things to work out for me. I import the necessary dependencies and defined my variables of total votes, votes per candidate and the output given to me in the assignment module. This was to help me print the proper verbiage as I was having trouble doing it later in my script. But found this to solve that issue. After that, I simply ran a few for loops for each of my variables to read the CSV as what they are equal to with the append function. And then redefined certain variables in order to find the total votes, winner, votes per candidate, and percentage of votes won. ONce I was able to do all that using the length function, and a few others, we were able to calculate our percnetage and print the output properly. Then I did the same as in PyBank and wrote it to a text file to be saved in the Analysis folder of PyPoll. Below are the results on that text file. 

[analysis.txt](https://github.com/stoddow313/Python-Challenge/files/11944156/analysis.txt)

I did have some help from google and the slides provided by Thomas Tellner and the UO Data Analytics Bootcamp in learning how to read files in, and write them out as well as learning some functions to make this smooth. 

![image](https://github.com/stoddow313/Python-Challenge/assets/134353666/3d55459d-b929-4d08-9266-c40dce2e1b04)
