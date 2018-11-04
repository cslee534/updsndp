import datetime
import pandas as pd
import numpy as np
import calendar

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def define_cities():
    '''Asks user to specify a city to begin data analysis'''
    # Asks for user prompt to start filtering data by city.(.title for returning string all caps)
    
    city_input = input('Would you like to see datasets for Washington, New York, or Chicago?\n').title()
    if city_input == 'Washington':
        return 'washington.csv'
    elif city_input == 'Chicago':
        return 'chicago.csv'
    elif city_input == 'New York':
        return 'new_york_city.csv'
    else: print('\n Invalid input. Please try again.')

    return define_cities()


def time_periods():
#.lower to return copy of string all lowercase
    input_time_data = input('Filter data by month, day, or none? Type "None" for no filter.\n').lower()
    if input_time_data == 'month':
        return ['month', month_data()]
    elif input_time_data == 'day':
        return ['day', weekday_data()]
    elif input_time_data == 'none':
        return['none', 'no filter']
    else: print('\nInvalid input. Please try again.')
    return time_periods()

def month_data():
    """Prompts user for month and returns it. Month number returned vs as string"""
    month_input = input ('\n What month do you wish to filter by?\n').title()
    if month_input == 'January':
        return '01'
    elif month_input == 'February':
        return '02'
    elif month_input == 'March':
        return '03'
    elif month_input == 'April':
        return '04'
    elif month_input == 'May':
        return '05'
    elif month_input == 'June':
        return '06'
    else: print('Invalid input. Please try again')
    return month_data()


def weekday_data():
    """Displays statistics on the most frequent times of travel."""
    weekday_input = input('\n What day do you wish to see? Please type the full weekday. \n').title()
    if weekday_input == 'Sunday':
        return 0
    elif weekday_input == 'Monday':
        return 1
    elif weekday_input == 'Tuesday':
        return 2
    elif weekday_input == 'Wednesday':
        return 3
    elif weekday_input == 'Thursday':
        return 4
    elif weekday_input == 'Friday':
        return 5
    elif weekday_input == 'Saturday':
        return 6
    else: print('\nInvalid input. Please try again.')
    return weekday_data()


def mode_month(df):
    """Retuns the most popular/mode trip taken within data frame bikeshare"""

    #Pandas Paramenters DataFrame.groupby(by=None, axis=0, level=None, as_index=True, sort=True, group_keys=True, squeeze=False, observed=False)
    #csv, Start Time, End Time
    month_trip_count = df.groupby('Month')['Start Time'].count()
    return 'Mode month with start time: ' + calendar.month_name[int(month_trip_count.sort_values(ascending=False).index[0])]


def mode_day(df):
    """Displays statistics on the total and average trip duration."""
    weekday_trip_count = df.groupby('Weekday')['Start Time'].count()

    #Pandas Paramenters DataFrame.groupby(by=None, axis=0, level=None, as_index=True, sort=True, group_keys=True, squeeze=False, observed=False)
    #csv, Start Time, End Time
    
    return 'Mode weekday for start time: '+ calendar.day_name[int(weekday_trip_count.sort_values(ascending=False).index[0])]


def mode_hour(df):
    """Displays statistics on the total and average trip duration."""
    
    hour_trip_count = df.groupby('Hour of Day')['Start Time'].count()
    
    mode_hour_val = hour_trip_count.sort_value(ascending=False).index[0]
    
    # datetime.strptime() class method creates a datetime object from a string representing 
    #a date and time and a corresponding format string
    
    mhv = datetime.datetime.strptime(mode_hour_val, '%H')

    #strftime Return a string representing the date, controlled by an explicit format string. 
    #Format codes referring to hours, minutes or seconds will see 0 values.
    
    return 'Mode hour of day for start time: ' + d.strftime("%I %p")


def trip_duration_stats(df):
    '''Data for total trip duration and avg calculcated'''
    
    average_trip_duration = df['Trip Duration'].mean()
    trip_duration_total = df['Trip Duration'].sum()
    # divmod() method takes two numbers and returns a pair of numbers (a tuple) consisting of their quotient and remainder.
    #Breakdown of times
    y, d = divmod(d, 365)
    d, h = divmod(h, 24)
    h, m = divmod(m, 60)
    m, s = divmod(total_trip_duration, 60)
    m, s = divmod(average_trip_duration, 60)
    h, m = divmod(m, 60)
    trip_duration_total = "\n Total duration elapsed:%d years %02d days %02d hrs %02d min %02d sec" % (y, d, h, m, s)
    average_trip_duration = "\n Average duration elapsed: %d hrs %02d min %02d sec" % (h, m, s)
    #Value 1 = String that shows avg value of trip durations
    #Value 2 = String that shows total sum of trip durations
    return [average_trip_duration, trip_duration_total]


def mode_stations_(df):
    """Displays statistics on the total and average trip duration."""
    #city csv's, start stations = 'Start Station'
    start_count = df.groupby('Start Station')['Start Station'].count()
    #city csv's, end stations = 'End Station'
    end_count = df.groupby('End Station')['End Station'].count()
    #sorting adj values with sort_values
    adj_start = start_count.sort_values(ascending=False)
    adj_end = end_count.sort_values(ascending=False)
    all_trips = df['Start Station'].count()
    mode_start = "\nMode start station is: " + adj_start.index[0] + " (" + str(adj_start_[0]) + " trips taken " 
    mode_end = "\nMode end station is: " +  adj_end.index[0] + " (" + str(adj_end[0]) + " trips taken"
    return [mode_start, mode_end]  


