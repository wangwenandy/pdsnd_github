Project Overview
This project explores data from bike share systems in three major US cities: Chicago, New York City, and Washington, DC. The Python script provided allows for the analysis of this data, computing descriptive statistics, and provides an interactive terminal experience for users to filter and view the data.

Datasets
The datasets used contain randomly selected data for the first six months of 2017 for each city. Each data file includes the following columns:
Start Time: The start time of the trip (e.g., 2017-01-01 00:07:57)
End Time: The end time of the trip (e.g., 2017-01-01 00:20:53)
Trip Duration: Duration of the trip in seconds (e.g., 776)
Start Station: The starting station name (e.g., Broadway & Barry Ave)
End Station: The ending station name (e.g., Sedgwick St & North Ave)
User Type: Type of user (Subscriber or Customer)
Additionally, the Chicago and New York City datasets include:
Gender
Birth Year

Files
The following files are required to run the program:
chicago.csv
new_york_city.csv
washington.csv
Software Requirements
Python 3
NumPy
Pandas
These packages can be installed using Anaconda or pip.

Script Overview
The script (bikeshare.py) performs the following tasks:
User Input: Prompts the user to specify a city, month, and day to analyze.
Load Data: Loads data for the specified city and filters it by the specified month and day.
Compute Statistics: Calculates and displays various statistics:
Popular times of travel
Popular stations and trip
Trip duration
User information (including counts of user types, gender, and birth year statistics)
Display Raw Data: Offers the user the option to view raw data in chunks of 5 rows.

How to Run the Script
Ensure that Python 3 and the required packages (NumPy and Pandas) are installed.
Place the chicago.csv, new_york_city.csv, and washington.csv files in the same directory as the script.
Run the script from the terminal:
python bikeshare.py
Follow the prompts to input the desired city, month, and day for analysis.

Resources
Python Standard Library
Pandas Documentation
Stack Overflow