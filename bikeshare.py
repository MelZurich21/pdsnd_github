"""file to submit from student Melinda Rokolya: US Bikeshare Python project"""

import time
import pandas as pd
import numpy as np

   # loading the .csv files

CITY_DATA = { 'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv' }

def get_filters():
    """
    This function starts the user interface by introduction and
    asks user to specify a city, month, and day to analyze.
     
  
    Returns:
       (str) city - name of the city to analyze
       (str) month - name of the month to filter by, or "all" to apply no month filter
       (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # Part 1/5 get user input for city (chicago, new york city, washington) month and day

    cities=['chicago','new york city','washington']

    months = [ 'january', 'february', 'march', 'april', 'may', 'june', 'all']

    days = [ 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','all']

    # get user input for City using while loop
    while True:
        city=str(input('\nWhich city would you like to explore?').lower())
        if city not in cities:
            print('\nSorry, your chosen city is not available, please choose from Chicago, New York city or Washington')
        else:
            print('You have selected: ', city)
            break
    # get user input for month (from january, february, ... , june)using while loop
            month=' '
    while True:
        month=str(input('Enter month to filter by months: ').lower())
        if month not in months:
            print('\nUps! Invalid month, please choose from january to june any month or choose\n all')
        else:
            print('You have selected: ', month)
            break
    # get user input for day of week (from monday, tuesday, ... sunday)using while loop
            day=' '
    while True:
        day=str(input('Enter day to filter by days: ').lower())
        if day not in days:
            print('\nUps! Invalid day, please choose monday to sunday any day or choose\n all')
        else:
            print('You have selected: ', day)
            break

    print('-'*40)

    return city, month, day


def load_data(city, month, day):
    # loads data for the specified city
    df=pd.read_csv(CITY_DATA[city])
    
    # extracts from Start Time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] =df['Start Time'].dt.month
    print("this is how month looks like: ")
    print(df['month'])

    df['day_of_week'] = df['Start Time'].dt.weekday_name
    print("this is how day of week looks like: ") 
    print(df['day_of_week'])

    df['hour'] = df['Start Time'].dt.hour

    if month.lower() != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        print("month after converted into integer: ")
        print(month)
        df = df.loc[df['month'] == month]
        print("here is data after month filter: ")
        print(df)

    if day.lower() != 'all':
        df = df.loc[df['day_of_week'] == day.title()]
        print("here is data after day filter: ")
        print(df)
    return df


    #Part 2/5: statistics on the most frequent times of travel

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # displays the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('Most Common Start Month: ', popular_month)
    # displays the most common day of week
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day'] = df['Start Time'].dt.day
    popular_day = df['day'].mode()[0]
    print('Most Common Start Day: ', popular_day)
    # displays the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Common Start Hour: ', popular_hour)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # part 3/5 statistics on the most popular stations and trip
def station_stats(df):    
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    # creates a column for start station, end station
    df['Start Station'] = df['Start Station'].mode()[0]
    df['End Station'] = df['End Station'].mode()[0]
    # displays most commonly used start station

    common_start = df['Start Station'].mode()[0]
    print("The most popular start station is \n{}".format(common_start))

    # displays most commonly used end station
    common_end = df['End Station'].mode()[0]
    print("The most popular end station is \n{}".format(common_end))
    # displays most frequent combination of start station and end station trip

    popular_trip=df.groupby(['Start Station', 'End Station']).size().nlargest(1)
    print("The most popular trip from start to end is \n {}".format(popular_trip))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # part 4/5 total travel time & average travel time statistics
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # displays total travel time
    total_duration = df['Trip Duration'].sum()
    print(total_duration)
    print("The total trip duration is in seconds \n {}".format(total_duration))

    # displays mean travel time
    average_trip_duration = df["Trip Duration"].mean()
    print("The averige trip duration is in seconds \n {}".format(average_trip_duration))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    # part 5/5 bikeshare users statistics: user types & gender, birth dates
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # displays counts of user types

    print('User Type Stats:')

    print(df['User Type'].value_counts())


   # displays counts of gender

    if "Gender" in df.columns:
         print(':')

         print(df['Gender'].value_counts())

    else:
             print("Gender data can't be displayed as no gender data for Washington exists")

    # displays earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
         print('Birth Year Data:')

         earliest_year = df['Birth Year'].min()

         print('Earliest Year:',earliest_year)

         most_recent_year = df['Birth Year'].max()

         print('Most Recent Year:',most_recent_year)

         most_common_year = df['Birth Year'].mode()[0]

         print('Most Common Year:',most_common_year)

         print("\nThis took %s seconds." % (time.time() - start_time))
    else:
             print("Birth date data can't be displayed as no data for Washington exists")

    print('-'*40)


    #additional 5 rows view optional question with restart
def display_data(df):
    BIN_RESPONSE_LIST = ['yes', 'no']
    rdata = ''
    counter = 0
    while rdata not in BIN_RESPONSE_LIST:
        print("\nDo you wish to view the raw data?")
        print("\nAccepted responses:\nYes or yes\nNo or no")
        rdata = input().lower()
        #raw data print in bold cyan 
        if rdata == "yes":
            print('\033[1;96m=\033[1;m'*40)
            print(df.head())
        elif rdata not in BIN_RESPONSE_LIST:
            print("\nPlease check your input.")
            print("Input does not seem to match any of the accepted responses.")
            print("\nRestarting...\n")


            
    #additional while loop asking to view more raw data print in bold cyan 
    while rdata == 'yes':
        print('\033[1;96m=\033[1;m'*40)   
        print("Do you wish to view more raw data?")
        counter += 5
        rdata = input().lower()
        #if yes it displays next 5 rows of data print in bold cyan 
        if rdata == "yes":
            print('\033[1;96m=\033[1;m'*40)
            print(df[counter:counter+5])
        elif rdata != "yes":
            break
            

    print('-'*80)

    
       #main function to call all the previous functions
def main():
     while True:
         city, month, day = get_filters()
         df = load_data(city, month, day)

         time_stats(df)
         station_stats(df)
         trip_duration_stats(df)
         user_stats(df)
         display_data(df)

         restart = input('\nWould you like to restart? Enter yes or no.\n')
         if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
