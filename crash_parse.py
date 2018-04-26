import csv

crash_list = []

with open('JEFFERSON COUNTY_CRASH DATA_2010-2017.csv') as crash_csv:
    crash_reader = csv.reader(crash_csv)


    for line in crash_reader:
        crash_list.append(line)

for header in enumerate(crash_list[0]):
    print(header[0], header[1])

class AccidentReport:
    '''Represents an individual crash report and parses the data'''

    master_file_number = None
    investigating_agency = None
    local_code = None
    collision_status_code = None
    county_name = None
    roadway_number = None
    block_or_house_number = None
    roadway_name = None
    roadway_suffix = None
    roadway_dir_code = None
    latitude = None
    longitude = None
    milepoint_derived = None
    collision_date = None
    collision_time = None
    intersection_roadway_number = None
    intersection_roadway_name = None
    intersection_roadway_sfx = None
    between_st_roadway_num_1 = None
    between_st_roadway_name_1 = None
    between_st_roadway_sfx_1 = None
    between_st_roadway_num_2 = None
    between_st_roadway_name_2 = None
    between_st_roadway_sfx_2 = None
    units_involved = None
    motor_vehicles_involved = None
    killed = None
    injured = None
    weather_code = None
    weather = None
    roadway_condition_code = None
    roadway_condition = None
    hit_and_run_indication = None
    roadway_type_code = None
    roadway_type = None
    directional_analysis_code = None
    directional_analysis = None
    manner_of_collision_code = None
    manner_of_collision = None
    roadway_character_code = None
    roadway_character = None
    light_condition_code = None
    light_condition = None
    ramp_from_roadway_id = None
    ramp_to_roadway_id = None
    secondary_collision_indicator = None


    

    def __init__(self, crash_row):
        pass

