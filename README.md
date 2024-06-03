>**Note**: Please **fork** the current Udacity repository so that you will have a **remote** repository in **your** Github account. Clone the remote repository to your local machine. Later, as a part of the project "Post your Work on Github", you will push your proposed changes to the remote repository in your Github account.

### Date created
Include the date you created this project and README file.

### Project Title
Replace the Project Title

### Description
Describe what your project is about and what it does

### Files used
Include the files used

### Credits
It's important to give proper credit. Add links to any repo that inspired you or blogposts you consulted.

US Bikeshare Data Analysis
This project explores data related to bike share systems for three major cities in the United States: Chicago, New York City, and Washington. The project allows the user to filter the data by city, month, and day of the week to display various statistics.


pandas
numpy
You can install the required libraries using:

bash
Copy code
pip install pandas numpy
Usage
Clone the repository or download the script to your local machine.
Ensure that you have the CSV files (chicago.csv, new_york_city.csv, washington.csv) in the same directory as the script.
Run the script using:
bash
Copy code
python bikeshare.py
Follow the prompts to filter the data by city, month, and day of the week.
Project Structure
The project consists of a single Python script with the following functions:

get_filters(): Prompts the user for inputs to filter the data by city, month, and day.
load_data(city, month, day): Loads the data for the specified city and filters it by month and day.
time_stats(df): Displays statistics on the most frequent times of travel.
station_stats(df): Displays statistics on the most popular stations and trips.
trip_duration_stats(df): Displays statistics on the total and average trip duration.
user_stats(df): Displays statistics on bikeshare users.
display_raw_data(df): Displays raw data upon user request.
main(): Main function to run the script.
Functions
get_filters()
Prompts the user to specify a city, month, and day to analyze. Returns the user's choices.

load_data(city, month, day)
Loads the data for the specified city and filters by month and day if applicable. Returns a DataFrame.

time_stats(df)
Calculates and displays statistics on the most frequent times of travel.

station_stats(df)
Calculates and displays statistics on the most popular stations and trip.

trip_duration_stats(df)
Calculates and displays statistics on the total and average trip duration.

user_stats(df)
Calculates and displays statistics on bikeshare users, including user types, gender counts, and birth year statistics if available.

display_raw_data(df)
Displays raw data upon request by the user.

main()
Main function that runs the program. It gets user filters, loads data, and calls the appropriate functions to display statistics.

Data Sources
The data for this project is provided by Motivate, a bike share system provider for many major cities in the United States. The data files used in this project are:

chicago.csv
new_york_city.csv
washington.csv
Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

License
This project is licensed under the MIT License. See the LICENSE file for more details.