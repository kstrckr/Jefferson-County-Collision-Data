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

        crash_values = (
        crash.master_file_number,
        crash.investigating_agency,
        crash.local_code,
        crash.collision_status_code,
        crash.county_name,
        crash.roadway_number,
        crash.block_or_house_number,
        crash.roadway_name,
        crash.roadway_suffix,
        crash.roadway_dir_code,
        crash.latitude,
        crash.longitude,
        crash.milepoint_derived,
        crash.collision_date,
        crash.collision_time,
        crash.intersection_roadway_number,
        crash.intersection_roadway_name, 
        crash.intersection_roadway_sfx,
        crash.between_st_roadway_num_1,
        crash.between_st_roadway_name_1,
        crash.between_st_roadway_sfx_1,
        crash.between_st_roadway_num_2,
        crash.between_st_roadway_name_2,
        crash.between_st_roadway_sfx_2,
        crash.units_involved,
        crash.motor_vehicles_involved,
        crash.killed,
        crash.injured,
        crash.weather_code,
        crash.weather,
        crash.roadway_condition_code,
        crash.roadway_condition,
        crash.hit_and_run_indication,
        crash.roadway_type_code,
        crash.roadway_type,
        crash.directional_analysis_code,
        crash.directional_analysis,
        crash.manner_of_collision_code,
        crash.manner_of_collision,
        crash.roadway_character_code,
        crash.roadway_character,
        crash.light_condition_code,
        crash.light_condition,
        crash.ramp_from_roadway_id,
        crash.ramp_to_roadway_id,
        crash.secondary_collision_indicator)

        insert_tuples.append(crash_values)

    insert_command = 'INSERT INTO crashes VALUES ' + '(' + ('?,'*45) + '?)'

    with db_conn:
        print('Inserting Rows')
        db_conn.executemany(insert_command, insert_tuples)

if __name__ == "__main__":

    csv_file = 'JEFFERSON COUNTY_CRASH DATA_2010-2017.csv'
    all_crashes = generate_accident_report_instances(generate_list_of_accident_rows(csv_file))

    db_conn = sqlite3.connect('crashes.db')

    insert_crashes(db_conn, all_crashes)