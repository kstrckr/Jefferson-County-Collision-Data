import csv
import sqlite3

from crash_parse import AccidentReport

def generate_list_of_accident_rows(csv_file):

    crash_list = []

    with open(csv_file) as crash_csv:
        crash_reader = csv.reader(crash_csv)

        for line in crash_reader:
            crash_list.append(line)
    
    return crash_list

def generate_accident_report_instances(list_of_crashes):

    all_crash_instances = []

    for crash in list_of_crashes[1:]:
        all_crash_instances.append(AccidentReport(crash))

    return all_crash_instances

def insert_crashes(db_conn, all_crash_instances):
    
    insert_tuples = []

    for crash in all_crash_instances:

        insert_tuples.append(crash.return_insert_tuple())

    insert_command = 'INSERT INTO crashes VALUES ' + '(' + ('?,'*45) + '?)'

    with db_conn:
        print('Inserting Rows')
        db_conn.executemany(insert_command, insert_tuples)

if __name__ == "__main__":

    csv_file = 'JEFFERSON COUNTY_CRASH DATA_2010-2017.csv'
    all_crashes = generate_accident_report_instances(generate_list_of_accident_rows(csv_file))

    db_conn = sqlite3.connect('crashes.db')

    insert_crashes(db_conn, all_crashes)