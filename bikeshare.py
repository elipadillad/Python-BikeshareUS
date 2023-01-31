import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_user_inputs(prompt, valid_input):
    """function for asking the user a valid input, this is checked in the main() function"""

    while True:
        
        value = input(prompt).lower()
        
        if value not in valid_input:
            print('Please enter a valid input 😟  ')
            continue
        else: 
            #the input it's okay
            break
    return value

def load_data(city, month, day):
   
 # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...🤔\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('Most Common Month:', most_common_month)

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('Most Common Day of Week:', most_common_day)

    # TO DO: display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:', most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...😎\n')
    start_time = time.time()
    #create new columns
    df['Start Station'] = df['Start Station'].mode()[0]
    df['End Station'] = df['End Station'].mode()[0]
    
    # TO DO: display most commonly used start station
    common_start_s = df['Start Station'].mode()[0]
    print('Most Commonly Used Start Station:', common_start_s)
    
    # TO DO: display most commonly used end station
    common_end_s = df['End Station'].mode()[0]
    print('Most Commonly Used End Station:', common_end_s)

    # TO DO: display most frequent combination of start station and end station trip
    combination_start_end = df.groupby(['Start Station','End Station']).size().idxmax()
    print("The Most Frequent Combination Of Start Station and End Station Trip is: \n {}".format(combination_start_end))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...😯\n')
    start_time = time.time()
    #create new columns
    df['Trip Duration'] = df['Trip Duration'].mode()[0]
    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()   # in seconds unit
    print("The Total Travel is {} seconds".format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()   #in seconds unit
    print("The Mean Travel Time is {} seconds".format(mean_travel_time))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...🤓\n')
    start_time = time.time()

    # TO DO: Display counts of user types
   
    counts_user_types = df['User Type'].value_counts()
    print("The Count of User Types are:\n", counts_user_types)
   
    print('\n')
    # Next is specific for Chicago and New York City
    # TO DO: Display counts of gender
    try:
       
         gender_counts = df['Gender'].value_counts()
         print("The Count of Gender is:\n", gender_counts)
            
    except KeyError:
         print("The Display of Gender is not available to Washington")
    print('\n')
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
    
         earliest = df['Birth Year'].min()
         most_recent = df['Birth Year'].max()
         most_common = df['Birth Year'].mode()
         print("The Earliest year of birth is {}, The Most Recent year of birth is {}, The Most Common year of birth is {}".format(earliest, most_recent, most_common))
         
    except KeyError:
                print("The Display of Year of Birth is not available to Washington")
                
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True: 
        print('Hello! Let\'s explore some US bikeshare data! 🚲')
        print('\n')
        city = get_user_inputs('Please enter a city 🗽 (chicago, new york city, washington): ', ['chicago', 'new york city', 'washington'])
        month = get_user_inputs('Please enter a month 📅 (all, january, february, march, april, may, june): ', ['all', 'january', 'february', 'march', 'april', 'may', 'june'])
        day = get_user_inputs('Please enter a day of week 📆 (all, monday, tuesday, wednesday, thursday, friday, saturday, sunday): ', ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'])

        print('-'*40)
           
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        

#To see more data 
        i = 0
        view_more_data = input("\nWould you like to view 5 rows of individual trip data? 👀  Enter yes or no.\n").lower()
        pd.set_option('display.max_columns',200)
        
        while True:            
            if view_more_data == 'no':
                break
            print(df[i:i+5])
            view_more_data = input('\n"Do you wish to continue? 📊  Enter yes or no.\n').lower()
            i += 5   

#Restart 
        restart = input('\nWould you like to restart? 🧐  Enter yes or no.\n')
        if restart.lower() == 'no' or restart.lower() == 'n':
            break
        
    
    
if __name__ == "__main__":
    main()
   


    
    
    