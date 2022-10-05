# Sean Perez
# 28/09/2022
# For use by Phillipstown Community Centre and their Human Resources branch.

import csv
import os
import sys
from datetime import datetime, timedelta


def get_date():
    now = datetime.now().date() - timedelta(days=3)

    # Creates and offset for when the sunday will be
    sun_offset = abs(now.weekday() - 6)

    # Calculates start of week and formats it correctly
    monday = str(now - timedelta(days=now.weekday()))
    monday = f"{monday[-2:]}/{monday[5:7]}/{monday[:4]}"

    # Calculates end of week and formats it correctly
    sunday = str(now + timedelta(days=sun_offset))
    sunday = f"{sunday[-2:]}/{sunday[5:7]}/{sunday[:4]}"
    return f"{monday} to {sunday}"


def convert_dates(str_date):
    """Takes string of date in 202212251037 and converts to 25/12/2022 10:37"""
    date = f"{str_date[6:8]}/{str_date[4:6]}/{str_date[0:4]} {str_date[-4:-2]}:{str_date[-2:]}"
    return date


def create_file(worker, total_num_keys):
    """Creates new csv file and adds the required formats"""
    title = ['Timesheet', '', get_date()]
    header = ['Name', 'Star Time', 'Finish Time', 'Total Time', 'Break', 'Sick', 'Annual', 'Public Holiday']

    # Total pay will be appended to this list and passed to the document.
    total_header = ['Total pay per hour (STD)', 'Total Sick (Paid)', 'Total Sick (Unpaid)', 'Total Annual (Paid)', 'Total Annual (Unpaid)', 'Total Public Holiday']
    now = datetime.now().date() - timedelta(days=3)
    monday = str(now - timedelta(days=now.weekday()))

    calculated_data = calculate_totals(import_csv())

    with open(f'TS_week_of_{monday}.csv', 'w+') as fl:
        writer = csv.writer(fl)

        # write the header
        writer.writerow(title)

        for _ in range(total_num_keys):
            writer.writerow(header)

            writer.writerow(total_header)

        return

        # write the data
        # writer.writerow(data)


# Validates file name input
def file_read_val():
    if len(sys.argv) <= 1:
        return False

    if ".csv" not in " ".join(sys.argv[1:]):
        return False

    return True


def list_to_dict(list_to_dic, reader) -> dict:
    # For every row, as long as there is a valid email with the at sign,
    # it will use that as key to create a list or append to existing list
    for row in reader:
        if "@" in row[-3]:
            # email_set.add(row[-3].strip('"'))
            try:
                list_to_dic[row[-3].strip('"')].append([s.strip('"') for s in row])
            except KeyError:
                list_to_dic[row[-3].strip('"')] = [s.strip('"') for s in row]

    return list_to_dic


def calculate_totals(email_dic):
    """loops through every user, figures out what each row will be"""




def dict_to_dict(dic_to_dic) -> dict:
    # For every key, create another key with the date. That date key has a value of a list of lists.

    for row in dic_to_dic:
        if "@" in row[-3]:
            # email_set.add(row[-3].strip('"'))
            try:
                dic_to_dic[row[-3].strip('"')].append(row)
            except KeyError:
                dic_to_dic[row[-3].strip('"')] = row

    return dic_to_dic


# Total times is in minutes; convert to hours in float.
def import_csv():
    """Import the file from the path"""
    # Checks to see if file was added and if it has the file type in the name
    if not file_read_val():
        error_msg = "No file name or file type '.csv' was provided, " \
                    "please try again by writing: python main.py NAME-OF-FILE.csv"
        print(error_msg)
        return

    # Creates the path that the new csv file will be created in the root directory (where the py file is located)
    read_path = " ".join(sys.argv[1:])

    with open(f'{read_path}', newline='') as csv_file:
        reader = list(csv.reader(csv_file, quotechar='|'))

        email_dic = list_to_dict({}, reader)

        return email_dic


        # use a for loop for each user; a for loop for each date. (if "email" and "start date" in row_entry_list)
        # Creates whole data dic with keys == UserEmail
        # data_dic = {}
        #
        # for email in email_set:
        #
        # data_dic[row[0].strip('"')]


if __name__ == "__main__":
    import_csv()
    get_date()
    convert_dates("202212251037")

