from datetime import datetime
import csv


# 1. Start by completing the read_csv_file function.
def read_csv_file(file_name):
    '''Reads a csv file and returns the data as a list.

    Args:
        file_name: a string representing the path and name of a csv file.

    Returns: a list.
    '''

    reading_file = []

    with open(file_name, encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        for line in reader:
            #print(line)
        
            reading_file.append(line)

    return reading_file


# 2. Complete the transform_daily_to_monthly function. 
# Two helper functions have been provided to help you determine the month each row of data was collected in. 
# These are: 
#   convert_mmddyyyy_date - to convert the date string to a datetime object (Python’s way of understanding dates).
def convert_mmddyyyy_date(date):
    '''Takes a date in the format mm/dd/yyyy and converts it to a datetime object.

    Args:
        date: string of a date in the mm/dd/yyyy format.

    Returns: a datetime object.
    '''
    return datetime.strptime(date, '%m/%d/%Y')


#   get_month_name - get the month name from a datetime object.
def get_month_name(date):
    '''Gets the month name from a datetime object.

    Args:
        date: a datetime object.

    Returns: the month name from the given date
        (e.g. "January", "February", etc).
    '''
    return date.strftime('%B')


def transform_daily_to_monthly(data):
    '''Transform the data from daily to monthly format.

    Args:
        data: a list of lists, where each sublist represents data
            for a specific day.

    Returns: a list of lists, where each sublist represents data
        for a whole month.
    '''
    monthly = {
        'October': [],
        'November': [],
        'December': [],
        'January': [], 
        'February': [],
        'March': []
    }

    for day in data:
        date = convert_mmddyyyy_date(day[0])
        month = get_month_name(date)
        monthly[month] = monthly[month] + [day[1:6]]

    for month in monthly.keys():
        days = monthly[month]
        # print(days)
        nests = 0
        false_crawls = 0
        hit_rocks = 0
        hatched_nests = 0
        nest_pred = 0
        
        for day in days:
            nests += int(day[0])
            false_crawls += int(day[1])
            hit_rocks += int(day[2])
            hatched_nests += int(day[3])
            nest_pred += int(day[4])

        print([month, nests, hatched_nests, false_crawls, hit_rocks, nest_pred])

    return [month, nests, hatched_nests, false_crawls, hit_rocks, nest_pred]

# 3. Complete the output_nests_per_month_graph function. 
# You’ll need to use the list created from the transform_daily_to_monthly function to get the number of nests recorded per month.

# 4. Complete the output_monthly_statistics function.

# 5. Complete the output_overall_statistics function.

# Note: you can use the format_text function to create the columns in the text output.
def format_text(text, spaces):
    '''Formats a string to be left aligned and take up a certain number of
        characters.

    Args:
        text: a string.
        spaces: the number of spaces the string should take up.

    Returns: the formatted string.
    '''
    return f"{text:<{spaces}}"


if __name__ == "__main__":
    all_data = read_csv_file('data/2020_2021_turtle_data.csv')
    all_data.remove(all_data[0])
    print(all_data)
    monthly_data = transform_daily_to_monthly(all_data)
    print()
    print(monthly_data)

    #print('2020/2021 Flatback Turtle Migration at Cemetery Beach')
    #print()


