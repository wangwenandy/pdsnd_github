import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (string) city - name of the city to analyze
        (string) month - name of the month to filter by, or "all" to apply no month filter 
        (string) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    cities = ['chicago', 'new york city', 'washington']
    while True:
        city = input("Please enter the city name (chicago, new york city, washington): ").lower()
        if city in cities:
            break
        else:
            print("Invalid city name. Please try again.")
    
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month = input("Please enter the month (january, february, ... , june) or 'all' for no filter: ").lower()
        if month in months:
            break
        else:
            print("Invalid month. Please try again.")
    
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while True:
        day = input("Please enter the day of the week (monday, tuesday, ... , sunday) or 'all' for no filter: ").lower()
        if day in days:
            break
        else:
            print("Invalid day. Please try again.")
    
    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        df = df[df['month'].str.lower() == month]
    
    if day != 'all':
        df = df[df['day_of_week'].str.lower() == day]
    
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # display the most common month
    common_month = df['month'].mode()[0]
    print('Most Common Month:', common_month)
    
    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most Common Day of Week:', common_day)
    
    # display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:', common_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most Commonly Used Start Station:', common_start_station)
    
    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most Commonly Used End Station:', common_end_station)
    
    # display most frequent combination of start station and end station trip
    df['Start To End'] = df['Start Station'] + " to " + df['End Station']
    common_trip = df['Start To End'].mode()[0]
    print('Most Frequent Combination of Start Station and End Station Trip:', common_trip)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # display total travel time
    total_duration = df['Trip Duration'].sum()
    print('Total Travel Time:', total_duration)
    
    # display mean travel time
    mean_duration = df['Trip Duration'].mean()
    print('Mean Travel Time:', mean_duration)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of User Types:')
    print(user_types)
    
    if 'Gender' in df.columns:
        # Display counts of gender
        gender_counts = df['Gender'].value_counts()
        print('\nCounts of Gender:')
        print(gender_counts)
    
    if 'Birth Year' in df.columns:
        # Display earliest, most recent, and most common year of birth
        earliest_year = int(df['Birth Year'].min())
        most_recent_year = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print('\nEarliest Year of Birth:', earliest_year)
        print('Most Recent Year of Birth:', most_recent_year)
        print('Most Common Year of Birth:', common_year)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """Displays raw data upon request by the user."""
    row_start = 0
    row_end = 5
    show_data = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n').lower()
    
    while show_data == 'yes':
        print(df.iloc[row_start:row_end])
        row_start += 5
        row_end += 5
        show_data = input('\nWould you like to see 5 more lines of raw data? Enter yes or no.\n').lower()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart != 'yes':
            break

if __name__ == "__main__":
    main()
