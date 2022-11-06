## Project 3  - Correlating COVID-19 data with a company Excel sheet

*A fictional case on how to use Python at your workplace*

*(Source Code in sample_code/project_covid_happiness)*

### The issue
- We work in an Austrian company and are responsible for some organisational kinda stuff
- We were given a bunch of Excel sheets, one for EACH employee of our company
 - Each Excel sheet contains the individual employee's happiness level for each week of the year
- We want to know if there are general happiness trends throughout the year within the company
- We also feel like the whole thing has something to do with COVID...

- Naturally, we want to see if we can correlate the average happiness with some COVID data.

### The solution
Our program shall do the following:
1. Go through all Excel sheets in a specific folder using a for loop
 - Read out the happiness levels of each employee-sheet and temporarily save them
1. Open another Excel sheet and enter the AVERAGE of the happiness of all employees in that sheet
1. Get "total confirmed cases of COVID-19" of AUSTRIA of the past months and add that data next to our employee-happiness-average

*(We could then do some crazy correlation stuff using Python as well but.... this is no Data Science class, sorry)*