def mode_trip(df):
    """Text"""
    #Count unique trips by grouping start stations
    trip_count = df.groupby (['Start Station, End Station'])['Start Time'].count
    #Same as before with sorting
    adj_stations = trip_count.sort_values(ascending=False)
    total_trip_count = df['Start Station'].count()
    #String combo of start and end station mode of trips
    return "Mode trip taken: " + "Start station: " + str(adj_stations.index[0][0]) + "\n  End station: " + str(adj_stations.index[0][1]) + "\n  (" + str(adj_stations[0]) +  " trips "
    
def user_gender(df):
    '''Displays statistics on bikeshare user's gender.'''
    #Group by with dataset, 'Gender', in csv (not washington?)
    gender_value_count = df.groupby('Gender')['Gender'].count()
    return gender_value_count


def user_stats(df):
    """Displays statistics on bikeshare user type."""

    #Group by csv, 'User Type'
    user_type_count = df.groupby('User Type')['User Type'].count()
    return user_type_count


def user_age(df):
    """Age of the users from youngest to oldest, as well as mode"""

    #Group by csv, 'Birth Year' (not washington?)
    user_year_count = df.groupby('Birth Year')['Birth Year']
    #Youngest Users
    youngest_user_year = 'Youngest user year: ' + str(int(df['Birth Year'].min()))
    #Oldest Users
    oldest_user_year = 'Oldest user year: ' + str(int(df['Birth Year'].min()))
    #Adjusted for for sorts
    adj_user_year = user_year_count.sort_values(ascending=False)
    #Mode Birth Year
    mode_user_year = 'Mode user birth year : ' + str(int(adj_user_year.index[0]))
    return [youngest_user_year, oldest_user_year, mode_user_year]


def display_prompt(df):
    """Displays data, five lines at a time with what the user inputted.
       Also can prompt additional five lines should the user want."""

    display_question = input ('\n Do you wish to view additional trip data? Yes or no?')
    #Accounts for upper case response
    display_question = display_question.lower()
    if display_question == 'yes':
        print(df.iloc[current_line:current_line+5])
        current_line += 5
        return display_prompt(df, current_line)
    #Ceases
    if display_question == 'no':
        return
    #Check
    else:
        print('\nInput error. Please try again.')
        return display_prompt(df, current_line)

    
    
def stats():
    '''Shows the calculations and stats of the city and time frame selected by user'''
    #City selection and filtering
    city = define_cities()
    city_import = pd.read_csv(city)
    
    def filter_weekday(str_date):
        '''Date data gets formatted and correctly displays information as interger'''
    #1-4 are year values, 5-6 month values, 7-8 are day values, 9+ time hours
        get_date = datetime.date(int(str_date[0:4]), int(str_date[5:7]), int(str_date[8:10]))
        return get_date.weekday()
    #Get hour, day, and month from csv data files
    city_import['Hour of Day'] = city_import['Start Time'].str[11:13]
    city_import['Month'] = city_import['Start Time'].str[5:7]
    #This gets weekday from def
    city_import['Weekday'] = city_import['Start Time'].apply(filter_weekday)

    #Brings back user input filter from def_time_periods
    input_time_data = time_periods()
    filter_time_data = input_time_data[0]
    filter_time_set = input_time_data[1]
    filter_none = 'no filter'
    
    if filter_time_data == 'none':
        filter_df = city_import
    elif filter_time_data == 'month':
        filter_df = city_import.loc[city_import['Month'] == filter_time_set]
        filter_none = calendar.month_name[int(filter_time_set)]
    elif filter_time_data == 'day':
            filter_df = city_import.loc[city_import['Weekday'] == filter_time_set]
            filter_time_set = calendar.month_name[int(filter_time_set)]

            #PRINTING DATASETS AND INFORMATION
            print('\n')
            print('\n')
            print('\n')
            
            print(city[:-4].upper().replace("_", " ") + ' - ' + filter_time_set.upper())
            print('+++++++++++++++++++++++++++++++++++++++++++++++++++')

            #Mode Section Print(Month, Weekday, Hour, Trip, Start/End Station
            if filter_time_data == 'none' or filter_time_data == 'day':
                print(mode_month(filter_df))
                if filter_time_data == 'month' or 'none':
                    print(mode_day(filter_df))
                    print(mode_hour(filter_df))
                    print(mode_trip(filter_df))
                    print(mode_start(filter_df))
                    print(mode_end(filter_df))
                    print('\n')

            #Total Trips Taken, trip duration, and avg
            total_duration_stat = trip_duration_stats(filter_df)
            print('Total Trips taken: ' + "{:,}" .format(filter_df['Start Time'].count()))
            print('\n')
            print(total_duration_stat[0])
            print(total_duration_stat[1])

            #User Data, status, age, gender
            user_age_years = user_age(filter_df)
            print('\n')
            print(user_stats(filter_df))
            if city_input == 'chicago.csv' or city_input == 'new_york_city.csv':
                print('')
            print(user_gender(filter_df))
            print(user_age_years[0])
            print(user_age_years[1])
            print(user_age_years[2])

            #Five lines
            display_prompt(filter_df, 0)

def restart_prompt():
    ''' Restart question to prompt on user input'''
    restart = input ('Restart the search? Yes or no?')
    #Check for lower input
    if restart_prompt.lower() == 'yes':
        stats()
    elif restart_prompt.lower() == 'no':
        return
    else:
        print ('\nInput Error. Please try again')
        return restart_prompt()
    
    
    restart_prompt()
    
if __name__ == "__main__":
    stats()

#Updating for Section 4